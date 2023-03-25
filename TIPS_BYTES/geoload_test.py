fh = open("where.data")
count = 0
for line in fh:
    if count > 10 :
        print(f'Retrieved 10/200 locations, restart to retrieve more')
        break

    # retiramos los espacios vacios de los extremos del string
    address = line.strip()                                                        # tipo  <class 'str'>
    print(f'\naddress =  {address.encode()}')                                     # address = b'AGH University of Science and Technology'     --> binaryArray()
    print(f'2da letra = {address.encode()[1]} / {chr(address.encode()[1])} ')     # 2da letra = 71 / G                                        --> bin() / char()
    print(f'memoryview = {memoryview(address.encode())}')                         # memoryview = <memory at 0x0000000002607340>               --> The memoryview() function returns a memory view object.
    print(f'memoryview = {memoryview(address.encode()).hex()}')                   # 4265696a696e67206e6f726d616c20756e6976657273697479
    
    w = list(memoryview(address.encode()))
    wo = ''.join(chr(c)  for c in w)
    print(f'memoryview = {wo}')
    count = count + 1

