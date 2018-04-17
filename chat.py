@bot.event
async def on_message(message):
    mention = bot.user.mention
    if message.content.startswith(mention):
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
        await bot.send_message(message.channel, rope)
