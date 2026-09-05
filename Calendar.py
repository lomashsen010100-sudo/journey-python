# import calendar as your month and year choice.

import calendar

while True:
    year=int(input("Enter Year:="))
    month=int(input("Enter Month:="))
    
    cal=calendar.month(year, month)
    print(cal)