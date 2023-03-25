while True:
    try:
        x = int(input("Please enter a number: "))
        print(f"Oh!  That a nice number = {x}!!")
        break
    except Exception:
        print("Oops!  That was no valid number.  Try again...\n")     # no handler for try

#--------------------------------------------------------------------
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for miCls in [D, C, B, C]:
    try:
        raise miCls()
    except D:
        print("clase D")
    except C:
        print("clase C")
    except B:
        print("clase B")
#--------------------------------------------------------------------
# A try-except block can have the finally clause (optionally). The finally clause is always executed.
# where the 'else' clause is executed only if no exception happens.
try:
    x = int(input("Please enter a number: "))
    
except:
    print('Failed to set x')
else:
    print('No exception occured')
finally:
    print('We always execute this sentences')

#--------------------------------------------------------------------    
# You can catch many types of exceptions this way, where the 'else' clause is executed only if no exception happens.    
try:
    x = int(input("Please enter a number: "))
except SyntaxError:
    print('Fix your syntax')
except TypeError:
    print('\tOh no! A TypeError has occured')
except ValueError:
    print('\tA ValueError occured!')
except ZeroDivisionError:
    print('\tDid by zero?')
else:
    print('\tNo exception ocurred')
finally:
    print('We always execute this sentences w/o Err\n\n')
    
#----------------------------------------------------
# python code to demonstrate example of 
# raise keyword; if input is negative an an exception run:
num = int(input("Enter a positive number: "))

try:
    if num<0:
        raise Exception("Please input only positive value ")
except Exception as e:
    print(f"El Error = {e}")                                    # El Error = Please input only positive value

print("num = ", num)
