# En este ejemplo explicamos la Recursividad haciendo una semejanza de Puh()/Pop() en una memoria FIFO stack assambler 8bits:
# ej sgnt; se va llamar asi mísmo, va hacer posh(), tantas veces n<1, si se cumple esta condicion, generamos el 1er 'return'
# (es como un switch de Push --> Pop) el stack a hora es Pop, y ahi recien empieza hacer Pop memory from stack.

c = 0

def fib(n):
    global c
    
    if n < 1:
        return 1
    
    c += 1
    print(f'stack in c={c} / n={n}')
    f = fib(n-1)
                
    print(f'stack out c={c} / n={n}')
    c -= 1
    return f

#---------- MAIN -------------------------
if __name__ == '__main__':
    print(f'final = {fib(3)}')


