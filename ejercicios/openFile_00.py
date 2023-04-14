filename = 'fileAnyOne.csv'
fl = open(filename, 'r')      # Open the file
linecount = 0
for line in fl:
    print(linecount,". ", line)
    linecount += 1
    if linecount > 2: break  # let's not print too many lines to the console

fl.close()                    # close the file 

#---------------------------------
filename = 'fileAnyOne.csv'
fl = open(filename, 'r') 
f = True
while fl and f:
   f =  fl.readline()
   print(fl.tell()," - ", f)            # return the position of character in file, 

#--------------------------------
fl = open(filename, 'r') 
with fl:
   print(fl.read())

#--------------------------------
with open(filename, 'r') as fl:
  print(fl.read())