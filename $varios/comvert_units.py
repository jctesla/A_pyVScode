class Largo:
    __descript = {"mm":"Milimetros", "cm":"Centimetros", "m":"Metros", "km":"Kilometros",
                  "in":"Pulgadas", "ft":"foots", "yd":"Yardas", "mi":"Millas"}
    
    __metric = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
                "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
                "mi" : 1609.344 }
    
    def __init__(self, value, unit = "m" ):
        self.value = value
        self.unit = unit
        
    def Converse2Metres(self):
        return self.value * Largo.__metric[self.unit]
      
    def __add__(self, other):
        l = self.Converse2Metres() + other.Converse2Metres()
        return Largo(l / Largo.__metric[self.unit], self.unit )
      
    def __str__(self):
        return str(self.Converse2Metres())
      
    def __repr__(self):
        return "Largo " + str(self.value) + self.unit + " --> " + Largo.__descript[self.unit]

      
if __name__ == "__main__":
    x = Largo(4)
    print(repr(x))
        
    z = Largo(4.5, "cm") + Largo(1)
    
    print(repr(z))
    print(z)