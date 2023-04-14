# This read the fiel form our local drive, 'fileAnyOne.csv', and separates the fields column for each data.

import csv

filename = 'fileAnyOne.csv'
count = 0

with open(filename, 'r') as fl:                                                 # its is the same to assign: fl = open(filename, 'r')
  csvRead = csv.reader(fl, delimiter=',', quotechar='"')                        # this is the header of the sheet: "longitude","latitude",...
                                                                                # header content  delimitier=','   &   quotes = "" for each fields. 
  for row in csvRead:                                                           # loop to read all lines of document.
     if count > 2: break                                                        # for porpuse demo, only process the first few rows.
     print(f"Row: {row[0]} | {row[1]} | {row[2]} ... and so on")                # We add demilimiter '|' to the row of lists.
     count += 1

# out:
# Row: longitude | latitude | housing_median_age ... and so on
# Row: -122.050000 | 37.370000 | 27.000000 ... and so on
# Row: -118.300000 | 34.260000 | 43.000000 ... and so on