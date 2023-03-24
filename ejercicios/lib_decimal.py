import decimal as dc

d1 = dc.Decimal(10/3)
print(f"decimal de 10/3 = {d1}\n")

d2 = dc.Decimal('3.333333333333333481363069950020872056484222412109375')
print(f"decimal de 10/3 = {d2}\n")

s = '23.45678'                        # string number
n0 = dc.Decimal(s)
print(f"n0 = {n0} \n")                # n0 = 23.45678

n1 = '{:.2f}'.format(10/3)            # 2 decimales : f=flota / b=binary / o=octal / x=hexadecimal
print(f"n1 = {n1} \n")                # n1 = 3.33

n2 = float(s)
print(f"n2 = {n2} \n")                # n2 = 23.45678

n3 = dc.Decimal(s)
print(f"n3 = {n3} \n")                # n3 = 23.45678


x = 13.949999999999999999
h = round(x, 2)
print(f"13.949 redondeo a = {h}\n")   #  13.95
  