A = int(input(f"Ingrese A : "))
print(f"Input A = {bin(A)}")
B = int(input(f"Ingrese B : "))
print(f"Inut B = {bin(B)}")
print(F"binary A OR B = {bin(A | B)}")
print(F"binary A AND B = {bin(A & B)}")
print(F"binary A XOR B = {bin(A ^ B)}")
print(F"binary A NOT A = {bin(~A)}")

# Out:
# Ingrese A : 9
# Input A = 0b1001
# Ingrese B : 5
# Inut B = 0b101
# binary A OR B = 0b1101
# binary A AND B = 0b1
# binary A XOR B = 0b1100
# binary A NOT A = -0b1010