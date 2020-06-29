'''write a program to create a lambda function that adds 15 to a given number
passed in as an argument... '''

print(" for additions")
def main():
    s=lambda x: x+15
    x=int(input("Enter your number:-"))
    r=s(x)
    print(r)
main()


'''also create a lambda function that multiplies argument
x with y argument print the result...'''
print("for multiplications:-")

def main():
    d=lambda a,b:a*b
    a=int(input("Enter your first number:-"))
    b=int(input("Enter your second number:-"))
    c=d(a,b)
    print(c)
main()

