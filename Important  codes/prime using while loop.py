#prime numbers.....
n=int(input("enter your number:-"))
i=1
count=0
while i<=n:
    if n%i==0:
        count+=1
    if count>2:
        break
    i+=1
if count==2:
    print(n,"number is prime")
else:
    print(n, "number is not a prime")
    
