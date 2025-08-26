"""
Haz una función llamada es_par(n) que:

Reciba un número entero n.

Devuelva True si es par, False si es impar.

En el programa principal, pide un número al usuario y usa esa función para imprimir:

"Es par" o "Es impar".

"""

# def es_par(numero):
#    resultado = numero % 2
#    if resultado == 0:
#        print(True)
#    else:
#       print(False)

def es_par(numero):
    return numero % 2 == 0
    
numero = int(input("Ingrese un número por favor ... "))

if es_par(numero):
    print("Es par")
else:
    print("Es impar")


