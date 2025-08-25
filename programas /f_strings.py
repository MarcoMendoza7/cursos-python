"""
Haz un programita que pida nombre y edad, y que imprima usando f-strings:

Tu nombre tiene <número_de_letras> letras y en 5 años tendrás <edad+5>.

"""

name = input("NOMBRE ...")
age = int(input("EDAD ..."))

print(f"Tu nombre es {name} y tienes {age} de edad")

print (f"Tu nombre tiene {len(name)} letras y en 5 años tendras {age + 5}")