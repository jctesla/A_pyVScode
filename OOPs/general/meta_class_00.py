 #Creating custom Metaclass: We can create classes using the type() function directly. 

def test_method(self):
  	print("This is Test class method!")


# creating a base class
class miBase:
	def mifun(self):
		print("This is inherited method!")


#-----------------------------------------
#            Main()
#-----------------------------------------
# Creating Test class dynamically using
# type() method directly
Test = type('Test', (miBase, ), dict(x="atul", mi_method=test_method)) 
#Test = type('Test', (miBase, ), {"x":"atul", "mi_method": test_method})    # puede escribirse tambien así. 

# Print type of Test
print("Type of Test class: ", type(Test))               # <class 'type'>

# Creating instance of Test class
test_obj = Test()
print("Type of test_obj: ", type(test_obj))             # <class '__main__.Test'>

# calling inherited method from miBase class.
test_obj.mifun()                                        # This is inherited method!

# calling Test class method
test_obj.mi_method()                                    # This is Test class method!  

# printing variable
print(test_obj.x)                                       # "atul"
