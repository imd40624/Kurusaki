import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os





bot_token=os.environ[BOT_TOKEN]
bot =commands.Bot(command_prefix='v')

@bot.event
async def on_ready():
  print("Bot {} is ready to run".format(bot.user.name))



bot.run(bot_token)
