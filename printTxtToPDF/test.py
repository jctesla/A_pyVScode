from fpdf import FPDF
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 15)

# create a cell
pdf.cell(200, 10, txt = "GeeksforGeeks",ln = 1, align = 'C')

# add another cell
pdf.cell(200, 10, txt = "A Computer Science portal for geeks.",	ln = 2, align = 'C')

# save the pdf with name .pdf
pdf.output("txtIngles.pdf")

fo=open('txtIngles.txt', 'w')



fi = open('Tips Ingles.txt')
pdf.add_page()
pdf.set_font("Arial", size = 15)

for nro,line in enumerate(fi):
   #print(f'{nro} {line}')
   #if nro==80:
   #  break
   if not line.startswith('•'):
      continue
      #print('No Cumple formato')
   else:
      i = line.find('=')
      fo.write(f'{nro}.- {line[2:i]} = {line[i+1:]}')   # 2= para evitar el simbolo y un espacio, i+1 = evitar copy el simbolo '='
      pdf.cell(200, 10, txt = "",ln = 1, align = 'C')
      
fo.close()      
          
          