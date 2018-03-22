#съесть, съесться, съеденный, съевший и все их формы
#съем съешь съест съедим съедите съедят +ся


import re

def file():
    with open('text.txt', encoding="utf-8") as f:
            text=f.read()
            text = text.replace('.', '').replace(';','').replace(',',' ').replace('?','').replace('!','').replace(':','').replace('  ',' ')
            text = text.lower()
            words = text.split()
    return words

def search(words):
    k=[]
    for word in words:
           w = re.match('съе[вмшд(ст)]', word) 
           if w != None:
               v = re.search('(съестн..)', word)
               if v == None:
                   b = re.search('съедем', word)
                   if b == None:
                       с = re.search('съедет', word)
                       if с == None:
                           if k.count(word) == 0:
                               k.append(word)
    print('\n'.join(k))

search(file())

#match должен исключать всякие варианты типа несъеденный
#а другие проверки - для слов, которые я смогла придумать, которые не должны попасть но попали бы - съестной и съедем, съедет
