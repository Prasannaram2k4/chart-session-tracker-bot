echo "# Chart Session Tracker Bot 📈

A Discord bot to help traders share their current market analysis status live in a server.

---

## Features

- Set your trading category (Indices, Commodities, Forex Majors/Crosses, All).
- Automatically detects Forex trading sessions based on your timezone.
- Announce your current status in a #status channel.
- Mark yourself done via command or button.
- Status auto-expires after 12 hours to keep things clean.

---

## Commands

- \`/setstatus category timezone\` — Start sharing your trading session.
- \`/done\` — Mark your trading session as finished.
- ✅ Interactive **Done** button to clear your status.

---

## Setup Instructions

1. Clone this repo:

\`\`\`bash
git clone https://github.com/Prasannaram2k4/chart-session-tracker-bot.git
cd chart-session-tracker-bot
\`\`\`

2. Create a Discord bot on [Discord Developer Portal](https://discord.com/developers/applications) and get your token.

3. Enable Privileged Gateway Intents on the bot page:

   - Presence Intent  
   - Server Members Intent  
   - Message Content Intent

4. Create a \`.env\` file in the project root with your bot token:

\`\`\`
DISCORD_TOKEN=your_bot_token_here
\`\`\`

5. Install dependencies:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

6. Run the bot:

\`\`\`bash
python main.py
\`\`\`

---

## Usage

- Use \`/setstatus\` to start sharing your market analysis session.
- Use \`/done\` when you finish.
- Your status will be posted in #status channel automatically.

---

## Contributing

Contributions are welcome! Feel free to fork and send pull requests.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by Prasannaram2k4
" > README.md
