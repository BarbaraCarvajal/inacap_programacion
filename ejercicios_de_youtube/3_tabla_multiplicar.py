""" 3 - Programa que calcule la tabla de multiplicar
de cualquier numero entero dado por el usuario
Debe calcular la tabla desde el 1 al 12.
"""
import os
os.system("cls")

def multiplicacion(num):
    for x in range(1,13):
        print(f"{num} x {x} = {num*x}")
        x += 1

def carga_de_datos():
    sw = True
    while sw == True: 
        respuesta = input("Desea saber un tabla de multiplicar? (s = si - n = no) \n")
        respuesta = respuesta.lower()
        if respuesta == "s":
            numero = int(input("Ingrese un numero: "))
            multiplicacion(numero)
        elif respuesta == "n":
            print("Muchas gracias, hasta luego")
            sw = False
        else:
            print("Respuesta no identificada, intente de nuevo. ")

carga_de_datos()