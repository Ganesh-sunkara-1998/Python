''' functions takes an arguments takes a number and that towards number
how many even number are there (or) that number less than
how many numbers are even'''
# Asked in zetamine labs.....
def fun(n):
    count=0
    for i in range(1,n+1):
        
        if i%2==0:
            print("the number is even",i)
            count+=1
        else:
            print("the number is odd",i)
    print("how many even numbers are their is:-", count)

def main():
    n=int(input("enter your number:-"))
    fun(n)
main()    
