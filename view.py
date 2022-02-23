from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def view_data(update: Update, title, context: CallbackContext):
    update.message.reply_text(title)
    