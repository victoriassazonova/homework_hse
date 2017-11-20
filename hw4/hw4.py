f = open('text.txt', encoding='utf-8')
k = 0
c = 0
for line in f:
    s = line.split()
    for i in range (len(s)):
        s[i] = len(s[i])
        c += s[i]
        if s[i] > 10:
            k += 1
ans=k/c*100
print(round(ans, 2), '%')
