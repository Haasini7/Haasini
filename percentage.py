phy=int(input("Phy marks:"))
chem=int(input("Chem marks:"))
math=int(input("math marks:"))
bio=int(input("bio marks:"))
comp=int(input("comp marks:"))
total=(phy + chem + bio + math + comp)/500
percentage=total*100
print("percentage :",percentage)
if percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("grade B")
elif percentage>=70:
    print("Grade c")
elif percentage>=60:
    print("Grade D")
elif percentage>=40:
    print("Grade E")
else:
    print("Grade F")
