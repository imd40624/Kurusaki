import discord
import asyncio
import time
import json
import requests as rq
from discord.ext import commands
from discord.ext.commands immport Bot
import bot



mention = bot.bot.user.mention
    if message.content.startswith(mention):
        anime = rq.get('https://kurusaki-webhook.herokuapp.com/').text
        raw_msg = message.content.split("{}".format(mention))
        msg = "".join(raw_msg[1:])
        ai = apiai.ApiAI(apiai_token)
        request = ai.text_request()
        request.lang = 'en'
        request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
        request.query = msg
        response = request.getresponse()
        rope = str(response.read())
        rope = rope[rope.index("speech") + 10:]
        rope = rope[0:rope.index("\"")]
        if '$anime' in rope:
            anime = rope.replace('$anime', anime)
            await bot.bot.send_message(message.channel, anime)
        elif 'anime' not in rope:
            await bot.bot.send_message(message.channel, rope)
        if "$time" in rope:
            await bot.bot.say(datetime.datetime.now())
        if '$yukinno' in rope:
            author_id = message.author.id
            if author_id == 287369884940238849:
                love = ['I love you Yukinno',
                        'Yukkino, I love you!', 'I love you!', '<3']
                ran_love = random.choice(love)
                yukinno_love = rope.replace(rope, ran_love)
                await bot.bot.send_message(message.channel, yukinno_love)
            elif message.author.id != 287369884940238849:
                await bot.bot.send_message(message.channel, rope)
