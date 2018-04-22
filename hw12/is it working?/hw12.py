import re
import os

#словом буду считать что-то, разделенное пробелом

def poisk():
    papki = []
    for folder in os.listdir():
        dirpath, filename = os.path.split(folder)
        r = re.search('[\S]+\s[\S]+', filename)
        if r!=None:
            papki.append(filename)
    return papki
            
def howmuch(papki):
    if len(papki)==1:
        print('Найдено', len(papki), 'папка:')
    if len(papki)<5:
        print('Найдено', len(papki), 'папки:')
    if len(papki)>4:
        print('Найдено', len(papki), 'папок:')
    for i in papki:
        print(i)

            
def main():
    howmuch(poisk()) 

main()
