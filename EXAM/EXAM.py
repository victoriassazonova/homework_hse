import csv
import re
import os

#Создайте csv-таблицу с полями "doc_id", "title",
#"author", "created", "topic", "tagging"
#с информацией о всех статьях (см. тег meta).

#пока непонятно куда это
with open("exam.csv", "w", newline='') as csv_file: 
    writer = csv.writer(csv_file)
    writer.writerow(['doc_id', 'title', 'author', 'created', 'topic', 'tagging'])

def first():
    for roots, dirs, files in os.walk('.'):
        for file in files:
            with open (file, 'r', encoding ='windows-1251') as t:
                for line in t:
                   a = re.search('name="docid"', line)
                   if a:
                       doc = re.search('content="([A-Za-z1234567890.]+)"', line)
                       if doc!=None:
                          doc=doc.group(1)
                          print (doc)
                   else:
                       b = re.search('name="header"', line)
                       if b:
                           tit = re.search('content="[a-zA-Z0-9а-яА-Я]*"', line)
                           if tit!=None:
                               tit=tit.group(1)
                               print (tit)
                           else:
                               c = re.search('name="author"', line)
                               
def second():
    d = {}
    for roots, dirs, files in os.walk('.'):
        for file in files:
            with open (file, 'r', encoding ='windows-1251') as t:
                for line in t:
                    r = re.search('[А-Я]{2,}', line)
                    if r:
                        word = r.group(0)
                        if word in d:
                            d[word] += 1
                        else:
                            d[word] = 1

                for word in sorted (d, key = d.get, reverse = True):
                    print('{}\t{}'.format(word, d[word])) #записать не успеваю
    

                               
def main():
 #   first()
 second()

main()
                               

 #       c = re.search('name="author"', line)
 #       d = re.search('name="created"', line)
 #       e = re.search('name="topic">', line)
 #       f = re.search('name="tagging"', line)
 #       writer.writerow(


