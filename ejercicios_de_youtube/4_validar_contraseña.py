"""
4 - Programa que valide si una contraseña especificada por el usuario es segura.
Una contraseña es segura cuando:
* Tiene más de 8 carácteres.
* Tiene al menos una letra mayúscula
* Tiene al menos un número.
"""
import os
os.system("cls")

def seguridad_contraseña(contraseña):
    long_contraseña = (len(contraseña))
    mayuscula = max(contraseña)
    mayuscula=int(mayuscula)
    numero = (contraseña).isnumeric()
    if long_contraseña > 8 and mayuscula >= 1 and numero >= 1:
        print("La contraseña es segura")
    else:
        print("La contraseña no es segura")


clave = input("Ingrese la contraseña para saber si es segura: ")
seguridad_contraseña(clave)