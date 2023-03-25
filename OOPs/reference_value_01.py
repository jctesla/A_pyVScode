# Con este ej demostrasmo como python tabja con referencias.add()

def changeme( mylist ):
   mylist.append([1,2,3,4]);
   print("Values inside : ", mylist)
   return 0

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside: ", mylist)


# Values inside :  [10, 20, 30, [1, 2, 3, 4]]
# Values outside:  [10, 20, 30, [1, 2, 3, 4]]