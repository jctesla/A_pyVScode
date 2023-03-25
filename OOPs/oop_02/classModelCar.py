class Car():
    
    #global lista_car
    lista_car = []
           
    @classmethod
    def __init__(self):
        self.number = 0 
        
    @classmethod    
    def add_car(self,make,model,color):
        self.make = make
        self.model = model
        self.color = color
        self.number = self.number + 1
        
        lst=[make,model,color,self.number]       # crea un list
        self.lista_car.append(lst)
        
    @classmethod    
    def read_car(self,indx):
        print(f'Indice = {indx}')
        print(f'self = {self.lista_car[indx]}')
        
    
    @classmethod
    def num_car(self):
        return len(self.lista_car)                   # longitud del List
        

        
#Input Data to Object        
import sys                                      # p sber la version de mi python
print(f"Version de Python={sys.version} \n")

carro = Car()
carro.add_car("BMW","M3","red")
carro.add_car("Mercedes","M100","blue")
carro.add_car("Volvo","V440","pink")
carro.add_car("Ford","F50","brown")

print(f'Nro de Carros Ingrsados = {carro.num_car()} lists creados')
for idx,itm in enumerate(carro.lista_car):
    print(f"List {idx}:{itm}")

