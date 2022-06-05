""" 2 - Programa que calcule el IVA de una compra, siendo
el IVA 19% sobre el valor total de la compra.
"""
import os
os.system("cls")

def calcular_iva(precio):
    return precio*1.19

def ingreso_datos():
    sw = True
    while sw == True:
        respuesta = input("Desea saber el valor final de un producto? (s = si - n = no)\n")
        respuesta = respuesta.lower()
        if respuesta == "s":
            valor_bruto = int(input("Ingrese el valor del producto: $"))
            valor_total = calcular_iva(valor_bruto)
            print(f"El valor total con iva de ${valor_bruto} es: ${valor_total}")
        elif respuesta == "n":
            print("Hasta luego :D")
            sw = False
        else:
            print("Respuesta no identificada, intentelo de nuevo :D")

ingreso_datos()