# cadena = 'hola'
# # FOR O FOREACH
# for letra in cadena:
#     print(letra)


# """ENCONTRAR LA PRIMERA LETRA A Y LUEGO ROMPER EL CICLO"""
#
# for letras in 'Holanda':
#     if letras == 'a':
#         print(letras)
#         break
# else:
#     print('Fin ciclo for')

"""IMPRIMIR LOS NUMEROS PARES"""
for i in range(7):
    if i % 2 == 0:
        print(f'Valores pares,{i}')
"""IMPRIMIR LOS NUMEROS IMPARES"""
for i in range(7):
    if i % 2 == 0:
        continue
    print(f'valores Impares,{i}')
