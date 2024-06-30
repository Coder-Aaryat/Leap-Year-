print("Welcome to the Leap Year Calculator!")
#year = int(input("Which year do you want to check?"))
year = int(input("Enter the year:"))
if year % 4 == 0:
  print("Leap Year")
elif year % 100 == 0:
  print("Not Leap Year")
elif year % 400 == 0:
  print("Leap Year")
else:
  print("Not A Leap Year")
