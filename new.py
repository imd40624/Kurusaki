import asyncio
import random
import time
import apiai
import discord
import requests as rq
from discord.ext import commands
from discord.utils import *
import random
import urllib
import bs4 as bs
import requests 
import youtube_dl
import json
import aiohttp as srq
from requests import Session
from requests_threads import AsyncSession
import trello
import discord.ext
key = '6615aae3f4caa1b02ffeb6e97b0b0786'
token = 'bd06c326915a2c6d8a64e78fa39aee53a0815b259fb0d270a60817e4661a8bf1'
client = trello.TrelloClient(api_key=key, api_secret=token)
bot=commands.Bot(command_prefix='a.')
server_dict={}
server_list=[]
server_id_dict={}
member_greeter=[]
member_greeter_dict={}
class Trello():
    class Logger():
        logger = client.list_boards()[2]
        types = logger.open_lists()
        greeter = types[0]
        cards=greeter.list_cards()
    class Couple():
        pass
    class Notes():
        pass
@bot.event
async def on_member_join(user:discord.Member):
    target=get(bot.get_all_channels(),server__id=user.server.id,id=member_greeter_dict[user.server.id])
    await bot.send_message(target,'**{} has joined the server**'.format(user.name))
async def greet_checker():
    while True:
        await asyncio.sleep(1)
        card_looper=0
        for i in range(len(Trello.Logger.cards)):
            if Trello.Logger.cards[card_looper].name not in member_greeter_dict:
                server_comment=Trello.Logger.cards[card_looper].get_comments()
                server_id= server_comment[0]['data']['text']
                member_greeter_dict[server_id]=Trello.Logger.cards[card_looper].name
            if Trello.Logger.cards[card_looper].name in member_greeter:
                pass
@bot.event
async def on_ready():
    print("I am running {}".format(bot.user.name))
    for i in bot.servers:
        server_dict[i.name]=i
        server_list.append(i)
        server_id_dict[i.id]=i
    chan = get(bot.get_all_channels(),server__id='295717368129257472', id='433654104435458049')
    print(chan)
@bot.command(pass_context=True)
async def greet(msg,*,channel):
    chan=find(lambda m:m.name == channel,msg.message.server.channels)
    if chan == None:
        await bot.send_message(msg.message.channel,"**Channel is not found**")
    if chan != None:
        if chan.type == discord.ChannelType.text:
            ac=Trello.Logger.greeter.add_card(chan.id).comment(chan.server.id)
            member_greeter_dict[msg.message.server.id]=chan.id
            await bot.send_message(msg.message.channel,"**Greetings message set to {}**".format(chan.mention))
        if chan.type != discord.ChannelType.text:
            await bot.send_message(msg.message.channel,"**Is not a text channel**")
bot.run('MzE3MDkyNzg4Mzc2NDM2NzM2.DhGETg.AWbbjLie0fGWY1gsWc9oPe510qE')
# # bot.run('NDAzNDAyNjE0NDU0MzUzOTQx.DeCrDw.zyBWdRkVggjETQraJhGTgTHRWuo')
