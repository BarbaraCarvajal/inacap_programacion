"""Solicitando el número de filas, el número de columnas y el caracter,
 generar la siguiente salida 
del caracter por pantalla: (Ejemplo: filas=7, columnas=4, caracter=*).  
Pista: Utilizar ciclo for anidado. 
"""
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
caracter = (input("Ingrese el caracter que desea ver: "))

for x in range(1,filas+1):
    print("")
    for x in range(columnas):
        print(end=caracter)
