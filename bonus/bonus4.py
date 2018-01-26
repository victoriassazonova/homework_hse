s = 'с'
vvod = input('Введите слово(русское):')
vivod=str()
while len(vvod)> 0:
    bukva = vvod[0]
    if bukva == 'о' or 'и' or 'а' or 'у' or 'е' or 'э' or 'ю' or 'я' or 'ы':
        vivod = vivod+bukva+s+bukva
    else:
        vivod = vivod + bukva
    vvod=vvod[1:]
print (vivod)
