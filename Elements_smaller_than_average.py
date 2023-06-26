n=int(input())
a=list(map(int,input().split()))
c=0
av=sum(a)//n
for i in a:
    if(av>=i):
        c+=1
print(c)