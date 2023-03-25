class MyList:
    def __init__(self, *args):
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            self._data = list(args[0])                        # handles `MyList([1, 2, 3])
        else:
            self._data = list(args)                           # handles `MyList(1, 2, 3)`

    def __getitem__(self, index):
        out = self._data[index]
        # slicing should return a `MyList` instance
        # otherwise, the individual element should be returned as-is
        return MyList(out) if isinstance(index, slice) else out

    def __setitem__(self, key, value):
        self._data[key] = value

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        """ Use the character | as the delimiter for our list"""
        # `self._data.__repr__()` returns '[ ... ]',
        # thus we can slice to get the contents of the string
        # and exclude the square-brackets, and add our own
        # delimiters in their place
        print("Method: __repr__")
        #return "|" + self._data.__repr__()[1:-1] + "|"
        return self._data.__repr__()                          # devuelv el list [,,,] todo como un string "[,,,]""

    def __contains__(self, item):
        return item in self._data

    def append(self, item):
        self._data.append(item)
        
#-------------------------------------------
#     Nain Class
#-------------------------------------------
# MyList can accept any iterable as its first (and only) input argument
x = MyList("hello")             
print(x)                                   # |'h', 'e', 'l', 'l', 'o'|

# MyList accepts an arbitrary number of arguments
x = MyList(1, 2, 3, 4, 5)
print(x)                                   # |1, 2, 3, 4, 5|

print(len(x))                              # 5

# getting an item
print(x[0])                                # 1

# slicing returns a MyList instance
print(x[2:4])                              # |3, 4|

# setting an item
x[0] = -1
print(x)                                   # |-1, 2, 3, 4, 5|

# checking membership
print(10 in x)                             # False

print(MyList())                            # ||
