"""EJERCICIO 1 ITERAR DEL 0 AL 10 DIVISIBLES ENTRE TRES"""
print('Ejercicio 1')
i = 0
for i in range(11):
    if i % 3 == 0:
        print(i)
print('Ejercicio 2')
"""EJERCICIO 2 CREAR UN RANGO DE NUMEROS DE 2 A 6 E IMPRIMELOS"""
# a = range(2, 7)
# for i in a:
#     print(i)

for i in range(7):
    if 0 <= i < 2:
        continue
    print(i)
print('Ejercicio 3')
"""EJERCICIO 3 CREAR UN RANGO DE 3 A 10 PERO CON INCREMENTO DE 2 EN 2 """
# for i in range(11):
#     if 0 <= i < 3:
#         continue
#     if i % 2 != 0:
#         print(i)

b = range(3, 11, 2)
for i in b:
    print(i)




