'''
Genera operaciones de suma resta Arriba Abajo:
# Solucion:
#    32      3801      45      123
# + 698    -    2    + 43    +  49



#     32       3801       45       123
# +  698    -     2    +  43    +   49
# ------    -------    -----    ------
#    730       3799       88       172

'''


def arithmetic_arranger(problems, withTotal=False):
  print("Len arry={len(problems)} \n")

  cntErr = 0
  op1 = []
  op2 = []
  symb = []
  rslt = []

  for m in problems:
    p = findOperator(m)

    #---------------------
    if p > -1:
      snum = m[0:p].strip()
      if snum.isnumeric():
        if len(snum) < 5:
          op1.append(snum)

          snum = m[p + 1:].strip()
          if snum.isnumeric():
            if len(snum) < 5:
              op2.append(snum)
              symb.append(m[p])
              
              if symb[-1] == '+':
                rslt.append(str(int(op1[-1]) + int(op2[-1])))
              else:  
                rslt.append(str(int(op1[-1]) - int(op2[-1])))
                
            else:
              cntErr += 1
              print(f"Ope2 = {err_code(3)}")
          else:
            cntErr += 1
            print(f"Ope2 = {err_code(2)}")
        else:
          cntErr += 1
          print(f"Ope1 = {err_code(3)}")
      else:
        cntErr += 1
        print(f"Ope1 = {err_code(2)}")

    else:
      cntErr += 1
      print(f"Ope1 = {err_code(1)}")

    #----------------------
    if cntErr > 4:
      arranged_problems = err_code(0)
      break

  # return all values formated

  if cntErr < 5:
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    spc =""

    
    for i, v in enumerate(problems):
      
      spc = spcOp(op1[i], op2[i])
      
      if i==(len(problems) - 1):
        spcOp1 = spc + op1[i]                               # "____" + 124
        lenOp = -1 * len(spc)                               # select lef of string 
        line1 = line1 + " " + spcOp1[lenOp:] + '\n'

        spcOp2 = spc + op2[i]                               # "____" + 4257
        line2 = line2 + symb[i] + spcOp2[lenOp:] + '\n'
        
        line3 = line3 + spcs(spcOp2[lenOp:],"-") + '\n'
        
        if withTotal:
          spcRslt = spc + rslt[i]
          lenOp = -1 * (len(spc) + 1)
          line4 = line4 + spcRslt[lenOp:] + '\n'
        
      else:
        spcOp1 = spc + op1[i]                               # "____" + 124
        lenOp = -1 * len(spc)
        line1 = line1 + " " + spcOp1[lenOp:] + "    "

        spcOp2 = spc + op2[i]                               # "____" + 4257
        line2 = line2 + symb[i] + spcOp2[lenOp:] + "    "   # YA incluye el spc antes del Numero
        
        line3 = line3 + spcs(spcOp2[lenOp:],"-") + "    "
        
        if withTotal:
          spcRslt = spc + rslt[i]
          lenOp = -1 * (len(spc) + 1)
          line4 = line4 + spcRslt[lenOp:] + "    "
        
    
    arranged_problems =  line1 + line2 + line3 + line4

  return arranged_problems



#--------------------------------------------
# return number of spaces of the Op big
def spcOp(op1, op2):
  if len(op1) > len(op2):
    return spcs(op1," ")
  elif len(op1) < len(op2):
    return spcs(op2," ")
  else:
    return spcs(op1," ")


# return number of spc
def spcs(w,symb):
  s = symb
  for i in w:
    s += symb
  return s


def findOperator(m):
  if m.find("+") > -1:
    return m.find("+")
  elif m.find("-") > -1:
    return m.find("-")
  else:
    return (-1)


def err_code(e):
  if e == 0:
    return "Error: Too many problems."
  elif e == 1:
    return " Error: Operator must be '+' or '-'."
  elif e == 2:
    return "Error: Numbers must only contain digits."
  elif e == 3:
    return "Error: Numbers cannot be more than four digits."
  else:
    return "Error: Error are Not clear."



#-----------------------------------------------------------
#             main()
#-----------------------------------------------------------

def main():
    print("Hello World!")
    print( arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]) )
    print()
    print( arithmetic_arranger(["32 - 698", "3801 + 2", "45 - 43", "123 - 49"],True ) )
    


if __name__ == "__main__":
    main()
    
    
