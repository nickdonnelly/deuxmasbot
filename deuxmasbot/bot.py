# This is is the main bot file.

# Standard
import logging

# External
import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler

# Internal
from settings import BOT_TOKEN
from image import stitcher
from wand.image import Image
from io import BytesIO

# Get a bot and an updater
bot = telegram.Bot(token=BOT_TOKEN)

updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher

# Set up the logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

'''
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='It is working')
'''
def echo(bot, update):
    prof_img = bot.get_user_profile_photos(update.message.from_user.id, limit=1).photos[0]
    f = bot.get_file(prof_img[0])
    downloaded = f.download()
    s = stitcher.ImageStitcher('images/stocking-base.png', [(10, 10)])
    s.draw_sprite(Image(filename=downloaded))
    bio = BytesIO()
    bio.name = "imagetest.png"
    s.image.save(bio)
    bio.seek(0)
    bot.send_photo(update.message.chat_id, photo=bio)

'''
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)
'''
echo_handler = MessageHandler(Filters.group, echo)
dispatcher.add_handler(echo_handler)

def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)


inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

updater.start_polling()
