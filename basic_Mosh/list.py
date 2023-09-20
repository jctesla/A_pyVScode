name = ['job','bob','juan','pedrino','maria']
print(name[-1])                 # the last element
print(name[-2])                  # secind element from last

print(name[0:3])
print(name[0:3:2])              # 0:3 = ['job','bob','juan'] , luego hagarra 0 y c/2 elementos = ['job','juan']

# List Method
nums = [num for num in range(10)]   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums)

nums.insert(1,-1)
nums.insert(3,True)
print(nums)                          # [0, -1, 1, True, 2, 3, 4, 5, 6, 7, 8, 9]

nums.remove(0)                       # [-1, 1, True, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums)

print(f'esta el Uno en nums = {1 in nums}')

numb = {idx:chr(idx+65) for idx in range(10)}
print(numb)                         # {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}

# truple

