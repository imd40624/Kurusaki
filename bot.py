import discord
from discord.ext import commands
import asyncio
import json
import requests as rq
import os
from discord.utils import get,find
import apiai
import random
import msg_track
import time
import systems as sys
import events


bot_token = Enter your bot token here' #to host code on Github, change to bot_token=os.environ['BOT_TOKEN'] then add a config var called BOT_TOKEN and put your bot token as the value
loaded={'systems':False,'msg_track':False}

bot = commands.Bot(command_prefix='s.')  # SETUP BOT COMMAND PREFIX
bot.remove_command('help')

extensions=['events','msg_track','fun','tools']



async def get_saki_chans():
    for i in bot.servers:
        for x in i.channels:
            if x.type == discord.ChannelType.text and x.name == 'kurusaki_text_channel' and x.id not in events.saki_chans:
                events.saki_chans.append(x.id)



async def background_tasks():
    bot.loop.create_task(get_saki_chans())



@bot.event
async def on_ready():

    """WHEN BOT IS READY, PRINT MESSAGE IN TERMINAL"""
    bot.loop.create_task(background_tasks())
    print("I am running on " + bot.user.name)



async def help_in(msg):
    emb= discord.Embed(title=None, description='**Help command for Kurusaki**')
    emb.add_field(name='Help Server',value='https://discord.gg/jK9XXqT', inline=True)
    emb.add_field(name='Command Prefix', value='**s.**', inline=True)
    emb.set_thumbnail(url='https://raw.githubusercontent.com/CharmingMother/Kurusaki/master/img/kurusaki.png')
    emb.add_field(name='Tools', value='8 commands', inline=True)
    emb.add_field(name='Music', value='5 Music commands', inline=True)
    emb.add_field(name='Fun', value='19 Fun commands', inline=True)
    emb.add_field(
        name='Help', value='s.help\ns.help fun\ns.help tools\ns.help music')
    emb.set_footer(text='Created By: Dong Cheng#2945',
                icon_url='https://raw.githubusercontent.com/CharmingMother/Kurusaki/master/img/Dong%20Cheng.png')
    await bot.send_message(msg.channel,embed=emb)




async def api_agent(msg):
    meg=msg
    try:
        pack1=msg.content.replace('<@403402614454353941> ','')
        pack1=msg.content.replace('<@403402614454353941>','')
    except:
        pass
    ai = apiai.ApiAI('f5aec7a704d048bb86bb53ff6614d1bc')
    request = ai.text_request()
    request.query = pack1
    response = request.getresponse()
    api_msg = json.loads(response.read())
    pack = api_msg['result']['fulfillment']['speech']
    if '<!DOCTYPE HTM' in pack:
        pack = pack.replace(pack, '🌸')
    if '$discord_name' in pack:
        pack=pack.replace('$discord_name',meg.author.name)
    if '$yukinno love' in pack:
        pack=pack.replace('$yukinno love','')
    if '$name' in pack:
        pack=pack.replace('$name',meg.author.name)
    await bot.send_message(meg.channel, '{}'.format(pack))



    if msg.author.id == '461402952058273793':
        await bot.add_reaction(msg,emoji='🌺')
        await bot.add_reaction(msg, emoji='❤')
        await bot.add_reaction(msg, emoji='😝')

    await bot.process_commands(msg)



async def fun(con):
    msg = discord.Embed(title=None, description='**Fun commands for Kurusai**')
    msg.add_field(name='Name', value='s.dice <min> <max>\n\
    s.game <name>\n\
    s.watching <name>\n\
    s.listening <name>\n\
    s.catfact\n\
    s.dogfact\n\
    s.bunnyfact\n\
    s.pifact\n\
    s.randomanime\n\
    s.randommovie\n\
    s.randomshow\n\
    s.cat\n\
    s.cookie <@user>\n\
    s.neko or s.neko nsfw\n\
    s.dog\n\
    s.bunny\n\
    s.tts <message>\n\
    s.say <message>\n\
    s.worldchat\n\
    s.timer <time>', inline=True)
    msg.add_field(name='Command Usage', value='Role random number from <min> <max>\n\
    Changes game playing status of bot\n\
    Changes watching status of bot\n\
    Changes Listening status of bot\n\
    Get random cat fact\n\
    Get a random dog fact\n\
    Get a random bunny fact\n\
    Get a random pi(3.14) fact\n\
    Get random anime\n\
    Get random movie\n\
    Get random show\n\
    Get a picture of random cat\n\
    Give random amount of cookie to mentioned user\n\
    Random Neko girl picture\n\
    Random bunny picture\n\
    Get random dog picture\n\
    Use text to speech on bot\n\
    Make the bot say what you want\n\
    Creates a text channel that connects to other servers\n\
    Creates a countdown timer', inline=True)
    await bot.send_message(con.message.channel, embed=msg)

async def tools(con):
    msg = discord.Embed(
        title=None, description='**Tools for Kurusaki**', inline=False)
    msg.add_field(name='Command name', value='s.urban <word>\n\
    s.define <word>\n\
    s.invite\n\
    s.node <your notes>\n\
    s.notes\n\
    s.weather <city>\n\
    s.pin <message>\n\
    s.info <@user>\n\
    s.channel <type> <name>\n\
    s.del_channel <name>')
    msg.add_field(name='Command Usage', value='Use urban dictionary to defien word\n\
    Define word from dictionary\n\
    Creates an invite link to invite Kurusaki\n\
    Adds your notes\n\
    Returns the notes you\'ve written\n\
    Get the weather of your city\n\
    Pins a message\n\
    Gets info of mentioned user\n\
    Creates a channel in your server\n\
    Deletes a channel')
    await bot.send_message(con.message.channel, embed=msg)


@bot.command(pass_context=True)
async def help(con, *, msg=None):
    commands = ['fun', 'tools']
    if msg not in commands:
        msg = discord.Embed(
            title=None, description='**Help command for Kurusaki**')
        msg.add_field(name='Help Server',
                      value='https://discord.gg/jK9XXqT', inline=True)
        msg.add_field(name='Command Prefix', value='**s.**', inline=True)
        msg.set_thumbnail(
            url='https://raw.githubusercontent.com/CharmingMother/Kurusaki/master/img/kurusaki.png')
        msg.add_field(name='Tools', value='8 commands', inline=True)
        msg.add_field(name='Fun', value='19 Fun commands', inline=True)
        msg.add_field(
            name='Help', value='s.help\ns.help fun\ns.help tools\ns.help music')
        msg.set_footer(text='Created By: Dong Cheng#2945',
                       icon_url='https://raw.githubusercontent.com/CharmingMother/Kurusaki/master/img/Dong%20Cheng.png')
        await bot.send_message(con.message.channel,embed=msg)
    if msg == 'fun':
        bot.loop.create_task(fun(con))

    if msg == 'tools':
        bot.loop.create_task(tools(con))



if __name__ == "__main__":
    for extension in extensions:
        # try:
        bot.load_extension(extension)
        print("{} loaded".format(extension))
        # except Exception as error:
            # print("Unable to load extension {} error {}".format(extension, error))

    bot.run(bot_token)
