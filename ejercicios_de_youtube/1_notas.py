""" 1 - Programa que toma las 3 notas de un estudiante y diga la nota
 final del curso. Tenga en cuenta que la primera y segunda nota valen el 30% de la nota
 final. La tercera nota vale el 40%.
"""
# def calcular_notas():

def calcular_nota(nota1,nota2,nota3):
    promedio = (nota1*0.3)+(nota2*0.3)+(nota3*0.4)
    return print(f"El promedio de notas es: {promedio}")

n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))
calcular_nota(n1,n2,n3)

