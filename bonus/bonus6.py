h=int(input('Введите рост(см): '))
w=int(input('Введите вес(кг): '))
m=h/100
i=w/m**2
print(round(i, 2))
if i<16:
    print('Выраженный дефицит массы тела')
if 18.5>=i>=16:
    print('Недостаточная (дефицит) масса тела')
if 24.99>=i>18.5:
    print('Норма')
if 30>=i>=25:
    print('Избыточная масса тела (предожирение)')
if 35>=i>30:
    print('Ожирение первой степени')
if 40>=i>35:
    print('Ожирение второй степени')
if i>40:
    print('Ожирение третьей степени (морбидное)')
