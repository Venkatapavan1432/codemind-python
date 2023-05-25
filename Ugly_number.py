n=int(input())
t=n
while(t%2==0):
    t=t//2
while(t%3==0):
    t=t//3
while(t%5==0):
    t=t//5
if(t==1):
    print('Ugly Number')
else:
    print("Not Ugly Number")