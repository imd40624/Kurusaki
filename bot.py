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
import bs4 as bs
import urllib
import urllib.request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.utils import get


#GETTING API KEYS FROM HEROKU
api = os.environ["RIOT_KEY"]
wu_key = os.environ['WU_API']
owm = os.environ['open_weather']
img_api = os.environ['img_api']
apiai_token = os.environ['api_ai']
bot_token = os.environ['BOT_TOKEN']
An = Pymoe.Anilist()

bot = commands.Bot(command_prefix='s.')  # SETUP BOT COMMAND PREFIX


@bot.event
async def on_ready():

    """WHEN BOT IS READY, PRINT MESSAGE IN TERMINAL"""
    print("I am running on " + bot.user.name)
    games=['Bread Puppies','Jump Rope Kitten: Nyawatobi','TripTrap','Potion Maker','Crusaders Quest','My Waffle Maker','AfroCat','Hello Kitty','Halo 4','My Cat Album','LINE: Disney Tsum Tsum','Cat Room','Alphabear','Play With Cats','My Dog Album','Giant Turnip Game','MEOW MEOW STAR ACRES','Patchmania','Tiny Sheep','Hello Kitty World – Fun Park Game']
#     while True:
#         global random_status_game
#         random_status_game=random.choice(games)
#         await asyncio.sleep(2)
    await bot.change_presence(game=discord.Game(name='Jump Rope Kitten'))




# #google spreadsheet connect
# scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
# credentials = ServiceAccountCredentials.from_json_keyfile_name('Annie-e432eb58860b.json', scope)
# gc = gspread.authorize(credentials)
# wks = gc.open('Kurusaki_database_discord').sheet1




@bot.event
async def on_message(message):
    mention = bot.user.mention
    if message.content.startswith(mention):
        discord_name=message.author.display_name
        discord_id=message.author.id
        raw_msg = message.content.split("{}".format(mention))
        msg = "".join(raw_msg[1:])
        if "?" in msg:
            msg=msg.replace("?","")
        get_resp=rq.get('https://kurusaki-webhook.herokuapp.com/kurusaki/{}/{}/{}'.format(msg,discord_id,discord_name)).text
        await bot.send_message(message.channel,get_resp)
#     try:
#         msg = message.content
#         user_id = message.author.id
#         name = message.author.name
#         find_user_id = wks.find(user_id)

#         #setting up spreadsheets for updates
#         row = wks.find(user_id).row
#         points = wks.cell(row, 3).value
#         if points == "":
#             get_value=wks.update_cell(row,3,2)
#         num_points = float(points)
#         if len(msg) <= 2 and len(msg) > 0:
#             new_value = wks.update_cell(row, 3, num_points+.50)
#         if len(msg) <= 10 and len(msg) > 2:
#             new_value = wks.update_cell(row, 3, num_points+.60)
#         if len(msg) <= 20 and len(msg) > 10:
#             new_value = wks.update_cell(row, 3, num_points+1.20)
#         if len(msg) <= 30 and len(msg) > 20:
#             new_value = wks.update_cell(row, 3, num_points+2.75)
#         if len(msg) <= 40 and len(msg) > 30:
#             new_value = wks.update_cell(row, 3, num_points+3.00)
#         if len(msg) <= 50 and len(msg) > 40:
#             new_value = wks.update_cell(row, 3, num_points+2.00)
#         if len(msg) <= 60 and len(msg) > 50:
#             new_value = wks.update_cell(row, 3, num_points+4.50)
#         if len(msg) <= 70 and len(msg) > 60:
#             new_value = wks.update_cell(row, 3, num_points+6.00)
#         if len(msg) <= 80 and len(msg) > 70:
#             new_value = wks.update_cell(row, 3, num_points+7.50)
#         if len(msg) <= 90 and len(msg) > 80:
#             new_value = wks.update_cell(row, 3, num_points+9.20)
#         if len(msg) <= 100 and len(msg) > 90:
#             new_value = wks.update_cell(row, 3, num_points+10.55)
#         if len(msg) <= 110 and len(msg) > 100:
#             new_value = wks.update_cell(row, 3, num_points+12.20)
#         if len(msg) <= 120 and len(msg) > 110:
#             new_value = wks.update_cell(row, 3, num_points+16.20)
#         if len(msg) <= 130 and len(msg) > 120:
#             new_value = wks.update_cell(row, 3, num_points+20.70)
#         if len(msg) <= 140 and len(msg) > 130:
#             new_value = wks.update_cell(row, 3, num_points+27.20)
#         if len(msg) <= 150 and len(msg) > 140:
#             new_value = wks.update_cell(row, 3, num_points+34.20)
#         if len(msg) <= 160 and len(msg) > 150:
#             new_value = wks.update_cell(row, 3, num_points+39.20)
#         if len(msg) <= 170 and len(msg) > 160:
#             new_value = wks.update_cell(row, 3, num_points+44.20)
#         if len(msg) <= 180 and len(msg) > 170:
#             new_value = wks.update_cell(row, 3, num_points+49.60)
#         if len(msg) <= 190 and len(msg) > 180:
#             new_value = wks.update_cell(row, 3, num_points+55.20)
#         if len(msg) <= 200 and len(msg) > 190:
#             new_value = wks.update_cell(row, 3, num_points+63.20)
#         if len(msg) <= 210 and len(msg) > 200:
#             new_value = wks.update_cell(row, 3, num_points+79.20)
#         if len(msg) <= 220 and len(msg) > 210:
#             new_value = wks.update_cell(row, 3, num_points+87.20)
#         if len(msg) <= 230 and len(msg) > 220:
#             new_value = wks.update_cell(row, 3, num_points+109.99)
#         if len(msg) <= 240 and len(msg) > 230:
#             new_value = wks.update_cell(row, 3, num_points+130.20)
#         if len(msg) <= 250 and len(msg) > 240:
#             new_value = wks.update_cell(row, 3, num_points+154.20)
#         if len(msg) <= 260 and len(msg) > 250:
#             new_value = wks.update_cell(row, 3, num_points+178.20)
#         if len(msg) <= 270 and len(msg) > 260:
#             new_value = wks.update_cell(row, 3, num_points+210.20)
#         if len(msg) <= 280 and len(msg) > 270:
#             new_value = wks.update_cell(row, 3, num_points+250.20)
#         if len(msg) <= 290 and len(msg) > 280:
#             new_value = wks.update_cell(row, 3, num_points+277.20)
#         if len(msg) <= 500 and len(msg) > 300:
#             new_value = wks.update_cell(row, 3, num_points+440.20)
#     except gspread.exceptions.CellNotFound:
#         print("Discord {} is not in Kurusaki's database yet.\nAttempting to add {} to database.".format(name, name))
#         adding_user = wks.append_row([name, user_id, 2.00])
    
   
    #reacting to discord user's message
    try:
        if "gay" in message.content.lower():
            await bot.add_reaction(message, emoji='👌')
            await bot.add_reaction(message, emoji='🏳️‍🌈')
        if "yukinno" in message.content.lower():
            await bot.add_reaction(message, emoji='❤')
            await bot.add_reaction(message, emoji='🌸')
            await bot.add_reaction(message, emoji='😇')
        if "🤔" in message.content.lower():
            await bot.add_reaction(message, emoji='🤔')
        if "👌" in message.content.lower():
            await bot.add_reaction(message, emoji='👌')
        if "think" in message.content.lower():
            emote=get(bot.get_all_emojis(), name='016')
            await bot.add_reaction(message, emoji=emote)
            await bot.add_reaction(message, emoji='🤔')
        if "league" in message.content.lower():
            emote=get(bot.get_all_emojis(), name='league')
            await bot.add_reaction(message, emoji=emote)
        if "teemo" in message.content.lower():
            emote=get(bot.get_all_emojis(), name='teemo')
            await bot.add_reaction(message, emoji=emote)
        if 'okay' in message.content.lower():
            await bot.add_reaction(message, emoji='👌')
        if 'flower' in message.content.lower():
            await bot.add_reaction(message, emoji='🌸')
        if 'gj' in message.content.lower():
            await bot.add_reaction(message, emoji='👏')
        if 'good job' in message.content.lower():
            await bot.add_reaction(message, emoji='👏')
        if 'nice job' in message.content.lower():
            await bot.add_reaction(message, emoji='👏')
        if 'cake' in message.content.lower():
            await bot.add_reaction(message, emoji='🍰')
        if 'goodjob' in message.content.lower():
            await bot.add_reaction(message, emoji='👏')
        if 'bye' in message.content.lower():
            await bot.add_reaction(message, emoji='👋')
        if 'bai' in message.content.lower():
            await bot.add_reaction(message, emoji='👋')
        if "<@287369884940238849>" in message.content.lower():
            await bot.add_reaction(message, emoji='❤')
            await bot.add_reaction(message, emoji='🌸')
            await bot.add_reaction(message, emoji='😇')
        if 'sleep' in message.content.lower():
            await bot.add_reaction(message, emoji='💤')
        if 'i\'m sick' in message.content.lower():
            await bot.add_reaction(message, emoji='🤧')
        if 'got sick' in message.content.lower():
            await bot.add_reaction(message, emoji='🤧')

        re = 287369884940238849
        send_id = int(message.author.id)
        if send_id == re:
            await bot.add_reaction(message, emoji='❤')
            await bot.add_reaction(message, emoji='🌸')
            await bot.add_reaction(message, emoji='😇')
        if "michelle" in message.content.lower():
            await bot.add_reaction(message, emoji='❤')
            await bot.add_reaction(message, emoji='😇')
            await bot.add_reaction(message, emoji='🌸')
        if "poop" in message.content.lower():
            await bot.add_reaction(message, emoji='🤔')
            await bot.add_reaction(message, emoji='💩')
        if "shit" in message.content.lower():
            await bot.add_reaction(message, emoji='💩')
    except:
        pass
#     try:  # message counter for users
#         try:
#             user_id = message.author.id  # user's id
#             user_row = wks.find(user_id).row  # finds user's row
#             msg_value = wks.cell(user_row, 6).value  # get user's msg value
#             if msg_value == "":  # check if the user has empty value
#                 # if user value is empty add value =1
#                 adding_value = wks.update_cell(user_row, 6, 1)
#             else:  # updating the user's new message value
#                 msg_int = int(msg_value)
#                 update_msg = wks.update_cell(user_row, 6, msg_int+1)
#         except:
#             print("Could not add msg value")
#     except:
#         print("Could not connect to google spreadsheet")
    await bot.process_commands(message)


# @bot.command(pass_context=True)
# async def ping(ctx):
#     """PINGS THE BOT"""
#     await bot.say(":ping_pong: ping!!")
#     print("user has pinged")


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


# @bot.command(pass_context=True)
# async def credits(ctx):
#     """CHECKS YOUR CREDITS"""

#     tax = 25
#     author_id = ctx.message.author.id
#     row = wks.find(author_id).row
#     cred = wks.cell(row, 3).value
#     cred_float = float(cred)
#     msg = await bot.say("{} You have a total of {} credits".format(ctx.message.author.mention, cred))
#     try:
#         if cred_float > 1200:
#             await bot.add_reaction(msg, emoji='💲')
#         if cred_float > 2300:
#             await bot.add_reaction(msg, emoji='💸')
#         if cred_float > 3400:
#             await bot.add_reaction(msg, emoji='🤑')
#         if cred_float > 4200:
#             await bot.add_reaction(msg, emoji='💵')
#         if cred_float > 5300:
#             await bot.add_reaction(msg, emoji='💰')
#     except:
#         await bot.say("Something went wrong while trying to react to your message")


# @bot.command(pass_context=True)
# async def check(ctx, user: discord.Member):
#     """CHECKS ANOTHER USER'S CREDITS. Ex: s.check @kurusaki"""
#     try:

#         tax = 50
#         checker = ctx.message.author.id  # pserson who is checking someone's credits
#         target_id = user.id  # the person that is getting his/her credits checked
#         target_name = user.name  # target's name
#         target_row = wks.find(target_id).row  # target's row
#         checker_row = wks.find(checker).row  # checker's row
#         target_credits = wks.cell(target_row, 3).value  # target's value
#         checker_credits = wks.cell(checker_row, 3).value
#         checker_float = float(checker_credits)  # checker's credits in float
#         target_float = float(target_credits)  # target's credits in float
#         update_checker = wks.update_cell(
#             checker_row, 3, checker_float-tax)  # taxing the checker
#         msg = await bot.say("{} The user {} has a total of {} credits.\n{} credits have been removed from you as tax.".format(ctx.message.author.mention, target_name, target_credits, tax))

#         #reacting to high credits
#         if target_float > 1200:
#             await bot.add_reaction(msg, emoji='💲')
#         if target_float > 2300:
#             await bot.add_reaction(msg, emoji='💸')
#         if target_float > 3400:
#             await bot.add_reaction(msg, emoji='🤑')
#         if target_float > 4200:
#             await bot.add_reaction(msg, emoji='💵')
#         if target_float > 5300:
#             await bot.add_reaction(msg, emoji='💰')
#         try:
#             # updating the user's  tax
#             checker_tax_value = wks.cell(
#                 checker_row, 7).value  # current tax value
#             tax_float = float(checker_tax_value)  # tax value into float
#             # updating the new tax value
#             updating_tax = wks.update_cell(checker_row, 7, tax_float+tax)
#         except:
#             new_tax = wks.update_cell(checker_row, 7, tax)
#             print("User had no current tax value, so it was added")

#     except gspread.exceptions.CellNotFound:  # if user has no database in gspread
#         tax = 35
#         checker = ctx.message.author.id  # checker id
#         checker_row = wks.find(checker).row  # checker's row
#         # checker's credits value
#         checker_credits = wks.cell(checker_row, 3).value
#         checker_float = float(checker_credits)  # checker credits float
#         await bot.say("User {} is not in database".format(target_name))
#         await bot.say("Attempting to adding user to database")
#         # adding value to no existing user
#         adding_user = wks.append_row([target_name, target_id, 55.00])
#         update_checker = wks.update_cell(
#             checker_row, 3, checker_float-tax)  # taxing user
#         await bot.say("{} now has 55.00 credits".format(target_name))
#         await bot.say("{} credits has been removed from your account as tax.".format(tax))

#         try:  # updating the user's tax
#             checker_tax_value = wks.cell(
#                 checker_row, 7).value  # checker's tax value
#             if checker_tax_value == "":
#                 new_tax = wks.update_cell(checker_row, 7, tax)
#             else:  # ADD A NEW TAX VALUE IF IT IS BLANK
#                 tax_float = float(checker_tax_value)
#                 updating_tax = wks.update_cell(checker_row, 7, tax_float+tax)
#         except:
#             print("Unable to add the user{} to tax database ".format(
#                 ctx.message.name))


# @bot.command(pass_context=True)
# async def scoreboard(ctx):
#     try:
#         records=wks.get_all_records()
#         await bot.say(records)
#     except:
#         await bot.say("Something went wrong")


# @bot.command(pass_context=True)
# async def rewards(ctx):  # ADD REACTIONS FOLLOWING THE REWARD TYPES
#     await bot.say("Currently only reaction rewards are available.")
#     msg = await bot.say(":rolling_eyes: :900\n:cherry_blossom: :1150\n:ok_hand: :900\n:kiss: : 900\n:thinking: :700\n:poop: : 800\n:zzz: :550\n:scream: :800\n:innocent: :2000")
#     await bot.add_reaction(msg, emoji='🌸')
#     await bot.add_reaction(msg, emoji='💋')
#     await bot.add_reaction(msg, emoji='👌')
#     await bot.add_reaction(msg, emoji='🙄')
#     await bot.add_reaction(msg, emoji='🤔')
#     await bot.add_reaction(msg, emoji='💩')
#     await bot.add_reaction(msg, emoji='😱')
#     await bot.add_reaction(msg, emoji='😇')


# @bot.command(pass_context=True)
# async def gift(ctx, user: discord.Member):
#     """GIVES SOMEONE ELSE YOUR CREDITS """
#     try:  # GIFTING A USER YOUR CREDITS TAX = 100
#         tax = 100
#         #user setup
#         amount = 200  # GIFTING AMOUNT
#         sender_name = ctx.message.author.name  # THE PERSON GIFTING'S DISCORD NAME
#         receiver_name = user.name  # THE DISCORD USER RECEIVING THE GIFT'S NAME
#         receiver = user.id  # THE DISCORD USER RECEIVING'S ID
#         sender = ctx.message.author.id  # DISCORD USER THAT IS IS GIFTING
#         #finding user row and value
#         receiver_row = wks.find(receiver).row  # RECEIVER'S GSPREAD ROW
#         sender_row = wks.find(sender).row  # SENDER ROW
#         sender_credits = wks.cell(sender_row, 3).value  # VALUE OF CREDITS
#         receiver_credits = wks.cell(receiver_row, 3).value  # VALUE OF CREDITS
#         send_float = float(sender_credits)  # CONVERT TO FLOAT TYPE
#         receiver_float = float(receiver_credits)  # CONVERT TO FLOAT TYPE
#         tax_gift = tax+amount  # ADD TA WITH AMOUNT
#         if send_float  <=-100:
#             await bot.saay("Your credits is too low right now to gift someone")
#         elif send_float >= 100:
#             update_sender = wks.update_cell(
#                 sender_row, 3, send_float-tax_gift)  # UPDATING VALUES
#             update_receiver = wks.update_cell(
#                 receiver_row, 3, receiver_float+amount)  # UPDATING VALUES

#             try:
#                 tax_value = wks.cell(sender_row, 7).value
#                 tax_float = float(tax_value)
#                 command_tax = wks.update_cell(sender_row, 7, tax_float+tax)
#             except gspread.exceptions.CellNotFound:
#                 adding_tax = wks.update_cell(sender_row, 7, tax)
#             await bot.say("{} {} credits have been sent to {} from your credits".format(ctx.message.author.mention, amount, receiver_name))
#             await bot.say("{} credits have been removed from your account as tax.".format(tax))

#     except gspread.exceptions.CellNotFound:
#         name=user.name
#         user_id=user.id
#         tax = 25
#         await bot.say("Dscord user {} has no credits data".format(receiver_name))
#         await bot.say("Attempting to add the data")
#         adding_user = wks.append_row([name, user_id, 55.00])
#         await bot.say("The user {} now has 55.00 credits.".format(receiver_name))
#         send_id = ctx.message.author.id
#         send_row = wks.find(send_id).row
#         send_credits = wks.cell(send_row, 3).value
#         send_float = float(send_credits)
#         if send_float <= -100:
#             await bot.say("Your credits is too low to gift someone")
#         elif send_float >= 100:
#             send_update = wks.update_cell(send_row, 3, send_float-tax)
#             user_tax = wks.update_cell(send_row, 7, tax)
#             await bot.say("{} {} credits have been removed from your account as tax.".format(ctx.message.author.mention, tax))
#             try:
#                 tax_value = wks.cell(sender_row, 7).value
#                 command_tax = wks.update_cell(sender_row, 7, tax_value+tax)
#             except gspread.exceptions.CellNotFound:
#                 adding_tax = wks.update_cell(sender_row, 7, tax)


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
        url = 'https://random.dog/{}'.format(hal)
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
                if ul != 'https://random.dog':
                    await bot.say(ul)
                    break
        elif url != 'https://random.dog/':
            await bot.say(url)

    except:
        await bot.say("Command is currently not available.")


@bot.command(pass_context=True)
async def logout(ctx):
    """RESTARTS THE BOT IN HEROKU SERVER, BUT ENDS IN TERMINAL"""
    creator_id = 185181025104560128
    sender_id = ctx.message.author.id
    send_id = int(sender_id)
    if send_id == creator_id:
        await bot.say("Logging out bot now!")
        await bot.logout()
    else:
        await bot.say("Can not restart bot because you are not the creator")


@bot.command(pass_context=True)
async def dice(ctx):
    """GENERATES A RANDOM BETWEEN 1-6"""
    r = random.choice(range(1, 7))
    await bot.say("**{}**".format(r))


@bot.command(pass_context=True)
async def game(ctx):
    """CHANGES THE PLAYING STATUS OF THE BOT. EX: s.game OSU!"""
    mesg = ctx.message.content[6:]
    await bot.change_presence(game=discord.Game(name=mesg))


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    """GETS THE BASIC INFORMATION OF A USER IN DISCORD. EX: s.info @Kurusaki#4763"""
    await bot.say("The user's name is: {}\n{}'s ID is: {}\n{} is: {}\n{}'s highest role is: {}\n{} joined at: {}".format(user.name, user.name, user.id, user.name, user.status, user.name, user.top_role, user.name, user.joined_at))


@bot.command(pass_context=True)
async def catfact(ctx):
    """SENDS YOU A RANDOM FACT ABOUT CATS. EX: s.catfact"""
    url = 'https://cat-fact.herokuapp.com/facts/random?amount=1'
    rq_url = rq.get(url).text
    rq_json = json.loads(rq_url)
    await bot.say(rq_json['text'])


@bot.command(pass_context=True)
async def randomanime(ctx):
    """GENERATES A RANDOM ANIME TITLE WITH 10 SECOND COOL DOWN. EX: s.randomanime"""
    ra1 = rq.get(
        'https://private-anon-589c768a77-popcornofficial.apiary-proxy.com/random/anime')
    ra2 = rq.get('https://tv-v2.api-fetch.website/random/anime')
    if ra1.status_code == 200:
        text = ra1.text
        rq_json = json.loads(text)
        title = rq_json['title']
        anime_id = rq_json['mal_id']
        genres = rq_json['genres']
        gen = " ".join(genres[1:])
        url2 = 'https://api.jikan.moe/anime/{}/stats/'.format(anime_id)
        r2 = rq.get(url2).text
        r2j = json.loads(r2)
        summary = r2j['synopsis']
        await bot.say("**Title**: {}\n**Genres**: {}\n**Synopsis**: {}".format(title, gen, summary))


@bot.command(pass_context=True)
async def randommovie(ctx):
    """GENERATES A RANDOM MOVIE TITLE. EX: s.randommovie"""
    movie = rq.get('https://tv-v2.api-fetch.website/random/movie')
    if movie.status_code == 200:
        rest = movie.text
        rq_json = json.loads(rest)
        title = rq_json['title']
        summary = rq_json['synopsis']
        runtime = rq_json['runtime']
        genres = rq_json['genres']
        gen = " ".join(genres[1:])
        await bot.say("**Title**: {}\n**Genres**: {}\n**Length*: {} Minutes\n**Synopsis**: {}".format(title, gen, runtime, summary))


@bot.command(pass_context=True)
async def randomshow(ctx):
    url = 'https://tv-v2.api-fetch.website/random/show'
    r = rq.get(url).text
    r_json = json.loads(r)
    name = r_json['title']
    year = r_json['year']
    img = r_json['images']['poster']
    await bot.say("**Name**: {}\n**Year**: {}\n**Poster**: {}".format(name, year, img))


@bot.command(pass_context=True)
async def invite(ctx):
    """GET AN INVITE LINK FOR THIS DISCORD BOT. EX: s.invite"""
    await bot.say("Here is the invite link for {}\n{}".format(bot.user.name, 'https://discordapp.com/oauth2/authorize?client_id=403402614454353941&scope=bot'))


@bot.command(pass_context=True)
async def weather(ctx):
    """GET THE WEATHER IN YOUR CITY. EX: s.weather austin"""
    city_state = ctx.message.content[10:]
    t = u"\u00b0"
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'.format(
            city_state, owm)
        ser = rq.get(url).text
        rq_json = json.loads(ser)
        temp = rq_json['main']['temp']
        max_temp = rq_json['main']['temp_max']
        min_temp = rq_json['main']['temp_min']
        dis = rq_json['weather'][0]['description']
        wind = rq_json['wind']['speed']
        await bot.say("**Temperature** **in** **{}** **is around** {}{}F\n**Minimum Temperature is**: {}{}F\n**Maximum Temperature is**: {}{}F\n**Mainly**: {}\n**Wind speed is around**: {} **MPH**".format(city_state, temp, t, min_temp, t, max_temp, t, dis, wind))
    except:
        await bot.say("Looks like something went wrong. Your spelling may be incorrect or the bot may just be able to process this command at the moment.")


@bot.command(pass_context=True, case_insensitive=True)
async def cat(ctx):
    """GET A RANDOM PICTURE OF A CAT. EX: s.cat"""
    pictures = range(1, 1600)
    num = random.choice(pictures)
    url = 'https://random.cat/view/{}'.format(num)
    page = urllib.request.urlopen(url)
    sp = bs.BeautifulSoup(page, 'html.parser')
    pic = sp.img
    se = str(pic)
    img = se[26:-12]
    await bot.say(img)


@bot.command(pass_context=True)
async def img(ctx):
    """FAILED IMAGE GENERATOR BY KEYWORDS s.img dog"""
    query = ctx.message.content[5:]
    url = 'http://version1.api.memegenerator.net//Generators_Search?q={}&apiKey={}'.format(
        query, img_api)
    rq_link = rq.get(url).text
    rq_json = json.loads(rq_link)
    await bot.say(rq_json['result'][0]['imageUrl'])


@bot.command(pass_context=True)
async def al(ctx):
    """SEARCH FOR ANIME WITH Anilist. EX: s.al School Rumble"""
    try:
        new_msg = ctx.message.content[4:]
        search = An.search.anime(new_msg)
        episodes = search['data']['Page']['media'][0]['episodes']
        episodes_dumps = json.dumps(episodes)
        if episodes_dumps == "null":
            episodes = "Currently airing or unknown"
        else:
            episodes = episodes
        name = search['data']['Page']['media'][0]['title']['romaji']
        rank = search['data']['Page']['media'][0]['popularity']
        score = search['data']['Page']['media'][0]['averageScore']
        img = search['data']['Page']['media'][0]['coverImage']['large']
        season = search['data']['Page']['media'][0]['season']
        an = Pymoe.Anilist()
        ide = search['data']['Page']['media'][0]['id']
        a = an.get.anime(ide)
        b = json.dumps(a)
        c = json.loads(b)
        d = c['data']['Media']['description']
        e = d.replace("<br><br>", "")
        await bot.say("Anime Name: {}\nEpisodes: {}\nRank: {}\nAverage Score: {}%\nSeason: {}\nSummary: {}\n{}".format(name, episodes, rank, score, season, e, img))

    except IndexError:
        print("")
    finally:
        #if anime is not found output not found
        not_found = json.dumps(search)
        not_json = json.loads(not_found)
        if not_json['data']['Page']['pageInfo']['lastPage'] == 0:
            await bot.say("Anime {} is not found.".format(new_msg))

            
            
            
@bot.command(pass_context=True)
async def neko(ctx):
    """GENERATES A RANDOM NEKO GIRL PICTURE. Ex: s.neko"""
    url = 'https://nekos.brussell.me/api/v1/random/image?count=1&nsfw=false'
    r=rq.get(url).text
    r_json=json.loads(r)
    pic = 'https://nekos.moe/thumbnail/{}'.format(r_json['images'][0]['id'])
    await bot.say(pic)


# @bot.command(pass_context=True)
# async def mal(ctx):
#     """SEARCH FOR ANIME USING MyAnimeList. EX: s.mal Mushishi"""
#     query = ctx.message.content[5:]
#     url = 'https://api.jikan.moe/search/anime/{}/'.format(query)
#     rq_url = rq.get(url).text
#     rq_json = json.loads(rq_url)
#     anime_id = rq_json['result'][0]['mal_id']
#     url2 = 'https://api.jikan.moe/anime/{}/stats/'.format(anime_id)
#     rq_url2 = rq.get(url2).text
#     rq_json2 = json.loads(rq_url2)
#     summary = rq_json2['synopsis']
#     title_jp = rq_json2['title_japanese']
#     title_en = rq_json2['title_english']
#     anime_type = rq_json2['type']
#     status = rq_json2['status']
#     airing = rq_json2['airing']
#     aired_from = rq_json2['aired']['from']
#     aired_to = rq_json2['aired']['to']
#     episodes = rq_json2['episodes']
#     source = rq_json2['source']
#     members = rq_json2['members']
#     popularity = rq_json2['popularity']
#     rank = rq_json2['rank']
#     duration = rq_json2['duration']
#     rating = rq_json2['rating']
#     premiered = rq_json2['premiered']
#     favorites = rq_json2['favorites']
#     scored_by = rq_json2['scored_by']
#     score = rq_json2['score']
#     #anime formatting output

#     anime_picture = rq_json2['image_url']
#     embed = discord.Embed(title="Title: {}".format(
#         query), description=title_en+":"+title_jp, color=0xDEADBF)
#     embed.add_field(name="Type", value=anime_type)
#     embed.add_field(name="Status", value=status)
#     embed.add_field(name="Members", value=members)
#     embed.add_field(name="Popularity", value=popularity)
#     embed.add_field(name="Rank", value=rank)
#     embed.add_field(name="Favorites", value=favorites)
#     embed.add_field(name="Score", value=score)
#     embed.add_field(name="Scored By", value=scored_by)
#     embed.add_field(name="Aired From", value=aired_from)
#     embed.add_field(name="Rating", value=rating)
#     embed.add_field(name="Duration", value=duration)
#     embed.add_field(name="Premiered", value=premiered)
#     await bot.say(embed=embed)
#     await bot.say("**Summary**: {}\n{}".format(summary, anime_picture))



@bot.command(pass_context=True)
async def summoner(ctx):
    """GET BASIC INFO OF A GIVEN SUMMONER. EX: s.summoner Charming Mother"""
    try:
        name = ctx.message.content[10:]
        """GETS THE SUMMONER'S BASIC INFORMATION; NAME,LEVEL"""
        link = rq.get(
            "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name, api)).text
        rq_json = json.loads(link)
        await bot.say("{}is level: {}\n{}'s profile icon is: {}\n{}'s ID is : {}\n{}'s Account ID is: {}".format(rq_json['name'], rq_json['summonerLevel'], rq_json['name'], rq_json['profileIconId'], rq_json['name'], rq_json['id'], rq_json['name'], rq_json['accountId']))
    except KeyError:
        await bot.say("{} is currently unable process your command.".format(bot.user.name))


@bot.command(pass_context=True)
async def lore(ctx):
    """GETS THE LORE OF A CHAMPION GIVEN. EX: s.lore Ashe"""
    msg = ctx.message.content[6:]
    new_msg=msg.lower()
    champ = rq.get('https://na1.api.riotgames.com/lol/static-data/v3/champions/{}?locale=en_US&champData=lore&api_key={}'.format(
        champs['keys'][new_msg], api)).text
    champ_json = json.loads(champ)
    await bot.say("Champion Name: {}\nTitle: {}\nLore: {}".format(champ_json['name'], champ_json['title'], champ_json['lore']))


@bot.command(pass_context=True)
async def champmastery(ctx):
    """GET A CHAMP MASTERY OF A SUMMONER. EX: s.champmastery Charming Mother,Vayne"""
    msg = ctx.message.content[14:]
    bett = msg.find(",")
    summoner = msg[0:bett]
    cham = msg[bett+1:]
    champ=cham.lower()
    url1 = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(
        summoner, api)
    sum_info = rq.get(url1).text
    info_json = json.loads(sum_info)
    name = info_json['name']
    sum_id = info_json['id']
    url2 = "https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/{}/by-champion/{}?api_key={}".format(
        sum_id, champs['keys'][champ], api)
    mast_info = rq.get(url2).text
    mast_json = json.loads(mast_info)
    champ_lvl = mast_json['championLevel']
    champ_points = mast_json['championPoints']
    chest = mast_json['chestGranted']
    await bot.say("**Level**: {}\n**Points**: {}\n**Chest**: {}".format(champ_lvl, champ_points, chest))


@bot.command(pass_context=True)
async def masterytotal(ctx):
    """GETS THE SUMMONER'S TOTAL MASTERY POINTS. EX: s.masterytotal Charming Mother"""
    name = ctx.message.content[14:]
    link = rq.get(
        "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name, api)).text
    rq_json = json.loads(link)
    ide = rq_json['id']
    mast = rq.get(
        "https://na1.api.riotgames.com/lol/champion-mastery/v3/scores/by-summoner/{}?api_key={}".format(ide, api)).text
    await bot.say("**Points**: {}".format(mast))


@bot.command(pass_context=True)
async def status(ctx):
    no_space = ctx.message.content[8:]
    mg = "".join(no_space[1:])
    if mg == "kr":
        url = 'https://{}.api.riotgames.com/lol/status/v3/shard-data?api_key={}'.format(
            mg, api)
        r = rq.get(url).text
        r_json = json.loads(r)
        region = r_json['name']
        game = r_json['services'][0]['status']
        store = r_json['services'][1]['status']
        website = r_json['services'][2]['status']
        client = r_json['services'][3]['status']
        await bot.say("**Region**: {}\n**Game**: {}\n**Store**: {}\n**Website**: {}\n**Client**: {}".format(region, game, store, website, client))
    if mg == "ru":
        url = 'https://{}.api.riotgames.com/lol/status/v3/shard-data?api_key={}'.format(
            mg, api)
        r = rq.get(url).text
        r_json = json.loads(r)
        region = r_json['name']
        game = r_json['services'][0]['status']
        store = r_json['services'][1]['status']
        website = r_json['services'][2]['status']
        client = r_json['services'][3]['status']
        await bot.say("**Region**: {}\n**Game**: {}\n**Store**: {}\n**Website**: {}\n**Client**: {}".format(region, game, store, website, client))
    else:
        url = 'https://{}1.api.riotgames.com/lol/status/v3/shard-data?api_key={}'.format(
            mg, api)
        r = rq.get(url).text
        r_json = json.loads(r)
        region = r_json['name']
        game = r_json['services'][0]['status']
        store = r_json['services'][1]['status']
        website = r_json['services'][2]['status']
        client = r_json['services'][3]['status']
        await bot.say("**Region**: {}\n**Game**: {}\n**Store**: {}\n**Website**: {}\n**Client**: {}".format(region, game, store, website, client))


@bot.command(pass_context=True)
async def rank(ctx):
    raw_msg = ctx.message.content[6:]
    url = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}'.format(
        raw_msg, api)
    r_basic = rq.get(url).text
    basic_json = json.loads(r_basic)
    try:
        code = basic_json['status']['status_code']
        if code == 404:
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
                rank2 = r_json[1]
                q_type2 = rank2['queueType']
                wins2 = rank2['wins']
                losses2 = rank2['losses']
                total_game2 = wins2+losses2
                league_name2 = rank2['leagueName']
                division2 = rank2['rank']
                fresh_blood2 = rank2['freshBlood']
                tier2 = rank2['tier']
                points2 = rank2['leaguePoints']
                #SOLO/DUO RANK
                rank = r_json[0]
                q_type = rank['queueType']
                wins = rank['wins']
                losses = rank['losses']
                total_game = wins+losses
                league_name = rank['leagueName']
                division = rank['rank']
                fresh_blood = rank['freshBlood']
                tier = rank['tier']
                points = rank['leaguePoints']
                await bot.say("Queue Type: {}\nTier: {}\nDivision:{}\nLeague Name:{}\nPoints:{}\nWins: {}\nLosses: {}\nTotal Wins: {}\nFresh Blood: {}\n\n\n\nQueue Type: {}\nTier: {}\nDivision:{}\nLeague Name:{}\nPoints:{}\nWins: {}\nLosses: {}\nTotal Wins: {}\nFresh Blood: {}".format(q_type2, tier2, division2, league_name2, points2, wins2, losses2, total_game2, fresh_blood2, q_type, tier, division, league_name, points, wins, losses, total_game, fresh_blood))

        except IndexError:
            try:
                if r_json[0]['queueType'] == "RANKED_SOLO_5x5":
                    rank = r_json[0]
                    q_type = rank['queueType']
                    wins = rank['wins']
                    losses = rank['losses']
                    total_game = wins+losses
                    league_name = rank['leagueName']
                    division = rank['rank']
                    fresh_blood = rank['freshBlood']
                    tier = rank['tier']
                    points = rank['leaguePoints']
                    await bot.say("Queue Type: {}\nTier: {}\nDivision:{}\nLeague Name:{}\nPoints:{}\nWins: {}\nLosses: {}\nTotal Wins: {}\nFresh Blood: {}".format(q_type, tier, division, league_name, points, wins, losses, total_game, fresh_blood))
                if r_json[0]['queueType'] == "RANKED_FLEX_SR":
                    rank = r_json[0]
                    q_type = rank['queueType']
                    wins = rank['wins']
                    losses = rank['losses']
                    total_game = wins+losses
                    league_name = rank['leagueName']
                    division = rank['rank']
                    fresh_blood = rank['freshBlood']
                    tier = rank['tier']
                    points = rank['leaguePoints']
                    await bot.say("Queue Type: {}\nTier: {}\nDivision:{}\nLeague Name:{}\nPoints:{}\nWins: {}\nLosses: {}\nTotal Wins: {}\nFresh Blood: {}".format(q_type, tier, division, league_name, points, wins, losses, total_game, fresh_blood))
            except IndexError:
                await bot.say("Summoner{} has no rank".format(raw_msg))
    except:
        pass


@bot.command(pass_context=True)
async def urban(ctx):
    """USES URBAN DICT TO FIND DEFINITION OF WORDS. EX: s.urban neko"""
    word = ctx.message.content[7:]
    link = 'http://api.urbandictionary.com/v0/define?term={}'.format(word)
    rq_link = rq.get(link).text
    rq_json = json.loads(rq_link)
    await bot.say("Word: {}\nVotes: {}\nDefinitioin: {}\nExample: {}".format(rq_json['list'][0]['word'], rq_json['list'][0]['thumbs_up'], rq_json['list'][0]['definition'], rq_json['list'][0]['example']))


bot.run(bot_token)
