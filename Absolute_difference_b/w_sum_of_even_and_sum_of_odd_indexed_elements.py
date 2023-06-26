n=int(input())
a=list(map(int,input().split()))
sum1=0
sum2=0
for i in range(n):
    if(i%2==0):
        sum1=sum1+a[i]
    else:
        sum2=sum2+a[i]
print(abs(sum1-sum2))