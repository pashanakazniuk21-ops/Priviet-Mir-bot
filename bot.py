#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import asyncio
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)
from utils import ensure_data_dir, add_user_if_new, get_stats

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise SystemExit("ERROR: BOT_TOKEN is not set in .env")

# Optional admin ID for restricted commands (set in .env)
ADMIN_ID = int(os.getenv("ADMIN_ID") or 0)

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Ensure data directory and files exist
ensure_data_dir()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat
    add_user_if_new(user, chat)
    keyboard = [
        [InlineKeyboardButton("Помощь", callback_data="help")],
        [InlineKeyboardButton("Инфо", callback_data="info")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"Привет, {user.first_name}! Я локальный бот.\nНажми кнопку или введи /help.",
        reply_markup=reply_markup,
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "/start — старт\n"
        "/help — показать это сообщение\n"
        "/info — информация о боте\n"
        "/stats — статистика (только админ)\n\n"
        "Отправьте любой текст — бот его повторит."
    )
    await update.message.reply_text(text)


async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот локальный. Работает в режиме polling. Автор: вы.")


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if ADMIN_ID and user.id != ADMIN_ID:
        await update.message.reply_text("Команда доступна только администратору.")
        return
    stats = get_stats()
    await update.message.reply_text(
        f"Статистика:\nВсего пользователей: {stats.get('users_count', 0)}"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # simple echo + store user
    if update.message:
        user = update.effective_user
        chat = update.effective_chat
        add_user_if_new(user, chat)
        await update.message.reply_text(update.message.text)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    if data == "help":
        await query.edit_message_text("Это помощь. Используйте /help для списка команд.")
    elif data == "info":
        await query.edit_message_text("Информация: локальный бот, запущен в polling режиме.")
    else:
        await query.edit_message_text(f"Нажата кнопка: {data}")


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("Неизвестная команда. Используйте /help.")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("info", info_command))
    app.add_handler(CommandHandler("stats", stats_command))

    # callback queries (inline buttons)
    app.add_handler(CallbackQueryHandler(button_handler))

    # messages: echo everything that is text and not command
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))

    # unknown commands
    app.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    logger.info("Bot starting (polling)...")
    app.run_polling()


if __name__ == "__main__":
    main()
