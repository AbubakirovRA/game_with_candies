from asyncio import log
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from log import *
from logic import *

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Есть 50 конфет. Игроки по очереди берут от 1 до 5 конфет. '\
    'Выигрывает тот, кто забрал последнюю.')
    update.message.reply_text('Для запуска игры наберите /start')

def start(update: Update, context: CallbackContext):
    update.message.reply_text(f'Осталось {logger(update, context)} конфет')