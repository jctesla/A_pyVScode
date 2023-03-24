# ingresa un Nro Decimal y lo convierte a string binario

def bina(nro,binario=""):
    q = nro // 2
    r = nro % 2
    if q < 2:
        binario = str(q) + str(r) + binario 
        return binario
    binario += str(r)
    
    f = bina(q,binario)
    return f

#---------MAIN--------------------
nro = int(input("ingrese Nro :"))
rslt = bina(nro)

print(rslt)


    