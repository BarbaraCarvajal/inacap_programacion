""""
Confeccionar una función que le enviemos como parámetro un string y nos retorne la 
cantidad de caracteres que tiene. En el bloque principal solicitar la carga de dos 
nombres por teclado y llamar a la función dos veces. Imprimir en el bloque principal 
cuál de las dos palabras tiene más caracteres.
"""
#funcion

import os
os.system("cls")

def contador_caracteres(caracter):
    largo= len(caracter)
    return largo


def datos():
    palabra1= input("Ingrese una palabra: ")
    largo_palabra_1 = contador_caracteres(palabra1)

    palabra2 = input("Ingrese otra palabra: ")
    largo_palabra_2 =contador_caracteres(palabra2)

    if largo_palabra_1 ==  largo_palabra_2:
        print (f"La cantidad de caracteres entre {palabra1} y {palabra2} es la misma '{largo_palabra_1}'")
    elif largo_palabra_1 > largo_palabra_2:
        print(f"La diferencia de caracteres entre {palabra1} y {palabra2} es: '{largo_palabra_1-largo_palabra_2}', por ende el mayor es palabra 1: {palabra1}")
    else:
        print(f"La diferencia de caracteres entre {palabra1} y {palabra2} es: '{largo_palabra_2-largo_palabra_1}', por ende el mayor es palabra 2: {palabra2}")

#main
datos()

    






