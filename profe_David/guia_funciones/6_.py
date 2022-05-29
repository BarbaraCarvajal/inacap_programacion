"""
Elaborar una función que nos retorne el per√≠metro de un cuadrado 
pasando como parámetros el valor de un lado. 
"""



def perimetro():
    lado = float(input("Ingrese la medida de un lado del cuadrado: "))
    print(f"El perimetro es: {lado*4}")

perimetro()