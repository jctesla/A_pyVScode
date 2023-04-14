import csv

filename = 'fileAnyOne.csv'
row_count = 0

with open(filename, 'r') as fl:
  csvreader = csv.reader(fl, delimiter=',', quotechar='"')
  print("Here are CSV contents")
  for row in csvreader:
    # only process the first few rows
    if row_count > 2: break

    # row is a list
    print("Row: %s | %s | %s ... and so on" % (row[0], row[1], row[2]))
    row_count += 1
