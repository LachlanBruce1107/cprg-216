is_leap_year = False
year = int(input("Please type a year: "))

#nested if statement version
'''
if (year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            is_leap_year = True
    else:
        is_leap_year = True

if (is_leap_year):
    print("That is a leap year")
else:
    print("That is not a leap year")
'''

#logical operators version
if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
    print("That is a leap year")
else:
    print("That is not a leap year")