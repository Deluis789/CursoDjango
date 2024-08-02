
"""" EJERCICIO MAYOR DE 3 NÚMEROS CON UNA FUNCIÓN"""
def mayor1(x, y, z):
    if x > y:
        m = x
    else:
        m = y
    if z > m:
        m = z
    return m


print(mayor1(5, 8, 6))

"""" EJERCICIO MAYOR DE 3 NÚMEROS CON UNA FUNCIÓN"""
# menor
def menor1(x, y, z):
    if x < y:
        m = x
    else:
        m = y
    if z < m:
        m = z
    return m


print(menor1(5, 8, 6))
