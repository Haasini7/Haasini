leap=int(input(" "))
if((leap%4==0) or (leap%100==0) and (leap%400!=0)):
	print("yes")
else:
	print("no")
