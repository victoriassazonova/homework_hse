import random

def create():
    d = {}
    with open('zagadki.csv', 'r', encoding='utf-8') as f:
        for line in f:
            line=line.replace('\n', '')
            word, hint=line.split(' ')
            d[word] = hint
    return d

def game():
    count=0
    puzzle = random.choice(list(create().keys()))
    print ('Добро пожаловать в игру! Сейчас вам будет предложено угадать слово по подсказке:')
    print(create()[puzzle], '.....')
    varik=input('Вариант: ')
    while varik.lower()!=puzzle:
        count+=1
        print('Не верно! Сделано попыток: ', count)
        varik = input('Вариант: ')
    count+=1
    if count==1:
        print('Верно! Вы молодец! Угадано с первой попытки.')
    else:
        print('Верно! Вы молодец! Угадано с', count,'попыток.')
    print ('Сыграете еще? Введите да/нет')
    da = input()
    if da == 'да'or'Да'or'ДА':      #да, нормально через lower слишком нормально
        game()
        
game()
        
