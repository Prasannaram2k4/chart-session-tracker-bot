# Market Pulse Bot 📈

A Discord bot to help traders share their current market analysis status live in a server.

---

## Features

- 📈 Set your trading category (Indices, Commodities, Forex Major/Cross, All).
- 🌐 Choose your timezone to determine the current market session.
- 📢 Posts your status to the `#status` channel automatically.
- ✅ Clickable Done button or `/done` command to end your session.
- 🕒 Status expires automatically after 12 hours.
---

## Commands


- `/setstatus category timezone` — Start sharing your trading session.  
  Example: `/setstatus category:"Forex (Major)" timezone:"Asia/Kolkata"`  
  (Both category and timezone are selected from dropdown lists.)

- `/done` — Mark your trading session as finished.

- `/status` — View everyone’s active trading statuses.

- `/mystatus` — View your current trading status.

- `/help` — Show all available commands and info.

- ✅ Click the **Done** button on your status message to mark your session as finished.

---

supported_categories:
  - Indices
  - Commodities
  - Forex (Major)
  - Forex (Cross)
  - All

supported_timezones:
  - UTC
  - Asia/Kolkata
  - America/New_York
  - Europe/London
  - Asia/Tokyo
  - Australia/Sydney
  - Europe/Paris
  - America/Los_Angeles
  - Asia/Shanghai
  - America/Chicago


---

## Setup Instructions

1. Clone this repo: git clone: git clone https://github.com/Prasannaram2k4/marketpulse-bot.git
cd marketpulse-bot

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
