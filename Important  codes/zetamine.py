'''Use two arguments in a function and find out odd numbers between two arguments.'''
# question from my friend (ramakrishna ) to the interviwer...
def func(a,b):
    count=0
    for i in range(a, b+1):
        if i%2==0:
            print("the number is even:-",i)
        else:
            print("the number is odd",i)
            count+=1
    print("how many odd nummbers are their:-",count)
def main():
    a=int(input("Enter your number:-"))
    b=int(input("Enter your number:-"))
    func(a,b)
main()
    
