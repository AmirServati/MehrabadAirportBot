#Mehrabad Telegram Bot

from telegram.ext import Updater, MessageHandler, Filters
from telegram import ParseMode
from emoji import emojize
import os
TOKEN = "992894946:AAHrFRfhetVL4dhlE_xjFJgJ75VWDYRC_ss"
PORT = int(os.environ.get('PORT', '5000'))
CHANNEL_LINK = "[Mehrabad Airport](https://t.me/mehrabad_airport)"

def caption(bot, update):
    try:
        content = update.message.text   #for plain text
    except:
        content = update.message.caption    #for video / photo
    finally:
        pass
    if "Mehrabad Airport" in content:
        content = content.replace("Mehrabad Airport", CHANNEL_LINK)
    else:
        content = content + "\n\n" + CHANNEL_LINK
    bot.send_message(text=content, chat_id="@amirstestchannel", parse_mode=ParseMode.MARKDOWN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.text, caption))


#updater.start_polling()
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                     url_path=TOKEN)
updater.bot.setWebhook("https://mehrabadairport.herokuapp.com/" + TOKEN)
updater.idle()
