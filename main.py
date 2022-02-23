import imp
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import controller
from commands import *


updater = Updater('5114113498:AAFnnrk1vvaX9nY0l_IhfXkW8hEJJtr3FZM')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('start', start))

print('server start')
updater.start_polling()
updater.idle()
