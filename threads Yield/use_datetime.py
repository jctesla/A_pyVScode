#Es necesario importar las depencendias necesarias
from datetime import datetime

#Día actual
today = datetime.today()

#Fecha actual
now = datetime.now()

print(today)                                    # 2020-07-29 19:29:30.414559
print(now)                                      # 2020-07-29 19:29:30.414559
print(today.strftime("%M : %S : %f"))           # 29 : 30 : 414559   -----> minutos : segundos : milisegundos

# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	
# %p	AM/PM	PM	
# %M	Minute 00-59	41	
# %S	Second 00-59	08	
# %f	Microsecond 000000-999999	548513

import time

start = time.time()                                             # número de segundos desde el 1 de enero de 1970 a las 00:00:00
print(start)
named_tuple = time.localtime()                                  # get struct_time
time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)  # 29/07/2020, 19:26:04
print(time_string)