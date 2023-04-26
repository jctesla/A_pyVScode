import threading, time


# -------------  THREAD Function -------------------------
def downlink(str, dly):
  while dly>0:  
    time.sleep(0.6)
    dly -=1
  print("\nFin : ", str)  
  
#-------------- Main Process ------------------------------    
t = threading.Thread(target=downlink,args=("Hola",10,))
t.start()
  
# print a progress bar of point until thread finish.  
pnts = "" 
while(t.is_alive()):
  pnts += "."
  print(pnts, end = '\r' )
  time.sleep(0.5)