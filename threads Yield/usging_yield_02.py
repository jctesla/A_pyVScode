# Object Generator  is a special type of function which does not return a single value,
# instead, it returns an 'Iterator Object' with a sequence of values
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
        if num > 10:
          break
        
for i in infinite_sequence():
  print(i, end=" ")  