"""Haz un programa que:

Pida el nombre y edad de la persona.
Guarde en un objeto Persona.
Lo meta en una lista.
Recorra la lista y los salude.

"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

personas = []

for i in range(3):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    personas.append(Persona(nombre, edad))

for p in personas:
    p.saludar() 
    
