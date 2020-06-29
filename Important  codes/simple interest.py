# simple interest...
def simpleinterest(p,n,r=1.5):
    s=(p*n*r)/100
    return s
def main():
    si1=simpleinterest(5000,12)
    si2=simpleinterest(7000,24,1.7)
    print(si1)
    print(si2)
main()
