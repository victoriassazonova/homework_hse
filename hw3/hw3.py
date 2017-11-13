word=list(input('введите слово:'))
n=len(word)-1
for i in range (n+1):
    print(''.join(word[n:]))
    n-=1
