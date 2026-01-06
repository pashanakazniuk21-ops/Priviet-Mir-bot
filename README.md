# Priviet-Mir-bot

A comprehensive Discord bot for community management and engagement.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Windows PowerShell](#windows-powershell)
  - [Linux](#linux)
  - [macOS](#macos)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Community moderation tools
- User engagement features
- Command-based interaction system
- Real-time message processing
- Configurable permissions and roles

## Requirements

- Python 3.8 or higher
- pip (Python package manager)
- Discord bot token
- Git (for installation)

## Installation

### Windows PowerShell

#### Step 1: Clone the Repository

```powershell
git clone https://github.com/pashanakazniuk21-ops/Priviet-Mir-bot.git
cd Priviet-Mir-bot
```

#### Step 2: Create a Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If you encounter an execution policy error, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then rerun the activation command.

#### Step 3: Install Dependencies

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

#### Step 4: Configure Environment Variables

Create a `.env` file in the project root directory:

```powershell
New-Item -Name ".env" -ItemType File
```

Add your Discord bot token and configuration:

```
DISCORD_TOKEN=your_bot_token_here
PREFIX=!
```

#### Step 5: Run the Bot

```powershell
python bot.py
```

---

### Linux

#### Step 1: Clone the Repository

```bash
git clone https://github.com/pashanakazniuk21-ops/Priviet-Mir-bot.git
cd Priviet-Mir-bot
```

#### Step 2: Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### Step 4: Configure Environment Variables

Create a `.env` file in the project root directory:

```bash
touch .env
nano .env
```

Add your Discord bot token and configuration:

```
DISCORD_TOKEN=your_bot_token_here
PREFIX=!
```

Save and exit (Ctrl+X, then Y, then Enter in nano).

#### Step 5: Run the Bot

```bash
python3 bot.py
```

#### (Optional) Run as a Background Service

To run the bot as a systemd service, create a service file:

```bash
sudo nano /etc/systemd/system/priviet-mir-bot.service
```

Add the following content:

```ini
[Unit]
Description=Priviet-Mir-bot Discord Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/Priviet-Mir-bot
ExecStart=/path/to/Priviet-Mir-bot/venv/bin/python3 bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Then enable and start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable priviet-mir-bot
sudo systemctl start priviet-mir-bot
sudo systemctl status priviet-mir-bot
```

---

### macOS

#### Step 1: Clone the Repository

```bash
git clone https://github.com/pashanakazniuk21-ops/Priviet-Mir-bot.git
cd Priviet-Mir-bot
```

#### Step 2: Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### Step 4: Configure Environment Variables

Create a `.env` file in the project root directory:

```bash
touch .env
nano .env
```

Add your Discord bot token and configuration:

```
DISCORD_TOKEN=your_bot_token_here
PREFIX=!
```

Save and exit (Ctrl+X, then Y, then Enter in nano).

#### Step 5: Run the Bot

```bash
python3 bot.py
```

#### (Optional) Run with LaunchAgent for Background Execution

To run the bot automatically at startup, create a LaunchAgent plist file:

```bash
mkdir -p ~/Library/LaunchAgents
nano ~/Library/LaunchAgents/com.privietmir.bot.plist
```

Add the following content (replace `YOUR_USERNAME` with your macOS username):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.privietmir.bot</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/YOUR_USERNAME/path/to/Priviet-Mir-bot/venv/bin/python3</string>
        <string>/Users/YOUR_USERNAME/path/to/Priviet-Mir-bot/bot.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardErrorPath</key>
    <string>/Users/YOUR_USERNAME/path/to/Priviet-Mir-bot/bot.log</string>
    <key>StandardOutPath</key>
    <string>/Users/YOUR_USERNAME/path/to/Priviet-Mir-bot/bot.log</string>
</dict>
</plist>
```

Then load the LaunchAgent:

```bash
launchctl load ~/Library/LaunchAgents/com.privietmir.bot.plist
launchctl start com.privietmir.bot
```

To check status:

```bash
launchctl list | grep com.privietmir.bot
```

---

## Configuration

### Environment Variables

The bot uses a `.env` file for configuration. Create this file in the project root with the following variables:

```
DISCORD_TOKEN=your_bot_token_here
PREFIX=!
LOG_LEVEL=INFO
```

### Getting Your Discord Bot Token

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Navigate to the "Bot" section
4. Click "Add Bot"
5. Copy the token and add it to your `.env` file

---

## Usage

### Basic Commands

Once the bot is running, you can interact with it in your Discord server using the configured prefix (default: `!`).

#### Examples:

```
!help              - Show all available commands
!ping              - Check bot latency
!status            - Show bot status
```

### Viewing Logs

#### Windows PowerShell:
```powershell
Get-Content -Path "bot.log" -Tail 50
```

#### Linux/macOS:
```bash
tail -f bot.log
```

### Stopping the Bot

#### Windows PowerShell:
```powershell
Ctrl+C
```

#### Linux/macOS:
```bash
Ctrl+C
```

#### Linux (systemd service):
```bash
sudo systemctl stop priviet-mir-bot
```

#### macOS (LaunchAgent):
```bash
launchctl stop com.privietmir.bot
```

---

## Troubleshooting

### Bot Not Responding

1. Verify the bot token is correct in `.env`
2. Check that the bot has proper permissions in Discord server
3. Ensure the bot is online (check Discord server member list)
4. Review logs for error messages

### Import Errors

If you encounter import errors, ensure all dependencies are installed:

```bash
pip install -r requirements.txt
```

### Virtual Environment Issues

To deactivate and reactivate your virtual environment:

#### Windows PowerShell:
```powershell
deactivate
.\venv\Scripts\Activate.ps1
```

#### Linux/macOS:
```bash
deactivate
source venv/bin/activate
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Support

For issues, questions, or suggestions, please open an issue on the [GitHub repository](https://github.com/pashanakazniuk21-ops/Priviet-Mir-bot/issues).

---

**Last Updated:** 2026-01-06
