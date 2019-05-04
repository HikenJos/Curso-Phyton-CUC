import math
# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
# -*- Esto es un comentario lineal -*-

""" Esto es un
    Comentario de un parrafo """

a = 5
# -*- VARIABLES -*-
print("Hola Mundo")

x = "TEXTO"
z = 4.5
a = True
b = False
c = 4 + 5j

print(x, z, a, b, c)

print(type(b))


# -*- CONVERCIONES DE TIPO DE DATOS -*-

x = int(2)
print(x)

x = int(2.8)
print(x)

# -*- FLOTAT(S) -*-

x = float(2)
print(x)

# -*- CADENAS -*-

x = str(2)
print(x)

# -*- MANEJO DE CADENAS DE TEXTO -*-

cad = "Hello World"
print(cad[0])
print(cad[0:5])
print(len(cad))
print(cad.lower())
print(cad.upper())
print(cad.replace('l', 'y'))
print(cad.split(" "))
cad = cad.strip()
print(cad)

# -*- OPERACIONES -*-
a = 4
b = 3
c = a // b  # division entera
c = a ** b  # -*- raiz -*-
c = math.sqrt(a)  # Exponente ( intercambia con la linea de arriba)
c = a % b  # Mod


# CAPTURA POR CONSOLA

print("Digite su nombre")
nombre = input()
print("Hola "+nombre+"!")

print("Digite a")
a = input()
print("Digite b")
b = input()

if a > b:
        print(a, " Es mayor que ", b)
else:
        print(b, "Es mayor que ", a)

if a > b:
    if b > 1:
        print(b, "Es mayor que 1 y es mayor que ", a)


# EJERCICIO CONDICIONAL


print("Digite su edad")

edad = input()
x = int(edad)

if x >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")
    
    
# VECTORESS!!!!!!!!!!!!!!
    
v = ["hola", "mundo", 4, 3, True, ["Otro", "Array"]]    
    
