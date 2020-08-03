def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a//b)

print("""Select your choice: 
1.add
2.sub
3.mul
4.div""")
choice = int(input("enter yr choice: "))
a= int(input("num 1: "))
b= int(input("num 2 : "))
if choice == 1:
    add(a, b)
elif choice == 2:
    sub(a, b)
elif choice ==3:
    mul(a, b)
else:
    div(a, b)
