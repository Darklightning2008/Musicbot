import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import youtube_dl

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the YouTube downloader
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'noplaylist': True,
}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I am a music bot. Send me the name of a song or a YouTube link to play it.")

def play(update: Update, context: CallbackContext) -> None:
    query = " ".join(context.args)

    if not query:
        update.message.reply_text("Please provide the name of a song or a YouTube link.")
        return

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(query, download=False)
            if 'entries' in info_dict:
                info_dict = info_dict['entries'][0]
            video_url = info_dict['url']
            update.message.reply_text(f"Playing: {info_dict['title']}")
            update.message.reply_audio(audio=video_url)

    except Exception as e:
        update.message.reply_text("An error occurred while trying to play the song.")

def main():
    # Replace 'YOUR_TOKEN' with your actual bot token
    updater = Updater("6228213035:AAG1oLG3aP4f3Axb_6tHuLERhffK9Uhbt6I")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("play", play))
    
    # Add additional handlers here if needed

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

