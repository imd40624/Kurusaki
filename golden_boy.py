import discord
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import Pymoe
import simplejson as json
import requests as rq
from champs import champs
import os








# api = os.environ['API_KEY']








An=Pymoe.Anilist()

bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    """WHEN BOT IS READY, PRINT MESSAGE IN TERMINAL"""
    print ("I am running on " + bot.user.name)
    await bot.change_presence(game=discord.Game(name='Discord.gg'))

@bot.command(pass_context=True)
async def ping(ctx):
    """PINGS THE BOT"""
    await bot.say(":ping_pong: ping!!")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    """GETS THE BASIC INFORMATION OF A USER IN DISCORD"""
    await bot.say("The user's name is: {}\n{}'s ID is: {}\n{} is: {}\n{}'s highest role is: {}\n{} joined at: {}".format(user.name,user.name,user.id,user.name,user.status,user.name,user.top_role,user.name,user.joined_at))





@bot.command(pass_context=True)
async def anime(ctx):
    """SEARCHES FOR AN ANIME THAT THE USER INPUTS FROM DISCORD USING ~ANIME (ANIME NAME)"""
    try:
        title=ctx.message.content.split("~anime ")
        new_msg = " ".join(title[1:])
        search = An.search.anime(new_msg)
        episodes = search['data']['Page']['media'][0]['episodes']
        episodes_dumps=json.dumps(episodes)
        if episodes_dumps == "null":
            episodes = "Currently airing or unknown"
        else:
            episodes = episodes
        name = search['data']['Page']['media'][0]['title']['romaji']
        rank = search['data']['Page']['media'][0]['popularity']
        score = search['data']['Page']['media'][0]['averageScore']
        img = search['data']['Page']['media'][0]['coverImage']['large']
        season = search['data']['Page']['media'][0]['season']
        an=Pymoe.Anilist()
        ide=search['data']['Page']['media'][0]['id']
        a=an.get.anime(ide)
        b=json.dumps(a)
        c=json.loads(b)
        d = c['data']['Media']['description']
        e = d.replace("<br><br>","")
        await bot.say("Anime Name: {}\nEpisodes: {}\nRank: {}\nAverage Score: {}%\nSeason: {}\nSummary: {}\n{}".format(name,episodes,rank,score,season,e,img))

    except IndexError:
        print("")
    finally:
        #if anime is not found output not found
        not_found=json.dumps(search)
        not_json=json.loads(not_found)
        if not_json['data']['Page']['pageInfo']['lastPage'] ==0:
            await bot.say("Anime {} is not found.".format(new_msg))




@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    """KICKS USER THAT IS TAGGED"""
    await bot.say(":boot: Bye bye, {}.".format(user.name))
    await bot.kick(user)





# @bot.command(pass_context=True)
# async def summoner(ctx):
#     raw_name = ctx.message.content.split("~summoner ")
#     name = " ".join(raw_name[1:])
#     """GETS THE SUMMONER'S BASIC INFORMATION; NAME,LEVEL"""
#     link = rq.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name, api)).text
#     rq_json = json.loads(link)
#     await bot.say("{}is level: {}\n{}'s profile icon is: {}".format(rq_json['name'],rq_json['summonerLevel'],rq_json['name'],rq_json['profileIconId']))


# @bot.command(pass_context=True)
# async def lore(ctx):
#     """GETS THE LORE OF A CHAMPION GIVEN"""
#     champ_name = ctx.message.content.split("~lore ")
#     new_msg = " ".join(champ_name[1:]).lower()
#     champ = rq.get('https://na1.api.riotgames.com/lol/static-data/v3/champions/{}?locale=en_US&champData=lore&api_key={}'.format(champs['keys'][new_msg],api)).text
#     champ_json=json.loads(champ)
#     await bot.say("Champion Name: {}\nTitle: {}\nLore: {}".format(champ_json['name'],champ_json['title'],champ_json['lore']))



# @bot.command(pass_context=True)
# async def masterytotal(ctx):
#     """GETS THE SUMMONER'S TOTAL MASTERY POINTS"""
#     raw_name=ctx.message.content.split("~masterytotal ")
#     name=" ".join(raw_name[1:]).lower()
#     link = rq.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name, api)).text
#     rq_json = json.loads(link)
#     ide = rq_json['id']
#     mast = rq.get("https://na1.api.riotgames.com/lol/champion-mastery/v3/scores/by-summoner/{}?api_key={}".format(ide, api)).text
#     await bot.say("{}'s total mastery points is: {}".format(name,mast))





# @bot.command(pass_context=True)
# async def rank(ctx):
#     """GETS THE SUMMONER'S RANK INFO, ONLY SOLODUO"""
#     try:
#         raw_name=ctx.message.content.split("~rank ")
#         name=" ".join(raw_name[1:])
#         link = rq.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name, api)).text
#         rq_json = json.loads(link)
#         ide = rq_json['id']
#         link2 = rq.get("https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/{}?api_key={}".format(ide,api)).text
#         rq_json1 = json.loads(link2)
#         #solo/duo rank info
#         solo_rank = rq_json1[1]['queueType']
#         league_name_solo = rq_json1[1]['leagueName']
#         tier_solo = rq_json1[1]['tier']
#         wins_solo = rq_json1[1]['wins']
#         losses_solo = rq_json1[1]['losses']
#         division_solo = rq_json1[1]['rank']
#         points_solo = rq_json1[1]['leaguePoints']
#         await bot.say("Rank Type: {}\nLeague Name: {}\nTier: {}\nWins: {}\nLosses: {}\nDivision: {}\nPoints: {}".format(solo_rank,league_name_solo,tier_solo,wins_solo,losses_solo,division_solo,points_solo))
#     except IndexError:
#         if link2 == "[]":
#             await bot.say("Summoner {} is not ranked".format(name))

#     except:
#         solo_rank = rq_json1[0]['queueType']
#         league_name_solo = rq_json1[0]['leagueName']
#         tier_solo = rq_json1[0]['tier']
#         wins_solo = rq_json1[0]['wins']
#         losses_solo = rq_json1[0]['losses']
#         division_solo = rq_json1[0]['rank']
#         points_solo = rq_json1[0]['leaguePoints']
#         await bot.say("Rank Type: {}\nLeague Name: {}\nTier: {}\nWins: {}\nLosses: {}\nDivision: {}\nPoints: {}".format(solo_rank, league_name_solo, tier_solo, wins_solo,losses_solo, division_solo, points_solo))





bot.run('MzE3MDkyNzg4Mzc2NDM2NzM2.DaX1VA.ULX1Eda4dMNVkv44VX2506V1jco')
