# import the lib
import datetime
my_date = "2017-11-13 10:22:54.677"                                 # store a string date
date = datetime.datetime.strptime(my_date, '%Y-%m-%d %H:%M:%S.%f')  # parse string --> date

print(f"Date:{date}")
print(f"Day: {date.day}")
print(f"Month:{date.month}")
print(f"Year: {date.year}")

import sys
print("python execut=", sys.executable, "  version=", sys.version)  # py exec= /usr/bin/python3   version= 3.9.16