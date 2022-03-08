import random

def randomizer(min, max):
    return random.randint(min, max)

def read_storage():
    d = {}
    with open('storage.txt', 'r') as file:
        d = {i.split(" ")[0]: " ".join(i.replace("\n", "").split(" ")[1:]) for i in file}
    return d

def logger(id):
    if not str(id) in read_storage():
        with open('storage.txt', 'a') as file:
            file.write(f'\n{str(id)} {randomizer(50, 100)}')
    d = read_storage()
    if d[str(id)] == '0':
            with open ('storage.txt', 'r') as file:  
                old_data = file.read()
                new_data = old_data.replace(f'{id} {d[str(id)]}', f'{id} {randomizer(50, 100)}')
            with open ('storage.txt', 'w') as file:  
                file.write(new_data)
    d = read_storage()
    return d[str(id)]

def change_balance(id, balans):
    if not str(id) in read_storage():
        logger(id)
    d = read_storage()
    bot_move = randomizer(1, 5)
    if (int(d[str(id)]) - balans) < 0:
        title = 'Нельзя взять конфет больше, чем их осталось!'
        result = ''
        return title, result
    elif (int(d[str(id)]) - balans) == 0:
        candies = int(d[str(id)]) - balans
        title = 'Поздравляю, ты выиграл!'
        result = True
    elif (int(d[str(id)]) - balans - bot_move) == 0:
        candies = int(d[str(id)]) - balans - bot_move
        title = f'Я взял {bot_move} шт.\nПоздравляю, ты ПРОиграл!'
        result = False
    elif (int(d[str(id)]) - balans - bot_move) < 0:
        while (int(d[str(id)]) - balans - bot_move) < 0:
            bot_move -=1
        candies = int(d[str(id)]) - balans - bot_move
        title = f'Я взял {bot_move} шт.\nПоздравляю, ты ПРОиграл!'
        result = False
    else:
        candies = int(d[str(id)]) - balans - bot_move
        title = f'Я взял {bot_move} шт.'
        result = ''
    with open ('storage.txt', 'r') as file:  
        old_data = file.read()
        new_data = old_data.replace(f'{id} {d[str(id)]}', f'{id} {candies}')
    with open ('storage.txt', 'w') as file:  
        file.write(new_data)
    return title, result