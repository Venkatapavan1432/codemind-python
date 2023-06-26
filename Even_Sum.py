n=int(input())
a=list(map(int,input().split()))
sum=0
for i in a:
    if(i%2==0):
        sum=sum+i
print(sum)