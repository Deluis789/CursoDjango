from math import sqrt
""" FUNCION QUE RETORNA EL MAYOR DE TRES NUMEROS """
def mayor(x, y, z):
    if x > y:
        m = x
    else:
        m = y
    if z > m:
        m = z
    return m


print(mayor(23, 6, 9))

""" FUNCION QUE RETORNA EL MENOR DE TRES NUMEROS """
def menor(x, y, z):
    if x<y and x<z:
        m = x
    elif y < z:
        m = y
    else:
        m = z
    return m

print(menor(8, 5, 4))

""" FUNCION QUE ORDENA TRES NUMEROS"""
def ordenar(x, y, z):
    may = mayor(x, y, z)
    men = menor(x, y, z)
    medio = x+y+z-may-men
    return men, medio, may

print(ordenar(6,12,9))

def fac(n):
    """ CALCULA FACTORIAL DE UN NUMERO """
    f = 1
    c = 1

    while(c <= n):
        f *= c
        c += 1
    return f

print(fac(6))

"""POSICION DE UN CUADRANTE QUE RECIBA LAS CORDENADAS DE (x, y)EN EL PLANO CARTESIANO"""
def posicion(x, y):
    """Posicion en el plano"""
    if x>0 and y>0:
        print('Cuadrante I')
    elif x==0 and y>0:
        print('Eje Y+')
    elif y==0 and x>0:
        print('Eje X+')
    elif x<0 and y>0:
        print('Cuadrante II')
    elif x<0 and y<0:
        print('Cuadrante III')
    elif x>0 and y<0:
        print('Cuadrante IV')
    elif x==0 and y<0:
        print('Eje Y-')
    elif y==0 and x<0:
        print('Eje X-')
    else:
        print('Punto 0')


print(posicion(0, -5))

"""FUNCION ECUACION QUE RECIBA a, b ,c DE UNA ECUACION DE 2DO GRADO QUE MUESTRE RAIZ"""
def ecuacion(a, b, c):
    if a == 0 and b == 0 and c == 0:
        print('INDETERMINADO')
    elif a == 0 and b==0:
        print('INCONSISTENTE')
    elif a == 0:
        print('RAIZ = ', -c/b)
    else:
        raiz1 = (-b+(b * b - 4 * a * c) ** (1 / 2)) / (2 * a)
        raiz2 = (-b-(b * b - 4 * a * c) ** (1 / 2)) / (2 * a)
        print(f'Raiz = {raiz1}')
        print(f'Raiz2 = {raiz2}')

ecuacion(2, 3, 5)