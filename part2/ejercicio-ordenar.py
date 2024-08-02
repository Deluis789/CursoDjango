"""" EJERCICIO MAYOR DE 3 NÚMEROS CON UNA FUNCIÓN"""
def mayor1(x, y, z):
    if x > y:
        m = x
    else:
        m = y
    if z > m:
        m = z
    return m


print('mayor:',mayor1(5, 8, 6))


"""" EJERCICIO MENOR DE 3 NÚMEROS CON UNA FUNCIÓN"""
# menor
def menor1(x, y, z):
    if x < y:
        m = x
    else:
        m = y
    if z < m:
        m = z
    return m


print('menor:',menor1(5, 8, 6))


"""" EJERCICIO ORDENAR  3 NÚMEROS CON UNA FUNCIÓN"""
#Ordenar
def ordenar (x, y, z):
    mayo = mayor1(x,y,z)
    meno = menor1(x,y,z)
    medio = x + y + z -mayo -menoS
    return mayo, medio, meno,

print('ordenado:',ordenar(12,19,15))




s = 'hellow'
a = 'el' in s
print(a)

print(s [0:2])
print(s [0:-2])
#print(len(' hola'))

print(ord('A'))
print(chr(65))
print('123'.rjust(10))
print('123'.ljust(5))
print('123'.center(10))
print('123'.zfill(8))