obj=iter('abcd')					# implementa naturalmente el metodo __next__
print(f'Valor de next(obj) = {next(obj)}')        	# a
print(f'Valor de next(obj) = {obj.__next__()}')		# b
print(f'Valor de next(obj) = {next(obj)}')		# c
arry = list(obj)
print(arry)                      	   		# Valor de obj = ['a', 'b', 'c', 'd']

