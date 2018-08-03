import telegram
import time
my_token = '681269723:AAERDY17ax7FdjWYf2sXXqd7abHrkk3uqgU'

bot = telegram.Bot(token = my_token)

updates = bot.getUpdates()

for u in updates :
    print(u.message)

while 1:
    time.sleep(10)
