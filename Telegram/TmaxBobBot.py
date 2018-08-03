import time
import telepot
from datetime import datetime
from telepot.loop import MessageLoop
import requests
import sys
bot = telepot.Bot('681269723:AAERDY17ax7FdjWYf2sXXqd7abHrkk3uqgU')


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        if msg['text'] == 'hi':
            bot.sendMessage(chat_id, 'hello')
        elif msg['text'] == 'boring':
            bot.sendMessage(chat_id, 'Update Me!')
        else:
            bot.sendMessage(chat_id, "I don\'t know who you are, I don\'t know what you want. But,"
                            "I will Kill you")



bot.message_loop(handle)

while 1:
    time.sleep(10)



