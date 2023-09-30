#Leap year or not
def LeapYear(y):
    if y%100==0:
        if y%400==0:
            return True
    elif y%4==0:
        return True
    else:
        return False

year=int(input("Enter the year: "))
if LeapYear(year):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
