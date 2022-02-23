from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from logic import *


def logger(update: Update, context: CallbackContext):
    d = {}
    with open('storage.txt', 'r') as file:
        d = {i.split(" ")[0]: " ".join(i.replace("\n", "").split(" ")[1:]) for i in file}
    if not str(update.effective_user.id) in d:
        with open('storage.txt', 'a') as file:
            file.write(f'{str(update.effective_user.id)} {randomizer()}\n')

    if str(update.effective_user.id) in d and int(d[str(update.effective_user.id)]) != 0:
        #game
    return d[str(update.effective_user.id)]

