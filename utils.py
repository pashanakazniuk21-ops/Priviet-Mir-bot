# Утилиты для простого хранения пользователей в JSON-файле
import os
import json
from typing import Optional
from telegram import User, Chat

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")


def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump({"users": []}, f, ensure_ascii=False, indent=2)


def _load_users():
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_users(data):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_user_if_new(user: User, chat: Chat):
    data = _load_users()
    users = data.get("users", [])
    # identify by user.id
    if not any(u.get("id") == user.id for u in users):
        users.append(
            {
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "chat_id": chat.id,
            }
        )
        data["users"] = users
        _save_users(data)


def get_stats():
    data = _load_users()
    users = data.get("users", [])
    return {"users_count": len(users)}