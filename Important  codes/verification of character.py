# input character is alphabet or digit or special character
ch=input("enter your character:-")
if (ch>='a'and ch<='z')or(ch>='A'and ch<='Z'):
    print("your character is aplhabet")
elif(ch>='0' and ch<='9'):
    print("your character is digit")
else:
    print(ch,"your character is special character")
    
