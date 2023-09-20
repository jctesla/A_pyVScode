import PyPDF2
import os


#--------- VERIFY if EXIST DIR & FILE --------------
def dir_exist_empty(path_dir):
  dir_exist = False
  
  if os.path.isdir(path_dir) and os.access(path_dir, os.R_OK):
    os.chdir(path_dir)                                               # c:\>cd PATH_DIR  ; el cursor lo cambiamos al Directorio indicado.
    print(f'Listado de Files en el Dir = {os.getcwd()}')               # ruta de las imagenes .png origen para convertir.
    lstfiles = os.listdir(os.getcwd())                               # c:\>dir          ; hacemos un listado del directorio actual.
    if len(lstfiles) > 0:
      for idx,filename in enumerate(lstfiles):
        print(f'{idx}.- {filename}')                               # vizualizo ruta de c/imagen .png    
      
      dir_exist = True
    else:      
      print(f'NO Hay Files en este Directory')   
      
  return dir_exist


#----------- Reade the PDF file -----------------------
def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)

        text = ''
        num_pages = pdf_reader.numPages
        print(f'Numero de Paginas = {num_pages}')
        page = pdf_reader.getPage(15)
        print(f'Texto 15ta Paguina = {page.extractText()}')
        
        #for page_num in range(num_pages):
        #    page = pdf_reader.getPage(page_num)
        #    text += page.extractText()
        
    return text


#---------------------------------------------------
#                    MAIN
# Replace 'path_to_your_pdf_file.pdf' with the actual path to your PDF file
PATH_Dir = 'G:\\$LIBROS VARIOS\\$HOW_to_LEARN'
pdfName = 'Make It Stick (Peter C. Brown)_2014.pdf'

# verifico si existe este path o file-
if (dir_exist_empty(PATH_Dir)):
  print(f'{read_pdf(pdfName)}')
else:
  print('NO EXISTE EL DIRECTORIO o NO TIENE PERMISO DE LEER')  
