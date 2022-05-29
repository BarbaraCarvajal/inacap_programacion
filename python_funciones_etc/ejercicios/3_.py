"""Escribir un programa que ingrese un numero entero mayor que cero 
(debe validar este ingreso) y muestre los 
divisores de ese número de manera decreciente. 
Ejemplo: número 75, divisores: 75, 25, 15, 5, 3, 1. """


def divisores():
    num = int(input("Ingrese un número mayor que cero\n"))
    if num>0:
        x=1
        for x in range(num):
            if num%x == 0:
                divisor = x
                print(divisor)
divisores()