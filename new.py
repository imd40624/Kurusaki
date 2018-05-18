import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio





bot_token=os.environ['NDAzNDAyNjE0NDU0MzUzOTQx.DeCrDw.zyBWdRkVggjETQraJhGTgTHRWuo']
bot =commands.Bot(command_prefix='v')

@bot.event
async def on_ready():
  print("Bot {} is ready to run".format(bot.user.name))



bot.run(bot_token)
