''' write a python program to get the fibbonocci series between 0 to 50
expected output :- 1 1 2 3 5 8 13 21 34...'''
nterms=int(input("Enter your number:-"))
count=0
n1=0
n2=1
if nterms<=0:
    print("invalid input please enter postive number:-")
elif nterms==1:
    print("Fibinocci series upto:-",nterms,":")
else:
    print("Fibinocci series upto:-",nterms,":")
    while nterms>count:
        print(n1,end=' ')
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
        
        
    
        
        
    
    
    
