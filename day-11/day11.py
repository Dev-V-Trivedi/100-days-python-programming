# This program calculates the number of seconds, minutes, hours, days, and weeks in a year.
# It takes the user's input on whether the current year is a leap year or not and calculates the number of days accordingly.
# It then calculates the number of seconds, minutes, hours, days, and weeks in a year based on the user's input.
# This program calculates the number of seconds, minutes, hours, days, and weeks in a year.


secs = 60
mins = secs * 60
hours = mins * 24
leapyear = input("Is the current year a leap year? (Yes or Now): ")

if leapyear == "Yes" or "yes":
    leapornot = 366
elif leapyear == "No" or "no":
    leapornot = 365
else:
    print("Please enter Yes or No")
day = hours * leapornot

print("Number of seconds in a day: ", day)
print("Number of minutes in a day: ", day / secs)
print("Number of hours in a day: ", day / mins)
print("Number of days in a year: ", leapornot)
print("Number of weeks in a year: ", leapornot / 7)