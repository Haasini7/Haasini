weekNum = input("Enter the week number:")
weekNum = int(weekNum)

if (weekNum == 1):
  weekDay = "sunday"
elif (weekNum == 2):
  weekDay = "Monday"
elif (weekNum == 3):
  weekDay = "Tuesday"
elif (weekNum == 4):
  weekDay = "Wednesday"
elif (weekNum == 5):
  weekDay = "Thursday"
elif (weekNum == 6):
  weekDay = "Friday"
elif (weekNum == 7):
  weekDay = "Saturday"
else:
  weekDay = "invalid week number"
  
print (weekDay)
