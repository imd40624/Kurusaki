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
import tools
import bs4 as bs
import urllib
import urllib.request
import gspread
from oauth2client.service_account import ServiceAccountCredentials








api = os.environ["RIOT_KEY"]
wu_key = os.environ['WU_API']
owm = os.environ['open_weather']
img_api = os.environ['img_api']
apiai_token = os.environ['api_ai']
bot_token = os.environ['BOT_TOKEN']
An = Pymoe.Anilist()

bot = commands.Bot(command_prefix='s.')

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
            anime=rope.replace('$anime',anime)
            await bot.send_message(message.channel, anime)
        elif 'anime' not in rope:
            await bot.send_message(message.channel, rope)
        if "$time" in rope:
            await bot.say(datetime.datetime.now())
        if '$yukinno' in rope:
            author_id=message.author.id
            if author_id == 287369884940238849:
                love=['I love you Yukinno','Yukkino, I love you!','I love you!','<3']
                ran_love=random.choice(love)
                yukinno_love=rope.replace(rope,ran_love)
                await bot.send_message(message.channel, yukinno_love)
            elif message.author.id !=287369884940238849:
                await bot.send_message(message.channel, rope)
    scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials=ServiceAccountCredentials.from_json_keyfile_name('Annie-e432eb58860b.json',scope)
    gc= gspread.authorize(credentials)
    wks = gc.open('Kurusaki_database_discord').sheet1
    try:
        msg = message.content
        user_id = message.author.id
        name = message.author.name
        find_user_id = wks.find(user_id)

        #setting up spreadsheets for updates
        row = wks.find(user_id).row
        points = wks.cell(row, 3).value
        num_points = float(points)
        if len(msg) <= 2 and len(msg)>0:
            new_value = wks.update_cell(row, 3, num_points+.50)
        if len(msg) <=10 and len(msg)>2:
            new_value=wks.update_cell(row,3,num_points+1.50)
        if len(msg) <=20 and len(msg)>10:
            new_value=wks.update_cell(row,3,num_points+2.50)
        if len(msg) <=30 and len(msg)> 20:
            new_value=wks.update_cell(row,3,num_points+3.75)
        if len(msg) <=40 and len(msg)>30:
            new_value=wks.update_cell(row,3,num_points+6.00)
        if len(msg) <=50 and len(msg)>40:
            new_value=wks.update_cell(row,3,num_points+9.00)
        if len(msg) <=60 and len(msg) >50:
            new_value=wks.update_cell(row,3,num_points+12.50)
        if len(msg) <=70 and len(msg) >60:
            new_value=wks.update_cell(row,3,num_points+16.00)
        if len(msg) <=100 and len(msg) > 90:
            new_value=wks.update_cell(row,3,num_points+19.55)
    except gspread.exceptions.CellNotFound:
        print("Discord {} is not in Kurusaki's database yet.\nAttempting to add {} to database.".format(name,name))
        adding_user = wks.append_row([name, user_id, 5.00])
    try:
        if "gay" in message.content:
            await bot.send_message(message.channel,":ok_hand:")
    except:
        await bot.send_typing(message.channel)
        await bot.send_message(message.channel, "Something went wrong while trying to react to the message sent.")
    await bot.process_commands(message)




@bot.command(pass_context=True)
async def ping(ctx):
    """PINGS THE BOT"""
    await bot.say(":ping_pong: ping!!")
    print ("user has pinged")


@bot.command(pass_context=True)
async def tts(ctx):
    """REPEATS WHATEVER THE USER SAYS USING TEXT TO SPEECH"""
    msg_id = ctx.message
    repeat = ctx.message.content[5:]
    await bot.say(repeat, tts=True)
    await asyncio.sleep(120)
    await bot.delete_message(msg_id)




@bot.command(pass_context=True)
async def say(ctx):
    """REPEATS WHATEVER THE USER SAYS"""
    msg_id = ctx.message
    repeat = ctx.message.content[5:]
    await bot.say(repeat)
    await asyncio.sleep(120)
    await bot.delete_message(msg_id)



@bot.command(pass_context=True)
async def credits(ctx):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials=ServiceAccountCredentials.from_json_keyfile_name('Annie-e432eb58860b.json',scope)
    gc = gspread.authorize(credentials)
    wks = gc.open('Kurusaki_database_discord').sheet1
    try:
        tax=25
        author_id=ctx.message.author.id
        row=wks.find(author_id).row
        cred=wks.cell(row,3).value
        await bot.say("{} You have a total of {} credits".format(ctx.message.author.mention,cred))
    except:
        await bot.say("Something went wrong while trying to find your credits.")

@bot.command(pass_context=True)
async def check(ctx, user:discord.Member):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('Annie-e432eb58860b.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open('Kurusaki_database_discord').sheet1
    try:
        tax=50
        checker=ctx.message.author.id
        target_id=user.id
        target_name=user.name
        target_row=wks.find(target_id).row
        target_credits=wks.cell(target_row,3).value
        # target_float=float(target_credits)
        checker_row=wks.find(checker).row
        checker_credits=wks.cell(checker_row,3).value
        checker_float=float(checker_credits)
        update_checker=wks.update_cell(checker_row,3,checker_float-tax)
        update_target=wks.update_cell(target_row,3,target_credits)
        await bot.say("{} credits have been removed from you as tax.\n{} The user {} has a total of {} credits.".format(tax,ctx.message.author.mention,target_name,target_credits))
    except gspread.exceptions.CellNotFound:
        tax=35
        checker=ctx.message.author.id
        checker_row=wks.find(checker).row
        checker_credits = wks.cell(checker_row, 3).value
        checker_float=float(checker_credits)
        await bot.say("User {} is not in database".format(target_name))
        await bot.say("Attempting to adding user to database")
        update_target = wks.update_cell(target_row, 3, target_credits)
        adding_user = wks.append_row([target_name, target_id, 55.00])
        update_checker = wks.update_cell(checker_row, 3,checker_flaot-tax)
        await bot.say("{} now has 55.00 credits".format(target_name))
        await bot.say("{} credits has been removed from your account as tax.".foramt(tax))

# @bot.command(pass_context=True)
# async def scoreboard(ctx):
#     scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
#     credentials = ServiceAccountCredentials.from_json_keyfile_name('Annie-e432eb58860b.json', scope)
#     gc = gspread.authorize(credentials)
#     wks = gc.open('Kurusaki_database_discord').sheet1
#     try:
#         records=wks.get_all_records()
#         await bot.say(records)
#     except:
#         await bot.say("Something went wrong")


@bot.command(pass_context=True)
async def gift(ctx, user:discord.Member):
    try:
        tax = 50
        #user setup
        name=user.name
        user_id=user.id
        amount=100
        sender_name=ctx.message.author.name
        receiver_name=user.name
        receiver=user.id
        sender=ctx.message.author.id
        #google locations
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('Annie-e432eb58860b.json', scope)
        gc = gspread.authorize(credentials)
        wks = gc.open('Kurusaki_database_discord').sheet1
        #finding user row and value
        receiver_row=wks.find(receiver).row
        sender_row=wks.find(sender).row
        sender_credits=wks.cell(sender_row,3).value
        receiver_credits=wks.cell(receiver_row,3).value
        send_float=float(sender_credits)
        receiver_float=float(receiver_credits)
        tax_gift=tax+amount
        new_sender_value=send_float-tax_gift
        new_receiver_value=receiver_float+amount
        update_sender=wks.update_cell(sender_row,3,new_sender_value)
        update_receiver=wks.update_cell(receiver_row,3,new_receiver_value)
        user_tax=wks.update_cell(sender_row,7,tax)
        await bot.say("{} credits have been sent to {} from your credits".format(amount,receiver_name))
        await bot.say("{} credits have been removed from your accoutn as tax.".format(tax))
    except gspread.exceptions.CellNotFound:
        tax=25
        await bot.say("Dscord user {} has no credits data".format(receiver_name))
        await bot.say("Attempting to add the data")
        adding_user = wks.append_row([name, user_id, 55.00])
        await bot.say("The user {} now has 55.00 credits.".format(receiver_name))
        send_id=ctx.message.author.id
        send_row=wks.find(send_id).row
        send_credits=wks.cell(send_row,3).value
        send_float=float(send_credits)
        send_update=wks.update_cell(send_row,3,send_float-tax)
        user_tax=wks.update_cell(send_row,7,tax)
        await bot.say("{} credits have been removed from your accoutn as tax.".format(tax))



        
@bot.command(pass_context=True)
async def dog(ctx):
    """GENERATES A RANDOM PICTURE OF A DOG"""
    try:
        source = 'https://random.dog/'
        page = urllib.request.urlopen(source)
        sp = bs.BeautifulSoup(page, 'html.parser')
        pic = sp.img
        se = str(pic)
        hal = se[23:-3]
        # char=str(hal)
        url='https://random.dog/{}'.format(hal)
        # print(url)
        if url == 'https://random.dog/':
            # print("is a video")
            while True:
                src = 'https://random.dog/'
                pg = urllib.request.urlopen(source)
                s = bs.BeautifulSoup(pg, 'html.parser')
                pi = s.img
                e = str(pi)
                ha = e[23:-3]
                ul = 'https://random.dog/{}'.format(ha)
                if ul !='https://random.dog':
                    await bot.say(ul);
                    break;
        elif url != 'https://random.dog/':
            await bot.say(url)



    except:
        await bot.say("Command is currently not available.")

    

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
async def dice(ctx):
    """GENERATES A RANDOM BETWEEN 1-6"""
    r=random.choice(range(1,7))
    await bot.say("{}".format(r))

@bot.command(pass_context=True)
async def game(ctx):
    """CHANGES THE PLAYING STATUS OF THE BOT. EX: a.game OSU!"""
    mesg = ctx.message.content[6:]
    await bot.change_presence(game=discord.Game(name=mesg))





@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    """GETS THE BASIC INFORMATION OF A USER IN DISCORD. EX: a.info @Kurusaki#4763"""
    await bot.say("The user's name is: {}\n{}'s ID is: {}\n{} is: {}\n{}'s highest role is: {}\n{} joined at: {}".format(user.name,user.name,user.id,user.name,user.status,user.name,user.top_role,user.name,user.joined_at))



# @bot.command(pass_context=True)
# async def serverinfo(ctx):
#     g=ctx.message.author.server
#     name=ctx.message.author.server.name
#     member_count=g.members
#     owner=g.owner
#     m_c=g.member_count
#     await bot.say("{}{}{}{}".format(name,member_count,m_c,owner))
  
  



@bot.command(pass_context=True)
async def catfact(ctx):
    """SENDS YOU A RANDOM FACT ABOUT CATS. EX: a.catfact"""
    url = 'https://cat-fact.herokuapp.com/facts/random?amount=1'
    rq_url=rq.get(url).text
    rq_json=json.loads(rq_url)
    await bot.say(rq_json['text'])



    
    
@bot.command(pass_context=True)
async def randomanime(ctx):
    """GENERATES A RANDOM ANIME TITLE WITH 10 SECOND COOL DOWN. EX: a.randomanime"""
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
    """GENERATES A RANDOM MOVIE TITLE. EX: a.randommovie"""
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
    url = 'https://tv-v2.api-fetch.website/random/show'
    r=rq.get(url).text
    r_json=json.loads(r)
    name=r_json['title']
    year=r_json['year']
    img=r_json['images']['poster']
    await bot.say("Name: {}\nYear: {}\nPoster: {}".format(name,year,img))

    


@bot.command(pass_context=True)
async def invite(ctx):
    """GET AN INVITE LINK FOR THIS DISCORD BOT. EX: a.invite"""
    await bot.say("Here is the invite link for {}\n{}".format(bot.user.name,'https://discordapp.com/oauth2/authorize?client_id=403402614454353941&scope=bot'))


@bot.command(pass_context=True)
async def weather(ctx):
    """GET THE WEATHER IN YOUR CITY. EX: a.weather austin"""
    city_state=ctx.message.content[10:]
    t = u"\u00b0"
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'.format(city_state,owm)
        ser = rq.get(url).text
        rq_json = json.loads(ser)   
        temp = rq_json['main']['temp']
        max_temp = rq_json['main']['temp_max']
        min_temp = rq_json['main']['temp_min']
        dis = rq_json['weather'][0]['description']
        wind = rq_json['wind']['speed']
        await bot.say("Temperature in {} is around {}{}F\nMinimum Temperature is: {}{}F\nMaximum Temperature is: {}{}F\nMainly: {} Wind speed is around: {} MPH".format(city_state,temp,t,min_temp,t,max_temp,t,dis,wind))
    except:
        await bot.say("Looks like something went wrong. Your spelling may be incorrect or the bot may just be able to process this command at the moment.")


@bot.command(pass_context=True,case_insensitive=True)
async def cat(ctx):
    """GET A RANDOM PICTURE OF A CAT. EX: a.cat"""
    pictures = range(1, 1600)
    num = random.choice(pictures)
    url = 'https://random.cat/view/{}'.format(num)
    page = urllib.request.urlopen(url)
    sp = bs.BeautifulSoup(page, 'html.parser')
    pic = sp.img
    se = str(pic)
    img=se[26:-12]
    await bot.say(img)



@bot.command(pass_context=True)
async def img(ctx):
    """FAILED IMAGE GENERATOR BY KEYWORDS a.img dog"""
    query=ctx.message.content[5:]
    url ='http://version1.api.memegenerator.net//Generators_Search?q={}&apiKey={}'.format(query,img_api)
    rq_link = rq.get(url).text
    rq_json = json.loads(rq_link)
    await bot.say(rq_json['result'][0]['imageUrl'])



@bot.command(pass_context=True)
async def al(ctx):
    """SEARCH FOR ANIME WITH Anilist. EX: a.al School Rumble"""
    try:
        new_msg =ctx.message.content[4:]
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
    """SEARCH FOR ANIME USING MyAnimeList. EX: a.mal Mushishi"""
    query =ctx.message.content[5:]
    url = 'https://api.jikan.moe/search/anime/{}/'.format(query)
    rq_url = rq.get(url).text
    rq_json = json.loads(rq_url)
    anime_id = rq_json['result'][0]['mal_id']
    url2 = 'https://api.jikan.moe/anime/{}/stats/'.format(anime_id)
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



# @bot.command(pass_context=True)
# async def kick(ctx, user: discord.Member):
#     """KICKS USER THAT IS TAGGED"""
#     if ctx.message.author.id != 185181025104560128:
#         await bot.say("you do not have premission to kick out members.")
#     if ctx.message.author.id == 185181025104560128:
#         await bot.say(":boot: Bye bye, {}.".format(user.name))
#         await bot.kick(user)
#     else:
#         await bot.say("Huh?")





@bot.command(pass_context=True)
async def summoner(ctx):
    """GET BASIC INFO OF A GIVEN SUMMONER. EX: a.summoner Charming Mother"""
    try:
        name =ctx.message.content[10:]
        """GETS THE SUMMONER'S BASIC INFORMATION; NAME,LEVEL"""
        link = rq.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name, api)).text
        rq_json = json.loads(link)
        await bot.say("{}is level: {}\n{}'s profile icon is: {}\n{}'s ID is : {}\n{}'s Account ID is: {}".format(rq_json['name'],rq_json['summonerLevel'],rq_json['name'],rq_json['profileIconId'],rq_json['name'],rq_json['id'],rq_json['name'],rq_json['accountId']))
    except KeyError:
        await bot.say("{} is currently unable process your command.".format(bot.user.name))

@bot.command(pass_context=True)
async def lore(ctx):
    """GETS THE LORE OF A CHAMPION GIVEN. EX: a.lore Ashe"""
    new_msg =ctx.message.content[6:]
    champ = rq.get('https://na1.api.riotgames.com/lol/static-data/v3/champions/{}?locale=en_US&champData=lore&api_key={}'.format(champs['keys'][new_msg],api)).text
    champ_json=json.loads(champ)
    await bot.say("Champion Name: {}\nTitle: {}\nLore: {}".format(champ_json['name'],champ_json['title'],champ_json['lore']))





@bot.command(pass_context=True)
async def champmastery(ctx):
    """GET A CHAMP MASTERY OF A SUMMONER. EX: a.champmastery Charming Mother,Vayne"""
    msg=ctx.message.content[14:]
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




@bot.command(pass_context=True)
async def masterytotal(ctx):
    """GETS THE SUMMONER'S TOTAL MASTERY POINTS. EX: a.masterytotal Charming Mother"""
    name=ctx.message.content[14:]
    link = rq.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name, api)).text
    rq_json = json.loads(link)
    ide = rq_json['id']
    mast = rq.get("https://na1.api.riotgames.com/lol/champion-mastery/v3/scores/by-summoner/{}?api_key={}".format(ide, api)).text
    await bot.say("Points: {}".format(mast))



    
   
@bot.command(pass_context=True)
async def status(ctx):
    no_space=ctx.message.content[8:]
    mg="".join(no_space[1:])
    if mg== "kr":
        url = 'https://{}.api.riotgames.com/lol/status/v3/shard-data?api_key={}'.format(mg,api)
        r = rq.get(url).text
        r_json=json.loads(r)
        region=r_json['name']
        game=r_json['services'][0]['status']
        store = r_json['services'][1]['status']
        website = r_json['services'][2]['status']
        client = r_json['services'][3]['status']
        await bot.say("Region: {}\nGame: {}\nStore: {}\nWebsite: {}\nClient: {}".format(region,game,store,website,client))
    if mg=="ru":
        url = 'https://{}.api.riotgames.com/lol/status/v3/shard-data?api_key={}'.format(mg,api)
        r = rq.get(url).text
        r_json=json.loads(r)
        region=r_json['name']
        game=r_json['services'][0]['status']
        store = r_json['services'][1]['status']
        website = r_json['services'][2]['status']
        client = r_json['services'][3]['status']
        await bot.say("Region: {}\nGame: {}\nStore: {}\nWebsite: {}\nClient: {}".format(region,game,store,website,client))
    else:
        url = 'https://{}1.api.riotgames.com/lol/status/v3/shard-data?api_key={}'.format(mg,api)
        r = rq.get(url).text
        r_json=json.loads(r)
        region=r_json['name']
        game=r_json['services'][0]['status']
        store = r_json['services'][1]['status']
        website = r_json['services'][2]['status']
        client = r_json['services'][3]['status']
        await bot.say("Region: {}\nGame: {}\nStore: {}\nWebsite: {}\nClient: {}".format(region,game,store,website,client))



    

@bot.command(pass_context=True)  
async def rank(ctx):
    raw_msg=ctx.message.content[6:]
    url = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}'.format(
    raw_msg, api)
    r_basic = rq.get(url).text
    basic_json = json.loads(r_basic)
    try:
        code = basic_json['status']['status_code']
        if code ==404:
            await bot.say("Summoner by the name of {} does not exist".format(raw_msg))
    except:
        pass
    try:
        ide = basic_json['id']
        url2 = 'https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/{}?api_key={}'.format(
        ide, api)
        r = rq.get(url2).text
        r_json = json.loads(r)
        try:  
            if r_json[1] in r_json:
                #FLEX RANK
                rank2=r_json[1]
                q_type2=rank2['queueType']
                wins2=rank2['wins']
                losses2=rank2['losses']
                total_game2=wins2+losses2
                league_name2=rank2['leagueName']
                division2=rank2['rank']
                fresh_blood2=rank2['freshBlood']
                tier2=rank2['tier']
                points2=rank2['leaguePoints']
                #SOLO/DUO RANK
                rank=r_json[0]
                q_type=rank['queueType']
                wins=rank['wins']
                losses=rank['losses']
                total_game=wins+losses
                league_name=rank['leagueName']
                division=rank['rank']
                fresh_blood=rank['freshBlood']
                tier=rank['tier']
                points=rank['leaguePoints']
                await bot.say("Queue Type: {}\nTier: {}\nDivision:{}\nLeague Name:{}\nPoints:{}\nWins: {}\nLosses: {}\nTotal Wins: {}\nFresh Blood: {}\n\n\n\nQueue Type: {}\nTier: {}\nDivision:{}\nLeague Name:{}\nPoints:{}\nWins: {}\nLosses: {}\nTotal Wins: {}\nFresh Blood: {}".format(q_type2,tier2,division2,league_name2,points2,wins2,losses2,total_game2,fresh_blood2,q_type,tier,division,league_name,points,wins,losses,total_game,fresh_blood))

        except IndexError:
            try:
                if r_json[0]['queueType']=="RANKED_SOLO_5x5":
                    rank=r_json[0]
                    q_type=rank['queueType']
                    wins=rank['wins']
                    losses=rank['losses']
                    total_game=wins+losses
                    league_name=rank['leagueName']
                    division=rank['rank']
                    fresh_blood=rank['freshBlood']
                    tier=rank['tier']
                    points=rank['leaguePoints']
                    await bot.say("Queue Type: {}\nTier: {}\nDivision:{}\nLeague Name:{}\nPoints:{}\nWins: {}\nLosses: {}\nTotal Wins: {}\nFresh Blood: {}".format(q_type,tier,division,league_name,points,wins,losses,total_game,fresh_blood))
                if r_json[0]['queueType']=="RANKED_FLEX_SR":
                    rank=r_json[0]
                    q_type=rank['queueType']
                    wins=rank['wins']
                    losses=rank['losses']
                    total_game=wins+losses
                    league_name=rank['leagueName']
                    division=rank['rank']
                    fresh_blood=rank['freshBlood']
                    tier=rank['tier']
                    points=rank['leaguePoints']
                    await bot.say("Queue Type: {}\nTier: {}\nDivision:{}\nLeague Name:{}\nPoints:{}\nWins: {}\nLosses: {}\nTotal Wins: {}\nFresh Blood: {}".format(q_type,tier,division,league_name,points,wins,losses,total_game,fresh_blood))
            except IndexError:
                await bot.say("Summoner{} has no rank".format(raw_msg))
    except:
        pass


@bot.command(pass_context=True)
async def urban(ctx):
    """USES URBAN DICT TO FIND DEFINITION OF WORDS. EX: a.urban neko"""
    word=ctx.message.content[7:]
    link='http://api.urbandictionary.com/v0/define?term={}'.format(word)
    rq_link=rq.get(link).text
    rq_json=json.loads(rq_link)
    await bot.say("Word: {}\nVotes: {}\nDefinitioin: {}\nExample: {}".format(rq_json['list'][0]['word'],rq_json['list'][0]['thumbs_up'],rq_json['list'][0]['definition'],rq_json['list'][0]['example']))

    
bot.run(bot_token)
