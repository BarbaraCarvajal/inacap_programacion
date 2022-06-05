"""
5 - Programa que valide si un número es primo o no
"""

def num_primos(num):
    contador =  0
    for x in range(1,num+1):
        if num%x == 0:
            contador = contador + 1
    if contador >2 :
        return print("El numero no es primo")
    elif contador == 1 or contador == 0:
        return print("Los numeros 0 y 1 no son primos ni primos ")

    else:
        return print("El numero si es primo")

numero = int(input("Ingrese un numero: "))
num_primos(numero)