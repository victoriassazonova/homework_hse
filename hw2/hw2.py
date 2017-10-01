# пятый вариант
s=input()
l=len(s)
k=l//2
for i in range (k):
    print(s[i])
for i in range (l-1,k-1,-1):
    print(s[i])
