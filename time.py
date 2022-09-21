# Starting with the required imports
from datetime import datetime, date, time, timedelta
# Getting current date
today = date.today()
print ("Today's date is ", today)
print ("Current year is ", today.year)
print ("Current month is ", today.month)
print ("Current day is ", today.day)
print ("Current weekday is ", today.weekday())

# Explanation:

# # First, the user will enter the year of his choice, which needs to be checked for leap year. As per the algorithm, if the year divisible by 400, that year is straightway leap year. And so the first if statement is “(input_year%400 == 0)”.
# # Now when the year not divisible by 400, the second If statement will be executed that is “(input_year%100 == 0)”. If “(input_year%100 == 0)” evaluates to True. That means it’s a century year but not a leap year.
# # Now when both the above statement doesn’t satisfy to True, then the third statement will be evaluated “input_year%4 == 0”. And if this satisfies, then that year is a leap year, Else not a leap year.

input_year = int(input("Enter the Year to be checked: "))
if (input_year%400 == 0):
          print("%d is a Leap Year" %input_year)
elif (input_year%100 == 0):
          print("%d is Not the Leap Year" %input_year)
elif (input_year%4 == 0):
          print("%d is a Leap Year" %input_year)
else:
          print("%d is Not the Leap Year" %input_year)