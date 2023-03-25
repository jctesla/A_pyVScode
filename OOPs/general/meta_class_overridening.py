# concepots:
# Method overriding is a feature of object-oriented programming languages where the subclass or child class
# can provide the program with specific characteristics or a specific implementation process of data provided
# that are already defined in the parent class or superclass.

# Method overriding is a feature of obj, where the subclass/child class, can provide specific characteristics/implementation of data
# that are already defined in the parent class or superclass.

# our metaclass
class MultiBases(type):
  	# overriding __new__ method
	def __new__(cls,bases):
		try:
			if len(bases) > 2:
				raise Exception("Herencia de Multiple")
			else:
				print("Todo Bien")
		except Exception as e:
			print(f"El Error = {e}")
      
# metaclass can be specified by 'metaclass' keyword argument
# now MultiBase class is used for creating classes
# this will be propagated to all subclasses of Base
class Base(metaclass=MultiBases):
	pass

# no error is raised
class A(Base):
	pass

# no error is raised
class B(Base):
	pass

# This will raise an error!
class C(A, B):
	pass
