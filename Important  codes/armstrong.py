# armstrong numbers.....(while loop using).....
n=int(input("enter your numbers:-"))
t=n
s=0
while n!=0:
    r=n%10
    s=s+(r**3)
    n=n//10
if t==s:
    print("The number is Armstrong:-",t)
else:
    print("The number is not an Armstrong:-",t)
