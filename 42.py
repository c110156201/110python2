from tkinter import Y


a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

x=((-b)+((b**2)-(4*a*c))**0.5)/(2*a)
y=((-b)-((b**2)-(4*a*c))**0.5)/(2*a)
print(x," ",y)