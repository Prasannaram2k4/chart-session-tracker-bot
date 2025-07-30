# Chart Session Tracker Bot 📈

A Discord bot to help traders share their current market analysis status live in a server.

---

## Features

- Set your trading category (Indices, Commodities, Forex Majors/Crosses, All).
- Automatically detects Forex trading sessions based on your timezone.
- Announce your current status in a `#status` channel.
- Mark yourself done via command or interactive button.
- Status auto-expires after 12 hours to keep things tidy.

---

## Commands

- `/setstatus category timezone` — Start sharing your trading session.
- `/done` — Mark your trading session as finished.
- ✅ Interactive **Done** button to clear your status.

---

## Setup Instructions

1. Clone this repo: git clone https://github.com/Prasannaram2k4/chart-session-tracker-bot.git
cd chart-session-tracker-bot

2. Create a Discord bot in the [Discord Developer Portal](https://discord.com/developers/applications) and get your token.

3. Enable the following Privileged Gateway Intents for your bot:
- Presence Intent  
- Server Members Intent  
- Message Content Intent

4. Create a `.env` file in the project root and add your bot token: DISCORD_TOKEN=your_bot_token_here

5. Install dependencies: pip install -r requirements.txt

6. Run the bot:


---

## Usage

- `/setstatus category timezone` — Start sharing your current market analysis session.
- `/done` — Mark your trading session as finished.
- `/status` — View your current session status.
- `/help` — Display a help message with available commands.
- Use the ✅ **Done** button on your status message to clear it quickly

---

## Contributing

Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to contribute.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by Prasannaram2k4
