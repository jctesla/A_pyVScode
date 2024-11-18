# ingresa un Nro Decimal y lo convierte a string binario

def bina(nro):
    binario=""
    while True:
        q = nro // 2
        r = nro % 2    
        if q < 2:
            binario = str(q) + str(r) + binario
            break
        binario += str(r)
        nro = q

    return binario

#---------MAIN--------------------
nro = int(input("ingrese Nro :"))
rslt = bina(nro)

print(rslt)


    