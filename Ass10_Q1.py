#Today's date and name of weekday
import datetime

# Get today's date
today_date = datetime.date.today()

# Get the name of the weekday
weekday_name = today_date.strftime("%A")

print("Today's Date:", today_date)
print("Name of the Weekday:", weekday_name)