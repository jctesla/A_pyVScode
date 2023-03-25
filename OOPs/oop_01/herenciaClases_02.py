# ESTE EJEMPLO Crea una Lista de Estudiantes que no tengan el Mismo codigo.
# class Student: .- permite crear el perfil de un Estudiante
# class ListaAlum(Student): 
# contiene todos los alumnos creados en una Lista, q no tengna el mismo codigo y Ejemplifica la Herencia de Clases en;
# class Course: .- Ejemplifica cmo Crear un Arreglo de Objectos

# --------------Clase Student
class Student:
  def __init__(self,code, name, nota):
    self.code = code
    self.name = name
    self.nota = nota

  def get_code(self):
    return self.code
  def get_name(self):
    return self.name
  def get_nota(self):
    return self.nota    


#--------------Clase List Students
#1ro verifica q no se repita el codigo y si no existe
#2do agrega a la lista General 'lstStudent'
class ListaAlum(Student):                       
  def __init__(self):
    self.lstStudent = []

  def addStd_list(self, student):
    flgExist = False                        # indica el resultado de la validacion.

    # Reviso si ya existe este 'code' en la lista de los Alumnos Ingresados = 'lstStudent'.
    # True = Ya Existe / False = No existe en la lista 'lstStudent'
    indx = 0
    while indx < len(self.lstStudent) and  len(self.lstStudent) > 1:  #Si el indice > 1 y menor q los elementos de la Lista 'lstStudent'
        if (self.lstStudent[indx].code == student.code):
          flgExist = True
          break
        else:
          indx+=1

    # Si no existe el nuevo 'code' lo agrego, de o contrario lo rechazo.
    if (flgExist != True):
      self.lstStudent.append(student)
      # print(student)                  # si solo imprimo asi, me va devolver al dir_mem de la variable.
      return True                       # ej : <__main__.Student object at 0x00000000029A8308>
    else:
      print(f"El Alumno = " + student.name.upper() + " con Codigo = " + str(student.code)  + " YA EXISTE!!")
      return False
      
  def rd_validList(self):
    return self.lstStudent


#--------------Clase Course
class Curso:
  def __init__(self, curso):
    self.cname = curso
    self.students = []

  def add_student(self, student):
    self.students = student
    return len(self.students)

  def prom_nota(self):
    value = 0
    for student in self.students:
      value += student.get_nota()
    return value / len(self.students)



#--------------------------------------------
#         Main program
#--------------------------------------------

# Creo 6 perfiles q son 6 Objts de Estudiantes: Codigo, Nomb, Nota
s1 = Student(100,"Tim",95)
s2 = Student(101,"Bill",75)
s3 = Student(102,"Jill",65)
s4 = Student(103,"Fill",55)
s5 = Student(100,"Bill",69)
s6 = Student(105,"Pabblo",77)

lstStudent = [s1,s2,s3,s4,s5,s6]      # c/perfil los agrupo en una Lista de Objs!

#Agrego a Lista General de Alumnos = listaAlumnos
listaAlumnos = ListaAlum()

# recorro c/profile y verif si el Codigo no se REPITE
# sino se REPITE se almacena en otra lista Valdidada
for alm in lstStudent:
  if listaAlumnos.addStd_list(alm):
    print("Alumno Nuevo  Codigo = " + str(alm.get_code()) + " / Nombre = " + alm.get_name())
  else:
    print("Alumno Ya Existe con el Mismo Codigo = " + str(alm.get_code()) + " / Nombre = " + alm.get_name())


print("---------------------------")
# Lista de Student validado
objSt =  listaAlumnos.rd_validList()
for idx,val in enumerate(objSt):
  print(f"Students[{idx}] = Code:{val.get_code()} Name:{val.get_name()}  Nota:{val.get_nota()}")


print("---------------------------")
course = Curso("Math")
print(f"List of Students Added! = {course.add_student(objSt)}")

# Saco el Promedio de la Lista Validada de Estudiantes.
print("Promedio Notas de Estudiantes = " + str(course.prom_nota()) )


# Alumno Nuevo  Codigo = 100 / Nombre = Tim
# Alumno Nuevo  Codigo = 101 / Nombre = Bill
# Alumno Nuevo  Codigo = 102 / Nombre = Jill
# Alumno Nuevo  Codigo = 103 / Nombre = Fill
# El Alumno = BILL con Codigo = 100 YA EXISTE!!
# Alumno Ya Existe con el Mismo Codigo = 100 / Nombre = Bill
# Alumno Nuevo  Codigo = 105 / Nombre = Pabblo
# ---------------------------
# Students[0] = Code:100 Name:Tim  Nota:95
# Students[1] = Code:101 Name:Bill  Nota:75
# Students[2] = Code:102 Name:Jill  Nota:65
# Students[3] = Code:103 Name:Fill  Nota:55
# Students[4] = Code:105 Name:Pabblo  Nota:77
# ---------------------------
# List of Students Added! = 5
# Promedio Notas de Estudiantes = 73.4