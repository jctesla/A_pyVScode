# Este programa convierte un file de PDF q le indiquemos a un audiobook.
import pyttsx3
import time

text = "Travis!! mi querido gatito LEON"
while True:
   print(text)                                  # imprimo l q se esta produciendo en audio
   speaker = pyttsx3.init()
   rate = speaker.getProperty('rate')           # getting details of current speaking rate
   print(rate)                                  # printing current voice rate
   speaker.setProperty('rate', 150)             # setting up new voice rate
   speaker.say(text)
   speaker.runAndWait()
   #speaker.stop()
   time.sleep(2)
   print("................\n")
