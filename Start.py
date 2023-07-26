import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from BotFather
TOKEN = '6228213035:AAG1oLG3aP4f3Axb_6tHuLERhffK9Uhbt6I'

# Replace 'YOUR_IMAGE_URL' with the URL of the image you want to send
IMAGE_URL = 'https://te.legra.ph/file/f0ba1c3bd3ea3245bdb81.jpg'

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=IMAGE_URL,
        caption=f"Hello, {user.first_name}!\nWelcome to your Telegram Bot.\nFeel free to explore!",
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add a command handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Add a fallback handler for unknown commands
    dp.add_handler(MessageHandler(Filters.command, unknown))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C
    updater.idle()
updater.start_polling(poll_interval=1.0)

if __name__ == '__main__':
    main()
