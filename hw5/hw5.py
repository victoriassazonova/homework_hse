arc = []
word = input('Latin word: ')
if word == '':
    print('empty')
else:
    while word != '':
        if word.endswith('tur') and not word.endswith('batur'):  #больше постоянных различий прошедшего пассива отнастоязего я не нашла
            arc.append(word + '\n')
        word = input()
with open('text.txt', 'w', encoding='utf-8') as f:
    f.writelines(arc)
