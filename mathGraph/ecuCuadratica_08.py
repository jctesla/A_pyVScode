#usado en el Libro de 
#Usemos un aecuacion diferencial
#Veamso como graficar la ecuacion

import matplotlib.pyplot as plt

# Draw the graph
def drawEq(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Valor de X')
    plt.ylabel('Valor de Y')
    plt.title('Ecuacion Cuadratica')
    plt.show()
    return

def calculateEq():
    import numpy
    
    # Genero un arreglo de Valores para 
    # 'X' = resolucion de 1 punto de '0' a '30'
    vX = numpy.arange(0.0, 30.0, 1)         
    
    # Creo un list vacio p lueo almacenar los valores
    # calculados por la Funcion f(x)
    vY = []
               
    # Calculo los valores de f(x) = Fy
    # Genero un arreglo de Valores para 'Y'
    for x in vX:
        Fy = x**2 + x + 1
        vY.append(Fy)
        
    # Call the draw_graph function
    drawEq(vX, vY)
    return
    
calculateEq()
