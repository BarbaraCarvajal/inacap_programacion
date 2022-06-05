"""
Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar 
si quiere calcular y mostrar su perímetro o su superficie.
Hacerlo con 3 funciones y que sea con parametros.
"""

def perimetro(num):
    return print(f"El perimetro es: {num*4}")

def superficie(num):
    return print(f"La superficie del cuadrado es: {num*2}")

def datos():
    sw = True
    while sw == True:
        pregunta = int(input("¿Desea usar el programa? 1 = sí - 2 = no\n"))
        if pregunta == 1: 
        
            num = float(input("Ingrese la distancia de un lado del cuadrado: "))
            respuesta = int(input("""
            ¿Qué desea hacer?
            Opción 1: Calcular perímetro
            Opción 2: Calcular superficie \n"""))

            if respuesta == 1:
                perimetro(num)
            elif respuesta == 2:
                superficie(num)
        else:
            print("Muchas gracias, adios!")
            sw = False
    
datos()

