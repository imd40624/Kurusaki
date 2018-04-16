import apiai
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot=commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
  print(bot.mention)
  print(bot.user.name)
  
  
  
  
  
# @bot.event
# async def on_message(message):
#   mention=bot.user.mention
#   if message.content.startswith(mention):
#     raw_msg=message.content.split(mention)
#     msg="".join(raw_msg[1:])
#     client_token='5df92cae29c5452aadd286f3001112c4'
#     ai=apiai.ApiAI(client_token)
#     request =ai.text_request()
#     request.lang= 'en'
#     request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
#     request.query = msg
#     response = request.getresponse()
#     rope = str(response.read())
#     rope = rope[rope.index("speech")+10:]
#     rope = rope[0:rope.index("\"")]
#     await bot.say(rope)

# def chatbot(arg):
#   client_token='5df92cae29c5452aadd286f3001112c4'
#   ai=apiai.ApiAI(client_token)
#   request =ai.text_request()
#   request.lang= 'en'
#   request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
#   request.query = arg
#   response = request.getresponse()
#   rope = str(response.read())
#   rope = rope[rope.index("speech")+10:]
#   rope = rope[0:rope.index("\"")]
#   print(rope)
  
# chatbot("hello")

bot.run('NDA1OTA3MzI2MDUxMDI0OTA2.DbaJsg.y5RgLat4y2295thK2ftjkd6EJkQ')
