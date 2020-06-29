# find the power of the number...
def power(n,p):
    r=1
    for i in range(p):
        r=r*n
    return r
def main():
    res=power(10,2)
    print(res)
    res=power(5,4)
    print(res)
main()
