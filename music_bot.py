import logging
from telegram.ext import Updater, CommandHandler

# Set up logging (optional, but useful for debugging)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Replace 'YOUR_BOT_TOKEN' with the token you obtained from BotFather
TOKEN = '6228213035:AAG1oLG3aP4f3Axb_6tHuLERhffK9Uhbt6I'
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

updater.start_polling()
updater.idle()
