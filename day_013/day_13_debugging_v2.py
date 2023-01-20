# number = int(input("Which number do you want to check? "))

# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")
  
year = input("What is the year?: ")
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  