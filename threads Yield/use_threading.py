# imports
import threading
import time

def worker(ii):
    print(f'worker....{i}')
    time.sleep(10)

threads = []
for i in range(1,3):
    thread = threading.Thread(target=worker,args=(i,) )
    threads.append(thread)
    thread.start()
print("fin")