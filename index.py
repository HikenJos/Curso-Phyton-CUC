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

aux = v[-1][0]  # ACCEDER A UN VECTOR DENTRO DE OTRO (INFINITAMENTE)
print(aux)

v2 = ["hola", "mundo"]

v3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

v4 = range(1, 201)

v5 = range(201)

for x in v2:
    print(x)


# MODIFICAR ELEMENTO

v2[1] = "LosLannisterSiemprePaganSusDeudas"

v2.remove("hola")  # ELIMINAR ELEMENTO

v2.pop()  # ELIMINAR  ULTIMO ELEMENTO
v2.pop(1)

v.append(5)  # INSERTAR ELEMENTO
v.insert(1, "Roberto")  # INSERTAR ELEMENTO ANTES DE

v.index('mundo')  # SABER LA POSSICION DE ALGO

len(v)  # TAMAÑO DEL VECTOR

v.count('mundo')  # NUMERO DE VECES DE UN OBJETO EN UN VECTOR

# ORDENAR UN VECTOR

a = [5, 9, 6, 7, 11]
a.sort()

res = 9 in a  # PREGUNTAR SI EXISTE UN ELEMENTO EN UN VECTOR
print(res)

# RECIRRER VECTOR

v = v[2:5]

# RECORRER CON SALTO

a = [5, 9, 6, 7, 11]

for x in a[0:5:2]:

# EJERCICIO

suma = 1
print("Digite limite de sumatoria")
lim = input()
x = int(lim)
vec = []
for z in vec[1:x]:
    suma = suma+1

print(suma)


# MIENTRAS QUE

i = 2

while i < 5:
    print(i)
    i = i + 1


# FUNCIONES

def hola_mundo():
    print("hola mundo")


hola_mundo()


def alCuadrado(numero):
    return numero ** 2
