[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Chart Session Tracker Bot 📈

A Discord bot to help traders share their current market analysis status live in a server.

---

## Features

- Set your trading category (Indices, Commodities, Forex Majors/Crosses, All).
- Automatically detects Forex trading sessions based on your timezone.
- Announce your current status in a `#status` channel.
- Mark yourself done via command or interactive button.
- Status auto-expires after 12 hours to keep things clean.

---

## Commands

- `/setstatus category timezone` — Start sharing your trading session.
- `/done` — Mark your trading session as finished.
- ✅ Interactive **Done** button to clear your status.

---

## Setup Instructions

1. Clone this repo:

   ```bash
   git clone https://github.com/Prasannaram2k4/chart-session-tracker-bot.git
   cd chart-session-tracker-bot
Create a Discord bot on the Discord Developer Portal and get your token.

Enable the following Privileged Gateway Intents on your bot's page:

Presence Intent

Server Members Intent

Message Content Intent

Create a .env file in the project root and add your bot token:

ini
Copy
Edit
DISCORD_TOKEN=your_bot_token_here
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the bot:

bash
Copy
Edit
python main.py
Usage
Use /setstatus to start sharing your market analysis session.

Use /done when you finish.

Your status will be posted automatically in the #status channel.

Contributing
Contributions are welcome! Please see CONTRIBUTING.md for contribution guidelines.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Made with ❤️ by Prasannaram2k4


