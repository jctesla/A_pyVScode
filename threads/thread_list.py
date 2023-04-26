import threading
import time

def worker(n, retro):
    st = time.time()
    print(f'Este es el hilo {n}')
    while retro > 0:
        retro -=1
    print(f'tiempo final Thread {n} = {time.time() - st}')
    return


threads = list()
for i in range(3,6):
    t = threading.Thread(target=worker, args=(i,1000))
    threads.append(t)
    t.start()