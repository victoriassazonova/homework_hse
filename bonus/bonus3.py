pyg = 'ay'
vvod = input('Введите слово(латиницей):')
if len(vvod)> 0:
    slovo = vvod.lower()
    bukva = slovo[0]
    if bukva == 'a' or 'i' or 'u' or 'o' or 'e'or 'y':
        vivod = slovo + pyg
        print (vivod)
    else:
        bukva_new = slovo[1]
        if bukva_new == 'y' or 'a' or 'u' or 'i' or 'o' or 'e':
            print (slovo[1:] + bukva + pyg)
        else:
            print (slovo[2:] + bukva + bukva_new + pyg)
else:
    print('Пустое')
