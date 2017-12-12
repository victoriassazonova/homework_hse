f = open('Extinct_languages.tsv', encoding='utf-8')
for line in f:
    if (len(line))>35:
        print(line)
        
f = open('Extinct_languages.tsv', encoding='utf-8')
k=0      
for line in f:
    if "Critically endangered" in line:
        k+=1
print ("Critically endangered languages:",k)

f = open('Extinct_languages.tsv', encoding='utf-8')
arc = []
word = input('Language: ')
if word == '':
    print('empty')
else:
    text=f.read()
    if word in text:
        arc.append(word + ' ')
    word = input()
    if word not in text:
        print('Not in file')
    word = input()
    
s=arc[1:1]
for line in f:
    if s in line:
        k = line.split( )
        for m in range (len(k)):
            print('name',m)
            m+=1
            print('number',m)
            m+=1
            print('status',m)
arc=arc[2:] 

