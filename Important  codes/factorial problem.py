''' factorial program....'''
def factorial (num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

def main():
    res=factorial (3)
    print(res)
main()
