# find out mean and median of the number:-
list=[]
n=int(input("enter how many integers:-"))
for i in range(n):
    a=int(input("enter any integer:-"))
    list.append(a)
s=0
num=0
for value in list:
    s=s+value/n
    if n%2==0:
        num=n/2
    else:
        num=(n+1)/2
    print(list)
    print("mean:-",s)
    print("median:-",num)
