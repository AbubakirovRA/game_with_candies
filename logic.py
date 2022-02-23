from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import telebot
import random

def randomizer():
    return random.randint(20, 50)

def game(candies, update: Update, context: CallbackContext):
    update.message.reply_text(f'{update.effective_user.first_name}, возьмите конфеты')
    


bot = telebot.TeleBot('5114113498:AAFnnrk1vvaX9nY0l_IhfXkW8hEJJtr3FZM')
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    text = message.text
    # ^^^^^^^^^^^^^^^^^
    bot.reply_to(message, text)

bot.polling()