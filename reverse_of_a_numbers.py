n=int(input())
t=n
rev=0
while(t!=0):
    r=t%10
    rev=rev*10+r
    t=t//10
print(rev)