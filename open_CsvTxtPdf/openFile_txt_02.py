# modos de aprtruar un file ne python con open():
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

cnt = 0
LL = ""
f=open('syslog_appamor.txt', 'r')
while True:
  L = f.read()
  
  if len(L) < 1:
    f.close()
    break
  LL = L
#print(LL)  


lxl = LL.split(chr(10))
print(len(lxl))
print(LL.count(chr(10)))

failed = []
sngt = len(lxl)
for li in lxl:
  if li.find('failed')!=-1 or li.find('Failed')!=-1 or li.find('FAILED')!=-1:
    failed.append(li)


print("\n")
#for l in failed:
#  print(l)
  
f=open('failedfile.txt', 'w')
for l in failed:
  f.write(l+chr(10))
f.close()  

  

  