import time


def countdwn(n):
    while n > 0:
        n -=1

if __name__ == '__main__':
    
    
    start = time.time()

    conta = 100000000
    print(f'Inicio...')
    countdwn(conta)
    print(f'tiempo Trasncurrido : {time.time() - start}')       # segundos.microseg
