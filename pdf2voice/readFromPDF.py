# Este programa convierte un file de PDF q le indiquemos a un audiobook.
# 100 import pyttsx3
import pdfplumber
import PyPDF2
import time

#obtenemos el nombre del file y la ruta del file PDF.
file = 'TipsIngles_2022_for_audio_espanol.pdf'  #'ejemplo_tts.pdf'

pdfFileObj = open(file, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages = pdfReader.numPages
print((f'Numero de Pag = {pages}'))

# segun la cantidad de paginas
with pdfplumber.open(file) as pdf:
    # loop segun el numero de paginas
    for i in range(0,1):                # pages
        page = pdf.pages[i]
        text = page.extract_text()
        
        lineas = text.split('\n')
        print(f'Lineas = {len(lineas)}\n')                     # imprimo l q se esta produciendo en audio
        cmip=1
        for idx,ln in enumerate(lineas):
          mip = ln.find('mip ',0)
          if (mip !=-1):
            digit = 'mip'+ str(cmip) + ': '
            ln = ln.replace('mip', digit)
            cmip +=1
          #print(f'Linea{str(idx+1)} : {ln}')
          print(f'{ln}')
          

        
        # 100 speaker = pyttsx3.init()
        # 100 rate = speaker.getProperty('rate')  # getting details of current speaking rate
        # 100 print(rate)  # printing current voice rate
        # 100 speaker.setProperty('rate', 150)  # setting up new voice rate
        # 100 speaker.say(text)
        # 100 speaker.runAndWait()

