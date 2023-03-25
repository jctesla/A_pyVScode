# Demonstrating (mis)use of special methods: __pow__  __doc__  __getitem__
class SillyClass:
    def __init__(self):
        self.lst = [10,20,30,40,50]

    def __getitem__(self, idx):
        """ Determines behavior of `self[key]` """
        if idx is None:
          return self.lst                 # return all list
        else:
          return self.lst[idx]            # return specific element.

    def __setitem__(self,idx,val):
        try:
          self.lst[idx] = val
        except IndexError:                # IndexError: list assignment index out of range 
          self.lst.append(val)
          print(f'value is adde, idx=dont exist, idx now = {len(self.lst)-1}')
          
    def __pow__(self, num):
        """ Determines behavior of `self ** NUM` """
        return f"Python Like You Mean It {num}"
      

silly = SillyClass()
print('1. ', silly[2])                      # 30    lo mismo
print('2. ', silly.__getitem__(2))          # 30    lo mismo

silly[5] = 100                              # if idx dont exist : value is adde, idx=dont exist, idx now = 5
print('3. ', silly[None])                   # None = return all list[] 
print('4. ', silly ** 2 )                   # Python Like You Mean It 2
print('5. ', SillyClass.__pow__.__doc__)    # Determines behavior of `self ** NUM`
print('6. ', silly.__pow__.__doc__)         # Determines behavior of `self ** NUM`

