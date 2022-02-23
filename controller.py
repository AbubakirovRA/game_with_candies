from commands import *
from logic import *
from view import *
from log import *
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def button_click(update: Update):
    title = (f'{update.effective_user.first_name}, это игра с конфетами. Для вывода правил и начала игры введите /start')