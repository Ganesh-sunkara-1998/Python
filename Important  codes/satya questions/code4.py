''' write a python program to get the difference between the number and 17,
if the number is greater than the 17 it'll double or if the nunmber is less than
the 17 it returns the absolute number (postive number)...'''
def num(x,y=17):
    if x>y:
        z=x-y
        print(z*2,"The number is doubled")
    else:
        z=x-y
        print(-z)
def main():
    x=int(input("Enter your number:-"))
    num(x)
main()
    
    
