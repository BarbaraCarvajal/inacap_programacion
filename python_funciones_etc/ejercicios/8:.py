"""Crear  un  programa  que  simule  el  lanzamiento  de 
 un  dado  y  nos  pregunte:  ¿Qué  número  es?,  para  lo  cual 
introducimos  un  número  y  nos  dirá  
“El  número  del dado es mayor o menor” según corresponda, hasta que 
acertamos y nos dice ¡Has acertado! """

from random import randint as dado

num = dado(1,6)
print(num)
print("El número arrojado es: ",num)
if num%2==0:
    print("Este número es par")
else:
    print("El número es impar")