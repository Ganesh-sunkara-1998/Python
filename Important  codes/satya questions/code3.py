# write a python function to check whether a number is perfect or not..

def num(n1,n2,n3):
    n4=n1+n2+n3
    print(n4,"postive divisiors")
    n5=n1+n2+n3+n4
    if n5%2==0:
        print(n4,"The number is perfect number")
    else:
        print(n4,"The number is not perfect number")
        
def main():
    n1=int(input("Enter your number:-"))
    n2=int(input("Enter your number:-"))
    n3=int(input("Enter your number:-"))
    num(n1,n2,n3)
main()
 
