import calendar

month, day, year = map(int, input().strip().split(" "))
day = calendar.weekday(year, month, day)
weekday = calendar.day_name[day]
print(weekday.upper())
