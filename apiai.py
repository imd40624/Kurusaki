import apiai
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot=commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
  print(bot.user.name+mention=bot.user.mention)
  
  
# @bot.event
# async def on_message(message):
#   mention=bot.user.mention
#   raw_msg=message.content.split("")



import apiai
def chatbot(arg):
  client_token='5df92cae29c5452aadd286f3001112c4'
  ai=apiai.ApiAI(client_token)
  request =ai.text_request()
  request.lang= 'en'
  request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
  request.query = arg
  response = request.getresponse()
  rope = str(response.read())
  rope = rope[rope.index("speech")+10:]
  rope = rope[0:rope.index("\"")]
  print(rope)
  
chatbot("hello")
