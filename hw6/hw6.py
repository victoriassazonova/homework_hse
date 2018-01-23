import random


def noun():
    return random.choice([line for line in open('noun.txt', 'r', encoding='utf-8')])[:-1]

def noun2():
    return random.choice([line for line in open('noun2.txt', 'r', encoding='utf-8')])[:-1]

def adv():
    b=random.randint(0, 1)
    if b==1:
        return random.choice([line for line in open('adv.txt', 'r', encoding='utf-8')])[:-1] +' '
    else:
        return ''

def yesno():
    a=random.randint(0, 1)
    if a == 1:
        return ''
    else:
        return 'не'
    
def verb():
    return random.choice([line for line in open('verb.txt','r', encoding='utf-8')])[:-1]

def pron():
    return random.choice([line for line in open('pron.txt', 'r', encoding='utf-8')])[:-1]

def random_sentence():
    sentence = noun() + ' ' + adv() + yesno() + ' '+ verb() + ',' + ' ' + pron() + ' ' + noun2()+ ' ' + adv() + yesno() + ' ' + verb() + '.'
    return sentence

m=int(input('введите максимальное количество предложений (мин 5): ')) #что-то я торможу и никак не придумаю, как еще сделать "не меньше 5", а не ровно 5 
n=random.randint(5, m)
for i in range(n):
    sentence = random_sentence() 
    sentence = sentence.capitalize()
    print(sentence, end=' ') 
