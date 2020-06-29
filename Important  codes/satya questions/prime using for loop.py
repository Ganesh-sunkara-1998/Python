# prime number uisng for loop....
n=int(input("enter your number:-"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print(n,"the number is  prime")
else:
    print(n, "the number is not a prime")
    
      
