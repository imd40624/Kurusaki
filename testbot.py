import discord
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']


credentials=ServiceAccountCredentials.from_json_keyfile_name("Annie-e432eb58860b.json",scope)
gc= gspread.authorize(credentials)
wks=gc.open("Kurusaki_database_discord").sheet1


sp=wks.get_all_records()
#[{'Discord Name': 'Dong Cheng', 'ID': 185181025104560128, 'Points': 1}]

bot = commands.Bot(command_prefix='a.')

@bot.event
async def on_ready():
    """WHEN BOT IS READY, PRINT MESSAGE IN TERMINAL"""
    print ("I am running on " + bot.user.name)






@bot.event
async def on_message(message):
  try:
    msg=message.content
    if message.author.id in sp:
      await bot.say("Someone has messaged!")
    elif message.author.id not in sp:
      await bot.say("Author id is not in database yet, let's add it")
  except:
    await bot.say("looks like it didn't work")
    


bot.run('MzE3MDkyNzg4Mzc2NDM2NzM2.Ddsvww.ofp-IDE7rgMlsGRF243yCwbfoao')
