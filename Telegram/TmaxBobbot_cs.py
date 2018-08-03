import time
import telepot
from datetime import datetime
from telepot.loop import MessageLoop
import requests
import sys
import chatclient
bot = telepot.Bot('681269723:AAERDY17ax7FdjWYf2sXXqd7abHrkk3uqgU')

def cs_client(content_type, chat_type, chat_id, msg):
    server = "127.0.0.1"

    port = 1024
    botname = ""
    user = chat_id
    s = msg['text']

    if s == "":
        s = " "

    message = u'%s\u0000%s\u0000%s\u0000' % (user, botname, s)
    message = str.encode(message)

    resp = chatclient.sendAndReceiveChatScript(message, server=server, port=port)

    if resp is None:
        resp = "Error communicating with chat server"

    return resp


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    print(content_type, chat_type, chat_id)

    if content_type =='text':
        resp = cs_client(content_type, chat_type, chat_id, msg)
        bot.sendMessage(chat_id, resp)

#    if content_type == 'text':
#        if msg['text'] == 'hi':
#            bot.sendMessage(chat_id, 'hello')
#        elif msg['text'] == 'boring':
#            bot.sendMessage(chat_id, 'Update Me!')
#        else:
#            bot.sendMessage(chat_id, "I don\'t know who you are, I don\'t know what you want. But,"
#                            "I will Kill you")

bot.message_loop(handle)

while 1:
    time.sleep(10)



