from replit import clear
clear()
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return print(f"\n{year}: Leap year.")
      else:
        return print(f"\n{year}: Not leap year.")
    else:
      return print(f"\n{year}: Leap year.")
  else:
    return print(f"\n{year}: Not leap year.")
    


def days_in_month(year,month):
  is_leap(year=year)
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  month_name = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
  return f"\n{month_name[month-1]} has {month_days[month-1]} days.\n"
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)