from discord.ext import commands
import discord
import os
from keep_alive import keep_alive
from discord import ChannelType

intents = discord.Intents.default()

intents.members = True

bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():
	print("The bot is online!")
	bot.load_extension("cogs.queue")

keep_alive()
bot.run(os.environ.get("TOKEN"))