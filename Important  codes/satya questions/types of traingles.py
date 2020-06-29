a=int(input("Enter your number:-"))
b=int(input("Enter your number:-"))
c=int(input("Enter your number:-"))
if a==b==c:
    print(" Then it is equilateral Traingle")
if a==c:
    print("Then it is Isosceles Traingle")
if a<b or a>b or b<c or b>c:
    print("Then it is Scalene Traingle")
