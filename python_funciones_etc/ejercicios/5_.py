"""Crear un programa que devuelva los caracteres 
ASCII de los códigos el 97 al 100 (a-n)."""


from math import ascii

def llamando_ascii(a,n):
    print(a,n)
print(llamando_ascii.join(chr()))

#.join(chr(x) for x in range(128))