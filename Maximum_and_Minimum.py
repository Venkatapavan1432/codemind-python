n=int(input())
a=list(map(int,input().split()))
p=set(a)
c=0
s=[]
for i in p:
    c=0
    for j in a:
        if(i==j):
            c+=1
    if(i==c):
        s.append(i)
if(len(s)==0):
    print('-1')
else:
    print(min(s),max(s),sep=' ')