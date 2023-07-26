python music_bot.py



import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set your Telegram Bot API token here
TOKEN = "6228213035:AAG1oLG3aP4f3Axb_6tHuLERhffK9Uhbt6I"

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variable to store the audio file URL
audio_url = None

# Command handlers

def start(update: Update, _: CallbackContext):
    update.message.reply_text("Welcome to the Music Player Bot! Send /help for available commands.")

def help_command(update: Update, _: CallbackContext):
    help_text = "Available commands:\n\n" \
                "/play - Play a song (send the audio file)\n" \
                "/stop - Stop the currently playing song\n" \
                "/help - Show this help message"
    update.message.reply_text(help_text)

def play_audio(update: Update, _: CallbackContext):
    global audio_url
    if update.message.audio:
        audio_file = update.message.audio.get_file()
        audio_url = audio_file.file_path
        update.message.reply_text("Now playing...")
    else:
        update.message.reply_text("Please send an audio file to play.")

def stop_audio(update: Update, _: CallbackContext):
    global audio_url
    audio_url = None
    update.message.reply_text("Playback stopped.")

def error(update: Update, _: CallbackContext):
    logger.warning(f"Update {update} caused an error.")

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("play", play_audio))
    dp.add_handler(CommandHandler("stop", stop_audio))

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()
updater.start_polling(poll_interval=1.0)

if __name__ == '__main__':
    main()
