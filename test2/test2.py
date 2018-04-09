import re

def first():
    count=0
    with open('test.xml', 'r', encoding='utf-8') as f:
        for line in f:
            count+=1
    with open('first.txt', 'w', encoding='utf-8') as t:
        count=str(count)
        t.write(count) 
    return count

def second():
    d = {}
    with open('test.xml', 'r', encoding='utf-8') as f:
        for line in f:
            word=re.search('<w lemma="[^"]+" type="([^"]+)', line)
            if word!=None:
                wword=word.group(1)
                if wword in d.keys():
                    d[wword]+=1
                else:
                    d[wword]=1
    with open('second.txt', 'a', encoding='utf-8') as w:
        for key in d:
            print(key, file=w)
    return d

def third(d):
    with open('second.txt', 'r', encoding='utf-8') as c:
        for line in c:
            word=re.search('(l.f\w+)', line)
            if word!=None:
                wword=word.group(1)
            kol=d.get(word)
            print (word)
            print (kol)

first()
second()
third(second())

