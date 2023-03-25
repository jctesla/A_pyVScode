import datetime as dt

# Mapping of the week day
weeks = ("monday", "tuesday", "wednesday", "thursday","friday", "saturday", "sunday")


def add_time(start, duration, dayWeek=""):

  if valida(start):
    if duration.find(":"):
      _duration = duration.split(":")              # separate hr & min.  
      d_hr = int(_duration[0])
      d_mi = int(_duration[1])
      
      _start = start.split(":")                    # 12:15 AM
      __start = _start[1].split(" ")               # 15 AM
      s_hr = int(_start[0].strip())
      s_mi = int(__start[0].strip())
      ampm = __start[1].strip().upper()
  
      if ampm == 'PM':
        s_hr = s_hr + 12                          # 24hr format.

      #------------------------------
      _days = int((s_hr + d_hr)/24)
      _hrs = (s_hr + d_hr)%24
      __hrs = int((s_mi + d_mi)/60)
      t_hrs = _hrs + __hrs
      if t_hrs > 23:
        _days += 1
        t_hrs -= 12
      _mins = (s_mi + d_mi)%60

      print(f"Dias={_days} Hrs={t_hrs}  Min={_mins}")

      #-------------------------------
      lbl_HR=""
      if t_hrs > 12:
        lbl_HR = ("0" + str(t_hrs - 12))[-2:] + ":" + ("0" + str(_mins))[-2:] + " PM"
      else:
        lbl_HR = ("0" + str(t_hrs))[-2:] + ":" + ("0" + str(_mins))[-2:]  + " AM"

      lbl_day=""
      if _days == 1:
        lbl_day= " ( " + "next day" + " )"
      elif _days > 1:
        lbl_day= " ( " + str(_days) + " day later" + " )"
      else:
        lbl_day= ""
      
      if dayWeek=="":
        new_time = lbl_HR +  lbl_day 
      else:
        n_day = weeks.index(dayWeek.lower())
        final_day= weeks[(n_day + _days )%7]
        new_time = lbl_HR +  ", " + final_day + lbl_day
       
  else:
    print(f"tiempo start NO VALIDO")
  return new_time



def valida(start):
  if start.find(":"):
    hr = start.split(":")
    if hr[0].isnumeric():
      if hr[1].find("AM") or hr[1].find("am") or hr[1].find("PM") or hr[1].find("pm"):
         return True
      else:
         return False
    else:
      return False
  else:
    return False