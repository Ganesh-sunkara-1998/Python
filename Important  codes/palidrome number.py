# palidrome numbers....
number=int(input("enter your number:-"))
reverse=0
tempt=number
while (tempt>0):
    remainder=tempt%10
    reverse=(reverse*10)+remainder
    tempt=tempt//10
print("Reverse of a given number is %d",reverse)
if (number==reverse):
    print("%d is a palidrome number",number)
else:
    print("%d is  not a palidrome number",number)
