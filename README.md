# 🎂 Discord Birthday Bot

A friendly Discord bot that remembers everyone's birthdays and sends them personalized birthday messages with historical facts about their special day!

## ✨ Features

- **Set Birthdays**: Users can register their birthdays using simple slash commands
- **Automatic Birthday Messages**: Bot sends personalized DMs on users' birthdays
- **Historical Facts**: Each birthday message includes a fun historical fact about that date
- **Data Persistence**: Birthdays are saved and remembered even after bot restarts
- **24/7 Monitoring**: Checks for birthdays every hour to never miss anyone

## 🤖 Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/setbirthday` | Set your birthday (MM/DD format) | `/setbirthday 12/25` |
| `/mybirthday` | Check your saved birthday | `/mybirthday` |
| `/removebirthday` | Remove your birthday from the bot | `/removebirthday` |

## 🚀 Quick Setup

### Prerequisites
- Python 3.7+
- A Discord account and server
- A Discord bot token

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/discord-birthday-bot.git
   cd discord-birthday-bot
   ```

2. **Install dependencies**
   ```bash
   pip install discord.py aiohttp
   ```

3. **Create your Discord bot**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications/)
   - Create a new application and bot
   - Copy the bot token
   - Enable necessary permissions (Send Messages, Use Slash Commands)

4. **Set up environment variable**
   ```bash
   export BOT_TOKEN=your_bot_token_here
   ```
   Or create a `.env` file with:
   ```
   BOT_TOKEN=your_bot_token_here
   ```

5. **Run the bot**
   ```bash
   python bot.py
   ```

## 🌐 Deploy to Replit (24/7 Hosting)

1. Fork this repository
2. Import to [Replit](https://replit.com) as a Python project
3. In Replit Secrets (🔒), add:
   - Key: `BOT_TOKEN`
   - Value: Your Discord bot token
4. Click Run!

## 📝 Bot Setup in Discord

### Invite Bot to Server
1. Go to Discord Developer Portal → OAuth2 → URL Generator
2. Select scopes: `bot` and `applications.commands`
3. Select permissions: `Send Messages` and `Use Slash Commands`
4. Use the generated URL to invite your bot

### Enable Privileged Intents (if needed)
1. Go to Bot tab in Developer Portal
2. Enable "Message Content Intent" under Privileged Gateway Intents
3. Save changes

## 📁 File Structure

```
discord-birthday-bot/
├── bot.py              # Main bot code
├── birthdays.json      # Auto-generated birthday storage
├── README.md          # This file
└── requirements.txt   # Python dependencies
```

## 🎉 How It Works

1. **Users register** their birthdays using `/setbirthday MM/DD`
2. **Bot stores** birthday data in `birthdays.json`
3. **Every hour**, bot checks if it's anyone's birthday
4. **On birthdays**, bot sends a personalized DM with:
   - Birthday wishes and emojis
   - A historical fact about that date
   - Beautiful embedded message format

## 🔧 Customization

### Modify Birthday Message
Edit the `send_birthday_message()` function in `bot.py` to customize:
- Message text and emojis
- Embed colors and formatting
- Additional fields or information

### Change Check Frequency
Modify the `@tasks.loop(hours=1)` decorator to change how often the bot checks for birthdays.

### Add More Commands
Extend the bot by adding new slash commands following the existing pattern.

## 🛠️ Dependencies

- [discord.py](https://pypi.org/project/discord.py/) - Discord API wrapper
- [aiohttp](https://pypi.org/project/aiohttp/) - HTTP client for fetching historical facts

## 📊 API Used

- [Numbers API](http://numbersapi.com/) - Provides historical facts for dates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues:
1. Check that your bot token is correct
2. Ensure the bot has proper permissions in your Discord server
3. Verify all dependencies are installed
4. Check the console for error messages

## 🎈 Example Birthday Message

```
🎉 Happy Birthday! 🎂

Happy Birthday, John! 🎈

Hope you have a wonderful day filled with joy, laughter, and cake! 🍰

📚 Fun Historical Fact
March 15 is the day in 44 BC that Julius Caesar was assassinated.

Birthday wishes from your friendly Discord bot! 💕
```

---

Made with ❤️ for celebrating birthdays in Discord servers!
