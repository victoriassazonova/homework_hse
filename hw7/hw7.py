def file(filename):
    with open(filename+ '.txt', encoding="utf-8") as f:
            text=f.read()
            text = text.replace('.', '').replace(';','').replace(',',' ').replace('?','').replace('!','').replace(':','').replace('  ',' ')
            text = text.lower()
            words = text.split()
    return words


def adj(words):
    i=[]
    for word in words:
        if word.endswith("ous"):
          i.append(word)
 
    return len(i)
        
def dlina(words):
    l=0
    for word in words:
        if word.endswith("ous"):
            l+=len(word)
    return l


def main():
    filename = input("Введите название: ")
    print ('всего: ', adj(file(filename)), 'в среднем:' , dlina(file(filename))/adj(file(filename)))


main()





