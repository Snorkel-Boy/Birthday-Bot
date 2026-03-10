Discord Birthday Bot
This bot tracks user birthdays and sends a DM with a historical fact on their day.

Core Functionality
Registration: Users save their birthday via /setbirthday MM/DD.

Automation: The bot runs a background task every hour to check for matches.

Data: Dates are stored in a local birthdays.json file.

Facts: Historical data is fetched from the Numbers API.

Setup
Install: pip install discord.py aiohttp

Configure: Get a bot token from the Discord Developer Portal.

Intents: Enable Message Content Intent in the developer settings.

Run: Set your BOT_TOKEN as an environment variable and execute python bot.py.

Commands
/setbirthday: Save your date.

/mybirthday: View your saved date.

/removebirthday: Delete your data.

Deployment
For 24/7 uptime, host on a VPS or Replit. On Replit, use the Secrets tool to store your token.

Prob the most unnecessary bot ever
