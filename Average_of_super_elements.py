n=int(input())
a=list(map(int,input().split()))
p=set(a)
c=0
s=0
m=0
for i in p:
    c=0
    for j in a:
        if(i==j):
            c+=1
    if(i==c):
        s=s+i
        m+=1
if(s==0):
    print('-1')
else:
    print("%.2f"%(s/m))