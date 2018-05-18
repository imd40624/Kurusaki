import discord
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import Pymoe
import simplejson as json
import datetime
import requests as rq
from champs import champs
import os
import apiai
import image_links
import random
import time
# 
import tools
import bs4 as bs
import urllib
import urllib.request
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials


# api = os.environ["RIOT_KEY"]
# wu_key = os.environ['WU_API']
# owm = os.environ['open_weather']
# img_api = os.environ['img_api']
# apiai_token = os.environ['api_ai']
bot_token = os.environ['BOT_TOKEN']
# An = Pymoe.Anilist()

bot = commands.Bot(command_prefix='s.')


@bot.event
async def on_ready():
    """WHEN BOT IS READY, PRINT MESSAGE IN TERMINAL"""
    print("I am running on " + bot.user.name)


bot.run(bot_token)
