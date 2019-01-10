import discord
from discord.utils import find,get
from discord.ext import commands
import asyncio
import random
import requests as rq
import json
import time
import events

img_api = 'f4237223-a9fc-4a7a-b789-e7d2beebcbef' # you can use your own api or use mine 
owm = 'e3d03bf7f7df7af0bbcc77784637a3dd' # you can use your own api or use mine (Open Weather API)
tc = []

class Tools:
    def __init__(self,bot):
        self.bot=bot

    





    @commands.command(pass_context=True)
    @commands.cooldown(rate=5, per=3.0, type=commands.BucketType.user)
    async def define(self,con, *, msg):
        try:
            session = rq.Session()
            app_key = '8e336d43889c9e541af389c81d44258d'
            url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/en/{}'.format(
                msg)
            headers = {"app_id": '3959fee6', 'app_key': app_key}
            raw = session.get(url, headers=headers).text
            if "<!DOCTYPE HTML" in raw:
                await self.bot.send_message(con.message.channel,"**No Results Found**")
            elif "<!DOCTYPE HTML" not in raw:
                word = json.loads(raw)
                name = word['results'][0]['id']
                definition = word['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
                try:
                    etymologies = word['results'][0]['lexicalEntries'][0]['entries'][0]['etymologies'][0]
                    await self.bot.send_message(con.message.channel,"**Word**: {}\n**Etymologies**: {}\n**Definition**: {}".format(name, etymologies, definition))
                except:
                    await self.bot.send_message(con.message.channel,"**Word**: {}\n**Definition**: {}".format(name, definition))
        except:
            await self.bot.send_message(con.message.channel,"**Something went wrong**")



    @commands.command(pass_context=True)
    async def invite(self,con):
        """GET AN INVITE LINK FOR THIS DISCORD BOT. EX: s.invite"""
        msg = discord.Embed(title="Kurusaki.gl", url='https://goo.gl/kYiEhu',
                            description='Invite link for Kurusaki bot')
        await self.bot.send_message(con.message.channel, embed=msg)



    @commands.command(pass_context=True)
    async def weather(self,con):
        session = rq.Session()
        """GET THE WEATHER IN YOUR CITY. EX: s.weather austin"""
        city_state = con.message.content[10:]
        t = u"\u00b0"
        try:
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'.format(
                city_state, owm)
            ser = session.get(url).text
            rq_json = json.loads(ser)
            temp = rq_json['main']['temp']
            max_temp = rq_json['main']['temp_max']
            min_temp = rq_json['main']['temp_min']
            dis = rq_json['weather'][0]['description']
            wind = rq_json['wind']['speed']
            await self.bot.send_message(con.message.channel, "**Temperature** **in** **{}** **is around** {}{}F\n**Minimum Temperature is**: {}{}F\n**Maximum Temperature is**: {}{}F\n**Mainly**: {}\n**Wind speed is around**: {} **MPH**".format(city_state, temp, t, min_temp, t, max_temp, t, dis, wind))
        except:
            await self.bot.send_message(con.message.channel, "Looks like something went wrong. Your spelling may be incorrect or the bot may just be able to process this command at the moment.")


    @commands.command(pass_context=True)
    async def pin(self,con, *, msg):
        await self.bot.pin_message(msg)


    @commands.command(pass_context=True)
    async def urban(self,con, *, msg):
        session = rq.Session()
        """USES URBAN DICT TO FIND DEFINITION OF WORDS. EX: s.urban neko"""
        link = 'http://api.urbandictionary.com/v0/define?term={}'.format(msg)
        rq_link = session.get(link).text
        rq_json = json.loads(rq_link)
        if rq_json['list'] == []:
            await self.bot.send_message(con.message.channel, "**No Results Found**")
        elif rq_json['list'] != []:
            await self.bot.send_message(con.message.channel, "**Word**: {}\n**Votes**: {}\n**Definitioin**: {}\n**Example**: {}".format(rq_json['list'][0]['word'], rq_json['list'][0]['thumbs_up'], rq_json['list'][0]['definition'], rq_json['list'][0]['example']))


    @commands.command(pass_context=True)
    async def del_channel(self,con, *, name):
        chan = find(lambda m: m.name == name, con.message.server.channels)
        await self.bot.delete_channel(chan)
        await self.bot.send_message(con.message.channel, "Channel {} has been deleted".format(name))






    async def timer_bg(self,con, time1):
        timer = time1
        ct = con.message.channel.id
        if ct in tc:
            await self.bot.send_message(con.message.channel, "Please wait for the current timer to complete.")
        elif ct not in tc:
            msg = await self.bot.send_message(con.message.channel, time1)
            tc.append(con.message.channel.id)
            for i in range(time1):
                await asyncio.sleep(1)
                timer -= 1
                await self.bot.edit_message(msg, new_content=timer)
            num = tc.index(ct)
            del tc[num]
            await self.bot.send_message(con.message.channel, "{} seconds timer complete in the channel!".format(time))


    @commands.command(pass_context=True)
    async def timer(self,con, time1=10):
        self.bot.loop.create_task(self.timer_bg(con, time1))


    @commands.command(pass_context=True)
    async def ping(self,con):
        channel = con.message.channel
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        embed = discord.Embed(title=None, description='Ping: {}'.format(
            round((t2-t1)*1000)), color=0x2874A6)
        await self.bot.send_message(con.message.channel, embed=embed)


    @commands.command(pass_context=True)
    async def channel(self,con, tpe, *, name):
        if tpe == 'text':
            tpe = discord.ChannelType.text
            if ' ' in name:
                name.replace(' ', '-')
            if '?' in name:
                name.replace('?', '')
                c_type = 'text'
        if tpe == 'voice':
            c_type = 'voice'
            tpe = discord.ChannelType.voice
        await self.bot.create_channel(con.message.server, name, type=tpe)
        await self.bot.send_message(con.message.channel, "**{}** channel **{}** created".format(c_type, name))


    @commands.command(pass_context=True)
    async def worldchat(self,info):
        try:
            chan = find(lambda m: m.name == 'kurusaki_text_channel',
                        info.message.server.channels)
            if chan == None:
                await self.bot.create_channel(info.message.server, 'kurusaki_text_channel', type=discord.ChannelType.text)
                await self.bot.reply("A text channel has been created that can chat with other {} servers".format(len(events.saki_chans)))
            elif chan != None:
                await self.bot.send_message(info.message.channel, "There is already a channel created for worldchat")
        except:
            pass


    @commands.command(pass_context=True)
    async def dice(self,con, min1=1, max1=6):
        """GENERATES A RANDOM BETWEEN 1-6"""
        r = random.randint(min1, max1)
        await self.bot.send_message(con.message.channel, "**{}**".format(r))




    @commands.command(pass_context=True)
    async def img(self,con):
        session = rq.Session()
        """FAILED IMAGE GENERATOR BY KEYWORDS s.img dog"""
        query = con.message.content[5:]
        url = 'http://version1.api.memegenerator.net//Generators_Search?q={}&apiKey={}'.format(
            query, img_api)
        rq_link = session.get(url).text
        rq_json = json.loads(rq_link)
        await self.bot.send_message(con.message.channel, rq_json['result'][0]['imageUrl'])






def setup(bot):
    bot.add_cog(Tools(bot))

