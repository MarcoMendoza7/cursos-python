"""

Haz un programa que:

Pida al usuario 3 nombres y los guarde en una lista.

Imprima

"""

nombres = []

for i in range(3):
    nombre = input(f"Ingrese su nombre{i + 1}")
    nombres.append(nombre)
    
print(nombres)
