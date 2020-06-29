''' write a python program to calculate the sum of three given numbers,
if the values are equal then return thrice of their sum:- '''
n1=int(input("Enter your first number:-"))
n2=int(input("Enter your second number:-"))
n3=int(input("Enter your third number:-"))
if n1==n2==n3:
    n4=n1*3
    print("Numbers are equal:-",n4)
else:
    n5=n1+n2+n3
    print("Number are not equal:-",n5)
