n=int(input())
a=list(map(int,input().split()))
sum1=0
sum2=0
for i in a:
    if(i%2==0):
        sum1=sum1+i
    else:
        sum2=sum2+i
print(abs(sum1-sum2))