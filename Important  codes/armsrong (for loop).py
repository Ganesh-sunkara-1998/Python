# Armstrong using for loop......
n=int(input("Enter your numbers:-"))
s=0
t=n
for i in range(1,n+1):
    
    r=n%10
    s=s+(r**3)
    n=n//10
    
if t==s:
    print("Armstrong number is:-",t)
else:
    print("Armstrong number is :-",t)
