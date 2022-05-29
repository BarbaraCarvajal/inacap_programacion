"""Crear un programa que contemple lo siguiente: 
- Debe utilizar estructura de control de repetición (ciclo). 
- El programa debe ser capaz de leer 3 valores, pero: 
El primero solo debe ser par. 
El segundo solo debe ser negativo. 
El tercero solo debe ser 0. 
- No puede leer el nuevo valor si aún no supera el anterior. 
- Debe  contar  cuanto  le  cuesta  a  llegar 
 a  obtener  los  3  valores  que  exige,  arrojando  una  estadística  al 
respecto."""

def muchas_weas():
    sw = True
    while sw == True:
        valor1 = int(input("Ingrese el primer valor: "))
        if valor1 %2 == 0:
            while sw == True:
                valor2 = int(input("Ingrese el segundo valor: "))
                if valor2 < 0:
                    while sw == True:
                        valor3 = int(input("Ingrese el tercer valor: "))
                        if valor3 == 0:
                            promedio = valor1 + valor2 /2
                            print(f"El promedio de {valor1}, {valor2} y {valor3} es: {promedio}")
                            sw = False
muchas_weas()