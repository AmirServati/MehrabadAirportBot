#Mehrabad Telegram Bot

from telegram.ext import Updater, MessageHandler, Filters
from telegram import ParseMode
from emoji import emojize
import os
TOKEN = "992894946:AAHrFRfhetVL4dhlE_xjFJgJ75VWDYRC_ss"
PORT = int(os.environ.get('PORT', '5000'))
CHANNEL_LINK = "[Mehrabad Airport](https://t.me/mehrabad_airport)"

def caption(bot, update):
    message_id  = update.effective_message.message_id
    try:
        #plain text
        content     = update.effective_message.text
        bot.sendMessage(text=content,
                        chat_id="@amirstestchannel",
                        parse_mode=ParseMode.MARKDOWN)
    except:
        content     = update.effective_message.caption
    if "Mehrabad Airport" in content:
        content = content.replace("Mehrabad Airport", CHANNEL_LINK)

    else:
        content = content + "\n\n" + CHANNEL_LINK

    try:
        bot.editMessageText(text=content,
                        chat_id="@amirstestchannel",
                        message_id=message_id,
                        parse_mode=ParseMode.MARKDOWN)
    except:
        bot.editMessageCaption(caption=content,
                        chat_id="@amirstestchannel",
                        message_id=message_id,
                        parse_mode=ParseMode.MARKDOWN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.all, caption))


#updater.start_polling()
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                     url_path=TOKEN)
updater.bot.setWebhook("https://mehrabadairport.herokuapp.com/" + TOKEN)
updater.idle()
