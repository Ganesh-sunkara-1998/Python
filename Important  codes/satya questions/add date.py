import datetime
dd=int(input("enter your date:-"))
mm=int(input("enter your month:-"))
yy=int(input("enter your year:-"))
d=datetime.date(yy,mm,dd+1)
print(d)
