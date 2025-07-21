import discord
from discord.ext import commands, tasks
import json
import asyncio
from datetime import datetimea
import os
import re

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# File to store birthday data
BIRTHDAYS_FILE = 'birthdays.json'

# Load existing birthdays or create empty dict
def load_birthdays():
    if os.path.exists(BIRTHDAYS_FILE):
        try:
            with open(BIRTHDAYS_FILE, 'r') as f:
                return json.load(f)
        except:
            print("Error loading birthdays file, starting fresh")
            return {}
    return {}

# Save birthdays to file
def save_birthdays(birthdays):
    with open(BIRTHDAYS_FILE, 'w') as f:
        json.dump(birthdays, f, indent=2)

# Load birthdays on startup
birthdays = load_birthdays()

# Validate date format (MM/DD or MM-DD)
def is_valid_date(date_string):
    pattern = r'^(0?[1-9]|1[0-2])[\/\-](0?[1-9]|[12][0-9]|3[01])$'
    return re.match(pattern, date_string) is not None

# Format date consistently
def format_date(date_string):
    return date_string.replace('-', '/')

# Get today's date in MM/DD format
def get_today_date():
    today = datetime.now()
    return f"{today.month}/{today.day}"

@bot.event
async def on_ready():
    print(f'🎉 Birthday Bot is ready! Logged in as {bot.user}')
    # Sync slash commands
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

    # Start birthday checking task
    if not check_birthdays_daily.is_running():
        check_birthdays_daily.start()

# Set birthday command
@bot.tree.command(name="setbirthday", description="Set your birthday (MM/DD format)")
async def set_birthday(interaction: discord.Interaction, date: str):
    if not is_valid_date(date):
        await interaction.response.send_message(
            "❌ Invalid date format! Please use MM/DD format (e.g., 12/25 or 3/15)",
            ephemeral=True
        )
        return

    formatted_date = format_date(date)
    user_id = str(interaction.user.id)

    birthdays[user_id] = {
        'date': formatted_date,
        'username': interaction.user.display_name
    }

    save_birthdays(birthdays)

    await interaction.response.send_message(
        f"🎂 Birthday saved! I'll wish you a happy birthday on {formatted_date}!",
        ephemeral=True
    )

# Check birthday command
@bot.tree.command(name="mybirthday", description="Check your saved birthday")
async def my_birthday(interaction: discord.Interaction):
    user_id = str(interaction.user.id)

    if user_id in birthdays:
        await interaction.response.send_message(
            f"🎂 Your birthday is set to: {birthdays[user_id]['date']}",
            ephemeral=True
        )
    else:
        await interaction.response.send_message(
            "❌ You haven't set your birthday yet! Use `/setbirthday` to set it.",
            ephemeral=True
        )

# Remove birthday command
@bot.tree.command(name="removebirthday", description="Remove your birthday from the bot")
async def remove_birthday(interaction: discord.Interaction):
    user_id = str(interaction.user.id)

    if user_id in birthdays:
        del birthdays[user_id]
        save_birthdays(birthdays)
        await interaction.response.send_message(
            "✅ Your birthday has been removed from the bot.",
            ephemeral=True
        )
    else:
        await interaction.response.send_message(
            "❌ You don't have a birthday set.",
            ephemeral=True
        )

# Daily birthday check task
@tasks.loop(hours=1)  # Check every hour in case bot was offline at midnight
async def check_birthdays_daily():
    today = get_today_date()
    print(f"Checking birthdays for {today}...")

    for user_id, user_data in birthdays.items():
        if user_data['date'] == today:
            await send_birthday_message(user_id, user_data['username'])

# Get historical fact for a date
async def get_historical_fact(date_str):
    try:
        # Convert MM/DD to month name and day for API
        month, day = date_str.split('/')
        month_names = ['', 'January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December']
        month_name = month_names[int(month)]

        import aiohttp
        async with aiohttp.ClientSession() as session:
            url = f"http://numbersapi.com/{month}/{day}/date"
            async with session.get(url) as response:
                if response.status == 200:
                    fact = await response.text()
                    return fact
                else:
                    return f"On {month_name} {day}, history was made - just like today with your birthday!"
    except Exception as e:
        print(f"Error fetching historical fact: {e}")
        return "Today is a special day in history - it's your birthday! 🎂"

# Send birthday DM
async def send_birthday_message(user_id, username):
    try:
        user = bot.get_user(int(user_id))
        if user is None:
            user = await bot.fetch_user(int(user_id))

        # Get historical fact for their birthday
        user_data = birthdays[str(user_id)]
        historical_fact = await get_historical_fact(user_data['date'])

        # Create birthday embed
        embed = discord.Embed(
            title="🎉 Happy Birthday! 🎂",
            description=f"Happy Birthday, {username}! 🎈\n\nHope you have a wonderful day filled with joy, laughter, and cake! 🍰",
            color=discord.Color.from_rgb(255, 105, 180)  # Hot pink
        )

        # Add historical fact field
        embed.add_field(
            name="📚 Fun Historical Fact",
            value=f"*{historical_fact}*",
            inline=False
        )

        embed.set_footer(text="Birthday wishes from your friendly Discord bot! 💕")
        embed.timestamp = datetime.now()

        await user.send(embed=embed)
        print(f"🎂 Birthday message sent to {username}!")

    except Exception as e:
        print(f"Failed to send birthday message to user {user_id}: {e}")

# Error handling
@bot.event
async def on_command_error(ctx, error):
    print(f"Command error: {error}")

# Run the bot
if __name__ == "__main__":
    import os
    # Get bot token from Replit secrets
    bot.run(os.getenv('_BOT_TOKEN'))
