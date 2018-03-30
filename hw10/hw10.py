import re

def search():
    with open('Кокос.html', 'r', encoding='utf-8') as f:
        for line in f:
            first=re.search('Семейство:&#160;<[^>]+><[^>]+><[^>]+>([A-яё]+)', line)
            if first!=None:
                fam=first.group(1)
                return fam
            
def main(fam):
        with open('fam.txt', 'w', encoding='utf-8') as t:
            theline = 'Семейство: ' + fam
            t.write(theline)

main(search())


        


