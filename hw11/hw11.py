import re


def search():
    with open('dino.txt', 'r', encoding='utf-8') as f:
        for line in f:
            result = re.sub('динозавр', 'кот', line)
            sresult = re.sub('Динозавр', 'Кот', result)
            tresult = re.sub('Диноза́вры', 'Коты́', sresult)
            with open('cat.txt', 'a', encoding='utf-8') as t:
                t.write(tresult) 
            
search()

#я не стала делать проверку на прилагательные от этого слова и тд,
#потому что от слова динозавр никаких форм кроме его падежей и чисел не образуется
#(во всяком случае насколько мне известно)
#я не поняла, тхт или хтмл скачивать, но работает одинаково

        


