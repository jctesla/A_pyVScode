filename = './sample_data/california_housing_test.csv'
fl = open(filename, 'r')      # Open the file
linecount = 0
for line in fl:
    print(line)
    linecount += 1
    if linecount > 10: break  # let's not print too many lines to the console

fl.close()                    # close the file 
print("FIN")                  # FIN de test en barch main