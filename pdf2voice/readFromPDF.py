# Este programa lee un file de PDF q le indiquemos y los separa en paginas para traducirlo y luego jalar la voz.
# 100 import pyttsx3
import pdfplumber
import PyPDF2
import time

#obtenemos el nombre del file y la ruta del file PDF.
file = 'page 6 to 8.pdf'    #'TipsIngles_2022_for_audio_espanol.pdf'  #'ejemplo_tts.pdf'

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
        cmip=0
        for idx,ln in enumerate(lineas):
          if len(ln) > 1:
            mip = ln.find('mip ',0)
            if (mip !=-1):
              cmip +=1
              digit = 'mip'+ str(cmip) + ': '
              ln = ln.replace('mip', digit)
              
            #verificamos si la linea de frase termina en punto.
            lnn = ln.rstrip(' ')
            if lnn[-1] != '.':
              lnn = lnn + "."
            
            print(f'{lnn}')
          

        
        # 100 speaker = pyttsx3.init()
        # 100 rate = speaker.getProperty('rate')  # getting details of current speaking rate
        # 100 print(rate)  # printing current voice rate
        # 100 speaker.setProperty('rate', 150)  # setting up new voice rate
        # 100 speaker.say(text)
        # 100 speaker.runAndWait()

