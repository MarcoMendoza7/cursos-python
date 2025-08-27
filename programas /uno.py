"""Ejercicio 1

Haz un programa en Python que:
Guarde tu nombre y edad en variables.
Imprima el mensaje:
Extra: imprime también si eres mayor de edad (usa un if).

"""

nombre = input("¿Cuál es tu nombre?")
edad = int(input("¿Cuál es tu edad?"))

print("Hola mi nombre es", nombre, "y tengo", edad, "años")

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    




