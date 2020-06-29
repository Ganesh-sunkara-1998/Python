#fibonnaci series...
nterms=int(input("enter how many integers:-"))
count=0
n1=0
n2=1
if nterms<=0:
    print("invalid input please enter positive numbers")
elif nterms==1:
    print("fabbonice series upto",nterms,":")
else:
    print("fabbonice series upto",nterms,":")
    while count<nterms:
        print(n1,end=',')
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
