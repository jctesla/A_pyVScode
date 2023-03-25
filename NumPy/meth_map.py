list1 = [[1, 3], [5, 7], [9, 11]] 
list2 = [[2, 4], [6, 8], [10, 12, 14]]   
print("Original lists:")
print(list1)
print(list2)
result = list(map(list.__add__, list1, list2)) 
print("\nZipped list:\n" +  str(result))
# zipped list:
# [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]


