import discord
from discord.ext import commands, tasks
from discord import app_commands, Interaction
import datetime
import asyncio
import os
import pytz

FOREX_SESSIONS = {
    "Sydney": (22, 7),
    "Tokyo": (0, 9),
    "London": (7, 16),
    "New York": (12, 21)
}

CATEGORIES = [
    "Indices",
    "Commodities",
    "Forex (Major)",
    "Forex (Cross)",
    "All"
]

TIMEZONES = [
    "UTC",
    "Asia/Kolkata",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "Europe/Paris",
    "America/Los_Angeles",
    "Asia/Shanghai",
    "America/Chicago",
]

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

user_statuses = {}

def get_current_session(tz_name: str):
    try:
        timezone = pytz.timezone(tz_name)
    except Exception:
        timezone = pytz.utc

    now = datetime.datetime.now(timezone).time()
    hour = now.hour
    for session, (start, end) in FOREX_SESSIONS.items():
        if start > end:  # overnight session
            if hour >= start or hour < end:
                return session
        else:
            if start <= hour < end:
                return session
    return "Unknown"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    check_expired.start()
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@tasks.loop(minutes=10)
async def check_expired():
    now = datetime.datetime.utcnow()
    expired = [user_id for user_id, (_, _, _, expiry) in user_statuses.items() if expiry <= now]
    for user_id in expired:
        del user_statuses[user_id]
        user = bot.get_user(user_id)
        if user:
            try:
                await user.send("Your trading status expired after 12 hours.")
            except:
                pass

@bot.tree.command(name="setstatus", description="Set your trading status")
@app_commands.describe(category="Choose your category", timezone="Select your timezone")
@app_commands.choices(category=[app_commands.Choice(name=c, value=c) for c in CATEGORIES])
async def setstatus(interaction: Interaction, category: app_commands.Choice[str], timezone: str = "UTC"):
    if timezone not in TIMEZONES:
        await interaction.response.send_message(f"Invalid timezone. Choose from: {', '.join(TIMEZONES)}", ephemeral=True)
        return

    session = get_current_session(timezone)
    expiry = datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    user_statuses[interaction.user.id] = (category.value, session, timezone, expiry)

    msg = f"{interaction.user.mention} is analyzing **{category.value}** during **{session}** session (timezone: {timezone})."
    channel = discord.utils.get(interaction.guild.text_channels, name="status")
    if not channel:
        channel = interaction.channel
    await channel.send(msg)

    try:
        await interaction.user.send(f"Your status is set: {category.value} during {session} session (timezone: {timezone}).")
    except:
        pass

    view = DoneButtonView(interaction.user.id)
    await interaction.response.send_message("Status set! Click the ✅ Done button when finished.", view=view, ephemeral=True)

@bot.tree.command(name="done", description="Mark trading as done")
async def done(interaction: Interaction):
    if interaction.user.id not in user_statuses:
        await interaction.response.send_message("You don't have an active status.", ephemeral=True)
        return
    del user_statuses[interaction.user.id]

    msg = f"{interaction.user.mention} has finished analyzing."
    channel = discord.utils.get(interaction.guild.text_channels, name="status")
    if not channel:
        channel = interaction.channel
    await channel.send(msg)

    try:
        await interaction.user.send("You have marked your session as done.")
    except:
        pass

    await interaction.response.send_message("Status cleared.", ephemeral=True)

@bot.tree.command(name="status", description="View everyone's active trading statuses")
async def status(interaction: Interaction):
    if not user_statuses:
        await interaction.response.send_message("No active trading statuses right now.", ephemeral=True)
        return

    lines = []
    for user_id, (category, session, timezone, expiry) in user_statuses.items():
        user = bot.get_user(user_id)
        if user:
            expires_in = expiry - datetime.datetime.utcnow()
            minutes_left = int(expires_in.total_seconds() // 60)
            lines.append(f"**{user.display_name}**: {category} | Session: {session} | TZ: {timezone} | Expires in {minutes_left} min")

    if not lines:
        await interaction.response.send_message("No active trading statuses right now.", ephemeral=True)
        return

    await interaction.response.send_message("\n".join(lines), ephemeral=True)

@bot.tree.command(name="mystatus", description="View your current trading status")
async def mystatus(interaction: Interaction):
    data = user_statuses.get(interaction.user.id)
    if not data:
        await interaction.response.send_message("You don't have an active status.", ephemeral=True)
        return

    category, session, timezone, expiry = data
    expires_in = expiry - datetime.datetime.utcnow()
    minutes_left = int(expires_in.total_seconds() // 60)

    msg = (f"Your status:\nCategory: {category}\nSession: {session}\nTimezone: {timezone}\nExpires in: {minutes_left} minutes")
    await interaction.response.send_message(msg, ephemeral=True)

@bot.tree.command(name="help", description="Get bot usage instructions")
async def help_cmd(interaction: Interaction):
    help_text = (
        "**Trading Status Bot Commands:**\n"
        "/setstatus category timezone - Set your trading status\n"
        "/done - Mark your trading session as done\n"
        "/status - View everyone's active trading statuses\n"
        "/mystatus - View your current trading status\n"
        "/help - Show this message\n\n"
        "Supported categories: " + ", ".join(CATEGORIES) + "\n"
        "Supported timezones: " + ", ".join(TIMEZONES)
    )
    await interaction.response.send_message(help_text, ephemeral=True)

class DoneButtonView(discord.ui.View):
    def __init__(self, user_id):
        super().__init__(timeout=None)
        self.user_id = user_id

    @discord.ui.button(label="✅ Done", style=discord.ButtonStyle.green)
    async def done_button(self, interaction: Interaction, button: discord.ui.Button):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("This button is not for you.", ephemeral=True)
            return
        if self.user_id not in user_statuses:
            await interaction.response.send_message("You don't have an active status.", ephemeral=True)
            return
        del user_statuses[self.user_id]

        msg = f"{interaction.user.mention} has finished analyzing."
        channel = discord.utils.get(interaction.guild.text_channels, name="status")
        if not channel:
            channel = interaction.channel
        await channel.send(msg)

        try:
            await interaction.user.send("You have marked your session as done.")
        except:
            pass

        await interaction.response.send_message("Status cleared.", ephemeral=True)

bot.run(os.getenv("DISCORD_TOKEN"))
