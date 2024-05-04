import calc
x=3
y=5
print("sum: ",calc.add(x,y))
print("mul:",calc.mul(x,y))
print("div",calc.div(x,y))
print("sub:",calc.sub(x,y))



print("1.adding")
print("2.multiplication")
print("3.division")
print("4.substraction")
choice=int(input("choice the operation:"))
x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
if choice==1:
    print("sum: ",calc.add(x,y))
elif choice==2:
    print("mul:",calc.mul(x,y))
elif choice==3:
    print("div",calc.div(x,y))
elif choice==4:
    print("sub:",calc.sub(x,y))
else:
    print("invalid")