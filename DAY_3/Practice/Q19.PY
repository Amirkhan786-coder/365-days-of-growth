# LEAP YEAR 

print("Leap Years from 2000 to 2100\n")

for year in range(2000, 2101):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year)