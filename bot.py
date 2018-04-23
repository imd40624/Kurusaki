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
import apiai
import image_links
import random
import time




api = os.environ['RIOT_KEY']
wu_key=os.environ['WU_API']
owm=os.environ['open_weather']

An=Pymoe.Anilist()

bot = commands.Bot(command_prefix='a.')

@bot.event
async def on_ready():
    """WHEN BOT IS READY, PRINT MESSAGE IN TERMINAL"""
    print ("I am running on " + bot.user.name)
    mesg="Hello Kitty"
    await bot.change_presence(game=discord.Game(name=mesg))


@bot.event
async def on_message(message):
    mention = bot.user.mention
    if message.content.startswith(mention):
        anime=rq.get('https://kurusaki-webhook.herokuapp.com/').text
        raw_msg = message.content.split("{}".format(mention))
        msg = "".join(raw_msg[1:])
        #         print(msg)
        client_token = os.environ['api_ai']
        ai = apiai.ApiAI(client_token)
        request = ai.text_request()
        request.lang = 'en'
        request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
        request.query = msg
        response = request.getresponse()
        rope = str(response.read())
        rope = rope[rope.index("speech") + 10:]
        rope = rope[0:rope.index("\"")]
        if '$anime' in rope:
            anime=rope.replace('$anime',anime)
            await bot.send_message(message.channel, anime)
        else:
            await bot.send_message(message.channel, rope)
        await bot.process_commands(message)



@bot.command(pass_context=True)
async def ping(ctx):
    """PINGS THE BOT"""
    await bot.say(":ping_pong: ping!!")
    print ("user has pinged")



@bot.command(pass_context=True)
async def say(ctx):
    """REPEATS WHATEVER THE USER SAYS"""
    mesg=ctx.message.content.split("a.say ")
    repeat=" ".join(mesg[1:])
    await bot.say(repeat)




@bot.command(pass_context=True)
async def logout(ctx):
    """RESTARTS THE BOT IN HEROKU SERVER, BUT ENDS IN TERMINAL"""
    creator_id = 185181025104560128
    sender_id = ctx.message.author.id
    send_id=int(sender_id)
    if send_id == creator_id:
        await bot.say("Logging out bot now!")
        await bot.logout()
    else:
        await bot.say("Can not restart bot because you are not the creator")




@bot.command(pass_context=True)
async def game(ctx):
    raw_msg = ctx.message.content.split("a.game ")
    mesg = "".join(raw_msg[1:])
    await bot.change_presence(game=discord.Game(name=mesg))







@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    """GETS THE BASIC INFORMATION OF A USER IN DISCORD"""
    await bot.say("The user's name is: {}\n{}'s ID is: {}\n{} is: {}\n{}'s highest role is: {}\n{} joined at: {}".format(user.name,user.name,user.id,user.name,user.status,user.name,user.top_role,user.name,user.joined_at))







@bot.command(pass_context=True)
async def catfact(ctx):
    url = 'https://cat-fact.herokuapp.com/facts/random?amount=1'
    rq_url=rq.get(url).text
    rq_json=json.loads(rq_url)
    await bot.say(rq_json['text'])



    
    
@bot.command(pass_context=True)
async def randomanime(ctx):
    ra1=rq.get('https://private-anon-589c768a77-popcornofficial.apiary-proxy.com/random/anime')
    ra2=rq.get('https://tv-v2.api-fetch.website/random/anime')
    if ra1.status_code == 200:
        text=ra1.text
        rq_json=json.loads(text)
        title=rq_json['title']
        anime_id=rq_json['mal_id']
        genres=rq_json['genres']
        gen=" ".join(genres[1:])
        url2 = 'https://api.jikan.me/anime/{}/stats/'.format(anime_id)
        r2=rq.get(url2).text
        r2j=json.loads(r2)
        summary=r2j['synopsis']
        await bot.say("Title: {}\nGenres: {}\nSynopsis: {}".format(title,gen,summary))




@bot.command(pass_context=True)
async def randommovie(ctx):
    movie=rq.get('https://tv-v2.api-fetch.website/random/movie')
    if movie.status_code == 200:
        rest=movie.text
        rq_json=json.loads(rest)
        title=rq_json['title']
        summary=rq_json['synopsis']
        runtime=rq_json['runtime']
        genres=rq_json['genres']
        gen = " ".join(genres[1:])
        await bot.say("Title: {}\nGenres: {}\nLength: {} Minutes\nSynopsis: {}".format(title, gen, runtime, summary))




@bot.command(pass_context=True)
async def randomshow(ctx):
    movie = rq.get('https://tv-v2.api-fetch.website/random/show')
    if movie.status_code == 200:
        rest = movie.text
        rq_json = json.loads(rest)
        title = rq_json['title']
        await bot.say(title)    
    
    
    


@bot.command(pass_context=True)
async def invite(ctx):
    await bot.say("Here is the invite link for {}\n{}".format(bot.user.name,'https://discordapp.com/oauth2/authorize?client_id=403402614454353941&scope=bot'))





@bot.command(pass_context=True)
async def weather(ctx):
    wu_key = 'c8034bd5f8c70795'
    try:
        t = u"\u00b0"
        remove_command = ctx.message.content.split("a.weather ")
        city_state = " ".join(remove_command[1:])
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'.format(city_state,owm)
        ser = rq.get(url).text
        rq_json = json.loads(ser)   
        temp = rq_json['main']['temp']
        max_temp = rq_json['main']['temp_max']
        min_temp = rq_json['main']['temp_min']
        hum = rq_json['main']['humidity']
        wind = rq_json['wind']['speed']
        await bot.say("Hi")
        await bot.say("The temperature in {} is around {}{}F\nThe minimum Temperature is: {}\nThe maximum Temperature is: {}\nThe humidity is around: {}%\nWind speed is around: {}MPH".format(city_state, temp, t, min_temp, max_temp, hum, wind))
    except:

        if " " in city_state:
            remove_space = city_state.split()
            no_space = "".join(remove_space[0:])
            bett = no_space.find(',')
            state = no_space[bett + 1:]
            city = no_space[0:bett]
            url = 'http://api.wunderground.com/api/{}/conditions/q/{}/{}.json'.format(wu_key, state, city)
            rq_url = rq.get(url).text
            rq_json = json.loads(rq_url)
            await bot.say("Country: {}\nState: {}\nCity: {}\nTemperature: {}{}F ({}{}C)\nRelative Humidity: {}\nWind Speed: {}MPH\nPowered By: {}".format(rq_json['current_observation']['display_location']['country'],rq_json['current_observation']['display_location']['state_name'],rq_json['current_observation']['display_location']['city'],rq_json['current_observation']['temp_f'], t,rq_json['current_observation']['temp_c'], t,rq_json['current_observation']['relative_humidity'],rq_json['current_observation']['wind_mph'], image_links.wu))
        else:
            bett = city_state.find(',')
            state = city_state[bett + 1:]
            city = city_state[0:bett]
            url = 'http://api.wunderground.com/api/{}/conditions/q/{}/{}.json'.format(wu_key, state, city)
            rq_url = rq.get(url).text
            rq_json = json.loads(rq_url)
            await bot.say("Country: {}\nState: {}\nCity: {}\nTemperature: {}{}F ({}{}C)\nRelative Humidity: {}\nWind Speed: {}MPH\nPowered By: {}".format(rq_json['current_observation']['display_location']['country'],rq_json['current_observation']['display_location']['state_name'],rq_json['current_observation']['display_location']['city'],rq_json['current_observation']['temp_f'], t,rq_json['current_observation']['temp_c'], t,rq_json['current_observation']['relative_humidity'],rq_json['current_observation']['wind_mph'], image_links.wu))



@bot.command(pass_context=True,case_insensitive=True)
async def cat(ctx):
    raw_msg=ctx.message.content.lower().split("a.cat ")
    url='http://aws.random.cat/meow'
    rq_url=rq.get(url).text
    rq_json=json.loads(rq_url)
    pic=rq_json['file']
    await bot.say("{}".format(pic))




@bot.command(pass_context=True)
async def img(ctx):
    api = 'f4237223-a9fc-4a7a-b789-e7d2beebcbef'
    raw_inp = ctx.message.content.split("a.img ")
    query=" ".join(raw_inp[1:])
    url ='http://version1.api.memegenerator.net//Generators_Search?q={}&apiKey={}'.format(query,api)
    rq_link = rq.get(url).text
    rq_json = json.loads(rq_link)
    await bot.say(rq_json['result'][0]['imageUrl'])







@bot.command(pass_context=True)
async def al(ctx):
    """SEARCHES FOR AN ANIME THAT THE USER INPUTS FROM DISCORD USING a.ANIME (ANIME NAME)"""
    try:
        title=ctx.message.content.split("a.al ")
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
async def mal(ctx):
    _raw_input = ctx.message.content.lower().split("a.mal ")
    query = "".join(_raw_input[1:])
    url = 'https://api.jikan.me/search/anime/{}'.format(query)
    rq_url = rq.get(url).text
    rq_json = json.loads(rq_url)
    anime_id = rq_json['result'][0]['id']
    url2 = 'https://api.jikan.me/anime/{}/stats/'.format(anime_id)
    rq_url2 = rq.get(url2).text
    rq_json2 = json.loads(rq_url2)
    summary = rq_json2['synopsis']
    title_jp = rq_json2['title_japanese']
    title_en = rq_json2['title_english']
    anime_type = rq_json2['type']
    status = rq_json2['status']
    airing = rq_json2['airing']
    aired_from = rq_json2['aired']['from']
    aired_to = rq_json2['aired']['to']
    episodes = rq_json2['episodes']
    source = rq_json2['source']
    members = rq_json2['members']
    popularity = rq_json2['popularity']
    rank = rq_json2['rank']
    duration = rq_json2['duration']
    rating = rq_json2['rating']
    premiered = rq_json2['premiered']
    favorites = rq_json2['favorites']
    scored_by = rq_json2['scored_by']
    score = rq_json2['score']
    #anime formatting output
    anime_picture = rq_json2['image_url']
    await bot.say('Here is what I could find about your query')
    embed = discord.Embed(title="Title: {}".format(query), description=title_en+":"+title_jp, color=0xDEADBF)
    embed.add_field(name="Type",value=anime_type)
    embed.add_field(name="Status",value=status)
    embed.add_field(name="Members",value=members)
    embed.add_field(name="Popularity",value=popularity)
    embed.add_field(name="Rank",value=rank)
    embed.add_field(name="Favorites",value=favorites)
    embed.add_field(name="Score",value=score)
    embed.add_field(name="Scored By",value=scored_by)
    embed.add_field(name="Aired From",value=aired_from)
    embed.add_field(name="Rating",value=rating)
    embed.add_field(name="Duration",value=duration)
    embed.add_field(name="Premiered",value=premiered)
    await bot.say(embed=embed)
    await bot.say("Summary: {}\n{}".format(summary,anime_picture))



@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    """KICKS USER THAT IS TAGGED"""
    await bot.say(":boot: Bye bye, {}.".format(user.name))
    await bot.kick(user)





@bot.command(pass_context=True)
async def summoner(ctx):
    try:
        raw_name = ctx.message.content.split("a.summoner ")
        name = " ".join(raw_name[1:])
        """GETS THE SUMMONER'S BASIC INFORMATION; NAME,LEVEL"""
        link = rq.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name, api)).text
        rq_json = json.loads(link)
        await bot.say("{}is level: {}\n{}'s profile icon is: {}\n{}'s ID is : {}\n{}'s Account ID is: {}".format(rq_json['name'],rq_json['summonerLevel'],rq_json['name'],rq_json['profileIconId'],rq_json['name'],rq_json['id'],rq_json['name'],rq_json['accountId']))
    except KeyError:
        await bot.say("{} is currently unable process your command.".format(bot.user.name))

@bot.command(pass_context=True)
async def lore(ctx):
    """GETS THE LORE OF A CHAMPION GIVEN"""
    champ_name = ctx.message.content.split("a.lore ")
    new_msg = " ".join(champ_name[1:]).lower()
    champ = rq.get('https://na1.api.riotgames.com/lol/static-data/v3/champions/{}?locale=en_US&champData=lore&api_key={}'.format(champs['keys'][new_msg],api)).text
    champ_json=json.loads(champ)
    await bot.say("Champion Name: {}\nTitle: {}\nLore: {}".format(champ_json['name'],champ_json['title'],champ_json['lore']))





@bot.command(pass_context=True)
async def champ_mastery(ctx):
    raw_msg=ctx.message.content.split("a.champ_mastery ")
    msg="".join(raw_msg[1:])
    bett=msg.find(",")
    summoner=msg[0:bett]
    champ=msg[bett+1:]
    url1="https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(summoner,api)
    sum_info = rq.get(url1).text
    info_json=json.loads(sum_info)
    name=info_json['name']
    sum_id=info_json['id']
    url2="https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/{}/by-champion/{}?api_key={}".format(sum_id,champs['keys'][champ],api)
    mast_info=rq.get(url2).text
    mast_json=json.loads(mast_info)
    champ_lvl=mast_json['championLevel']
    champ_points=mast_json['championPoints']
    chest=mast_json['chestGranted']
    await bot.say("Level: {}\nPoints: {}\nChest: {}".format(champ_lvl,champ_points,chest))
    await bot.say(mast_json)




@bot.command(pass_context=True)
async def masterytotal(ctx):
    """GETS THE SUMMONER'S TOTAL MASTERY POINTS"""
    raw_name=ctx.message.content.split("a.masterytotal ")
    name=" ".join(raw_name[1:]).lower()
    link = rq.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name, api)).text
    rq_json = json.loads(link)
    ide = rq_json['id']
    mast = rq.get("https://na1.api.riotgames.com/lol/champion-mastery/v3/scores/by-summoner/{}?api_key={}".format(ide, api)).text
    await bot.say("Points: {}".format(mast))



@bot.command(pass_context=True)
async def status(ctx):
    raw_inp = ctx.message.content.split("a.status ")
    region=" ".join(raw_inp[1:]).lower()
    try:
        if region == "kr" or "ru":
            link1 = 'https://{}.api.riotgames.com/lol/status/v3/shard-data?api_key={}'.format(region, api)
            rq_link1=rq.get(link1).text
            rq_json1=json.loads(rq_link1)
            await bot.say("Region: {}\nGame: {}\nStore: {}\nWebsite: {}\nClient: {}".format(rq_json1['name'],rq_json1['services'][0]['status'],rq_json1['services'][1]['status'],rq_json1['services'][2]['status'],rq_json1['services'][3]['status']))

    except:
        link = 'https://{}1.api.riotgames.com/lol/status/v3/shard-data?api_key={}'.format(region, api)
        rq_link=rq.get(link).text
        rq_json=json.loads(rq_link)
        await bot.say("Region: {}\nGame: {}\nStore: {}\nWebsite: {}\nClient: {}".format(rq_json['name'],rq_json['services'][0]['status'],rq_json['services'][1]['status'],rq_json['services'][2]['status'],rq_json['services'][3]['status']))



@bot.command(pass_context=True)
async def rank(ctx):
    """GETS THE SUMMONER'S RANK INFO, ONLY SOLODUO"""
    try:
        raw_name=ctx.message.content.split("a.rank ")
        name=" ".join(raw_name[1:])
        link = rq.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name, api)).text
        rq_json = json.loads(link)
        ide = rq_json['id']
        link2 = rq.get("https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/{}?api_key={}".format(ide,api)).text
        rq_json1 = json.loads(link2)
        #solo/duo rank info
        solo_rank = rq_json1[1]['queueType']
        league_name_solo = rq_json1[1]['leagueName']
        tier_solo = rq_json1[1]['tier']
        wins_solo = rq_json1[1]['wins']
        losses_solo = rq_json1[1]['losses']
        division_solo = rq_json1[1]['rank']
        points_solo = rq_json1[1]['leaguePoints']
        await bot.say("Rank Type: {}\nLeague Name: {}\nTier: {}\nWins: {}\nLosses: {}\nDivision: {}\nPoints: {}".format(solo_rank,league_name_solo,tier_solo,wins_solo,losses_solo,division_solo,points_solo))
    except IndexError:
        if link2 == "[]":
            await bot.say("Summoner {} is not ranked".format(name))

    except:
        solo_rank = rq_json1[0]['queueType']
        league_name_solo = rq_json1[0]['leagueName']
        tier_solo = rq_json1[0]['tier']
        wins_solo = rq_json1[0]['wins']
        losses_solo = rq_json1[0]['losses']
        division_solo = rq_json1[0]['rank']
        points_solo = rq_json1[0]['leaguePoints']
        await bot.say("Rank Type: {}\nLeague Name: {}\nTier: {}\nWins: {}\nLosses: {}\nDivision: {}\nPoints: {}".format(solo_rank, league_name_solo, tier_solo, wins_solo,losses_solo, division_solo, points_solo))




@bot.command(pass_context=True)
async def urban(ctx):
    word1=ctx.message.content.split("a.urban ")
    word=" ".join(word1[1:])
    link='http://api.urbandictionary.com/v0/define?term={}'.format(word)
    rq_link=rq.get(link).text
    rq_json=json.loads(rq_link)
    await bot.say("Word: {}\nVotes: {}\nDefinitioin: {}\nExample: {}".format(rq_json['list'][0]['word'],rq_json['list'][0]['thumbs_up'],rq_json['list'][0]['definition'],rq_json['list'][0]['example']))

    



bot.run(os.environ['BOT_TOKEN'])
