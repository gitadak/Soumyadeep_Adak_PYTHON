#How many leap years are there in a provided range of years
from calendar import isleap

start_year = int(input("Enter the starting year: "))
end_year = int(input("Enter the ending year: "))

leap_year_count = 0
l=[]
for year in range(start_year, end_year + 1):
    if isleap(year):
        l.append(year)
        leap_year_count += 1

print("Number of leap years between {} and {}: {}".format(start_year, end_year, leap_year_count))
if len(l)!=0:
    print("The leap years are:")
    for i in l:
        print(i)