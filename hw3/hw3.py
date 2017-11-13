word=list(input())
word1=[]
n=len(word)-1
for i in range (n+1):
    print(''.join(word[n:]))
    n-=1
