# Este programa convierte un file de PDF q le indiquemos a un audiobook.
import pyttsx3
import pdfplumber
import PyPDF2
import time

#obtenemos el nombre del file y la ruta del file PDF.
file = 'TipsIngles_2022_for_audio.pdf'  #'ejemplo_tts.pdf'

pdfFileObj = open(file, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages = pdfReader.numPages
# segun la cantidad de paginas
with pdfplumber.open(file) as pdf:
    # loop segun el numero de paginas
    for i in range(0,pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)                     # imprimo l q se esta produciendo en audio
        speaker = pyttsx3.init()
        rate = speaker.getProperty('rate')  # getting details of current speaking rate
        print(rate)  # printing current voice rate
        speaker.setProperty('rate', 150)  # setting up new voice rate
        speaker.say(text)
        speaker.runAndWait()


