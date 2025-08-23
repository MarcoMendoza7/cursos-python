"""

Ejercicio Integrador

Haz un programa en Python que:

Pida al usuario su nombre y edad.

Use un if para imprimir si es mayor de edad o no.

Pida un número n.

Cree una función es_par(n) que devuelva True si es par, False si es impar.

Use esa función para imprimir si n es par o impar.

Con un for, imprima todos los números del 1 al n, indicando en cada caso si es par o impar (usando la función).

"""

nombre = input("¿Cuál es su nombre?")
edad = int(input("¿Cuál es tu edad?"))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
    
numero = int(input("Ingrese un numero por favor ... "))

def es_par():
    resultado = numero % 2 == 0
    return resultado 

if es_par():
    print("Es par")
else:
    print("Es impar")
    
for i in range (1, numero + 1):
    print(i)


