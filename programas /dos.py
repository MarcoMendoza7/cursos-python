"""
Haz un programa que:

Pida un número n.

Si n es par, imprime: "El número es par".

Si es impar, imprime: "El número es impar".

Luego usa un for para imprimir todos los números del 1 al n.

"""

numero = int(input("Ingrese un número por favor ..."))

r = numero % 2

if r == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")
    
    
# for i in range (numero):
#    print(i)

for i in range (1, numero + 1):
    print(i)
