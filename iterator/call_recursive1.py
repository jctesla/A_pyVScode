# Ej metodo recursivo de python, es decir se va comportar como
# un stack memory del tipo FIFO. x cada llamada a 'fib(n)' debo
# tener un 'return()'.

c = 0

#-------------------------------------------
# solo pintan la progres de PoP/Push
def push(n):
    global c
    c += 1                           
    print(f'stack Push(in) c={c} / n={n}')
    return 1
    
def pop(n):
    global c
    c -= 1
    print(f'stack PoP(out) c={c} / n={n}')
    return 1


#------------------------------------------
# Funcion principal
def fib(n):
   
    if n < 1:
        pop(n)
        return 1
    
    push(n)
    f = fib(n-1)                        # c/llamada asi mísmo, crea un 'push' to stack memory
                                        # y xC/push debe tener un 'pop', este se genera con un 'retur()'.
    pop(n)
    return f

#---------- MAIN -------------------------
push(0)
print(f'final = {fib(3)}')               # 1er call a 'fib(n)'