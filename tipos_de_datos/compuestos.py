# TIPOS DE DATOS COMPUESTOS Y SUS PRINCIPALES CARACTERISTICAS

#LISTAS
""" 
    * Sus indices empiezan desde el numero 0
    * Las posiciones no son lo mismo que los indices
    * Una lista va entre corchetes 
    * Se puede tomar cualquier valos de la lista 
    * Se pueden modificar los valores de la lista
"""

lista = ["Marco", 20, "Souls", "Antonio"]
print (lista)
print (lista[3])

#TUPLAS
"""
    *Una tupla va entre parentesis
    *Sus valores no pueden ser cambiados
""" 

tupla = ("Marco", 20, "Souls", "Antonio")

# Diccionario
""""
    *Su sintaxis es como un json en J
    *Puede tener n numero de palabras definidas
"""

# CONJUNTO (SET)
"""
    *Va entre llaves
    *Los elementos son desordenados
    *NO podemos modificar elementos ni llamarlos
    *NO permite repetir vaores
"""
conjunto = {"Marco", 20, "Souls", "Antonio", "Marco"}
print(conjunto)

diccionario = {
    'uno' : "Dark souls",
    'dos' : "Blood Borne",
    'tres' : "Sekiro",
    'cuatro' : "Demon",
    'cinco' : "Elden Ring",
    'seis' : "Pinocho"
    
}

print (diccionario)