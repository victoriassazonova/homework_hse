aig = 'aig'
vvod = input('Введите слово(латиницей):')
vivod=str()
while len(vvod)> 0:
    bukva = vvod[0]
    if bukva == 'a' or 'i' or 'u' or 'o' or 'e' or 'y':
        vivod = vivod+bukva
    else:
        vivod = vivod + bukva + aig 
    vvod=vvod[1:]
print (vivod)
