n=int(input())
a=input()
c=0
for i in a:
    if(i=='1' or i=='0'):
        c+=1
print(c==n)