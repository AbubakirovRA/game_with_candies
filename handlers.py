import telebot
import parser
import config, logic

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_handler(message):
    id = message.chat.id
    bot.send_message(id, f'Осталось {logic.logger(id)} конфет')
    bot.send_message(id, f'{message.chat.first_name}, твоя очередь брать конфеты (не более 5 штук)')

@bot.message_handler(commands=['help'])
def help_handler(message):
    id = message.chat.id
    bot.send_message(id, f'Этот бот играет в игру "Возьми конфету". \nИгра очень простая: нужно по очереди брать конфеты из кучки, \nкто заберет последнюю - тот и выиграл. \nПравило одно: за один ход можно брать не больше пяти конфет, и не меньше одной. \nКоличество конфет задается случайно из диапазона от 50 до 100. \nЧтобы начать игру наберите /start.')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    id = message.chat.id
    if text == "привет":
        bot.send_message(id, 'Привет, я бот игры "Возьми конфету".\nДавай поиграем?')
    elif text == "как дела?":
        bot.send_message(id, 'Хорошо, а у тебя?')
    elif text == "давай":
        bot.send_message(id, 'Правила знаешь? \nЕсли да - набери /start. \nЕсли хочешь прочитать правила набери команду /help.')        
    elif text == "1":
        balans = int(text)
        title, result = logic.change_balance(id, balans)
        if result == True:
            bot.send_message(id, f'{title}\nДавай еще партейку?')
        elif result == False:
            bot.send_message(id, f'{title}\nДавай еще партейку?')
        else:
            bot.send_message(id, title)
            start_handler(message)
    elif text == "2":
        balans = int(text)
        title, result = logic.change_balance(id, balans)
        if result == True:
            bot.send_message(id, f'{title}\nДавай еще партейку?')
        elif result == False:
            bot.send_message(id, f'{title}\nДавай еще партейку?')
        else:
            bot.send_message(id, title)
            start_handler(message)
    elif text == "3":
        balans = int(text)
        title, result = logic.change_balance(id, balans)
        if result == True:
            bot.send_message(id, f'{title}\nДавай еще партейку?')
        elif result == False:
            bot.send_message(id, f'{title}\nДавай еще партейку?')
        else:
            bot.send_message(id, title)
            start_handler(message)
    elif text == "4":
        balans = int(text)
        title, result = logic.change_balance(id, balans)
        if result == True:
            bot.send_message(id, f'{title}\nДавай еще партейку?')
        elif result == False:
            bot.send_message(id, f'{title}\nДавай еще партейку?')
        else:
            bot.send_message(id, title)
            start_handler(message)
    elif text == "5":
        balans = int(text)
        title, result = logic.change_balance(id, balans)
        if result == True:
            bot.send_message(id, f'{title}\nДавай еще партейку?')
        elif result == False:
            bot.send_message(id, f'{title}\nДавай еще партейку?')
        else:
            bot.send_message(id, title)
            start_handler(message)
    else:
        bot.send_message(id, 'Простите, я вам не понял :(')

print('server start')
bot.polling()