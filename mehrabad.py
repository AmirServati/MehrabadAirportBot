#Mehrabad Telegram Bot

from telegram.ext import Updater, MessageHandler, Filters
from telegram import ParseMode
from emoji import emojize
import os
TOKEN = "992894946:AAHrFRfhetVL4dhlE_xjFJgJ75VWDYRC_ss"

def caption(bot, update):
    try:
        content = update.message.text   #for video / photo
    except:
        content = update.message.caption    #for plain text
    finally:
        pass
    bot.send_message(text=content, chat_id=112137855)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.caption, caption))

#updater.start_polling()
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                     url_path=TOKEN)
updater.bot.setWebhook("https://mehrabadairport.herokuapp.com/" + TOKEN)
updater.idle()
