'''write a program to create a dictionary  interms keys and values in
runtime... and sorted according to values...'''
list1=[]
n=int(input("Enter how many entire you have:-"))
for i in range(n):
        e=(input("Enter your key:-"))
        list1.append(e)
dict1={}
for j in list1:
    val= input("Enter your value:-")
    dict1[j]=val
print("Dictionary is:-",dict1)

dict2={}
dict2=sorted(dict1.values())
print("Dictionary sorted:-",dict2)

    
    
    

    


    



        
