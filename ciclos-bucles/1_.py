
import os
os.system("cls")

# 1 - Realizar un programa que imprima en pantalla los números del 1 al 100.

def uno_al_cien_con_for_():
    for x in range(1,101):
        print(x)
        x += 1
        
def uno_al_cien_con_while():
    x = 1
    while x <=100:
        print(x)
        x += 1

"""
print("For")
uno_al_cien_con_for_()
print("While")
uno_al_cien_con_while()
"""

# 2 - Imprimir los números del 50 al 100.

def cincuenta_for():
    for x in range(50,101):
        print(x)
        x +=1 

def cincuenta_while():
    x = 50
    while x <=100:
        print(x)
        x += 1

"""
print("For")
cincuenta_for()
print("While")
cincuenta_while()
"""

# 3 - Imprimir los números del -50 al 0.

def cincuenta_negativo_for():
    for x in range(-50,1):
        print(x)
        x += 1

def cincuenta_negativo_while():
    x = -50
    while x <= 0:
        print(x)
        x += 1


"""
print("For")
cincuenta_negativo_for()
print("While")
cincuenta_negativo_while()
"""

# 4 - Imprimir los números del 2 al 100 pero de 2 en 2 (2,4,6,8 ....100).

def de_2_en_2_for():
    for x in range(2,101,2):
        print(x)
        x +=1

def  de_2_en_2_while():
    x = 2
    while x <= 100:
        print(x)
        x += 2
"""
print("For")
de_2_en_2_for()
print("While")
de_2_en_2_while()
"""

# 5 - Codificar un programa que solicite la carga de un valor positivo y nos muestre desde 1 hasta el valor 
# ingresado de uno en uno.
# Ejemplo: Si ingresamos 30 se debe mostrar en pantalla los números del 1 al 30

def secuencia():
    sw = True
    while sw == True:
        num = int(input("Ingrese un numero positivo: "))
        if num > 0:
            for x in range(1,num+1):
                print(x)
                x += 1
                sw = False
        else:
            print("No puede ingresar numeros negativos o el número 0. Intentelo de nuevo.")

# secuencia()

# 6 - Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la 
# suma de los valores ingresados y su promedio.

def suma_promedio():
    suma_numeros = 0
    promedio = 0
    for x in range(1,11):
        numero = int(input(f"{x}: Ingrese un numero: "))
        suma_numeros += numero
    promedio = suma_numeros/10
    print(f"La suma de los 10 números ingresados es: {suma_numeros}, y su promedio es: {promedio}")

# suma_promedio()

# 7 - Una planta que fabrica perfiles de hierro posee un lote de n piezas.
# Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese la 
# longitud de cada perfil; sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son 
# aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.

def hierro():
    pieza_apta = 0
    pieza_no_apta = 0
    cant_piezas = int(input("Ingrese la cantidad de piezas: "))
    for x in range(1,cant_piezas+1):
        longitud_pieza = float(input(f"Ingrese la lóngitus de la pieza N° {x}: "))
        if longitud_pieza >= 1.20 and longitud_pieza <= 1.30:
            pieza_apta += 1
            print("Pieza Apta :D ")
        else:
            pieza_no_apta += 1
            print("Pieza no apta :C ")
    print(f"La cantidad de piezas aptas son: {pieza_apta}")
    print(f"La cantidad de piezas no aptas son: {pieza_no_apta}")

hierro()

