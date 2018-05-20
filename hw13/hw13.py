import os

#сколько в этих папках встречается разных названий файлов без учёта расширений; 

def nazv():
    names=[]
    for root, dirs, files in os.walk('.'):
        for file in files:
            filename, filetype = os.path.splitext(file)
            if filename not in names:
                names.append(filename)
    return names

def count(names):
    c=0
    for i in names:
        c+=1
    c-=1    #выдает на 1 больше
    return c

def main(c):
    print (c)

main(count(nazv()))
