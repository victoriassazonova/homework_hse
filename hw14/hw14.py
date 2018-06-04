import re


def read():
    with open('text.txt', 'r', encoding='utf-8') as f:
        file = f.read()
    return file

def sent(file):
    split_regex = re.compile(r'[.|!|?|…]')
    sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(file)])
    return sentences
         

def pr(sentences):
    for i in sentences:
        words = i.split()
        for word in words:
            d={}
            word1=word
            for c in word1:
                k=word.count(c)
                word1=word.replace(c, c*k)
            print(word1)
            
#я вижу, что оно не работает, но не знаю как это изменить
                
print(pr(sent(read())))


