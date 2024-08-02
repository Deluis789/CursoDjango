# Unpacking - Desempquetado
valor1,valor2, valor3 = 1, 2, 3
print(valor1, valor2, valor3)

# para no usar una variable
valor1, _, valor3 = 2, 3, 6
print(valor1, valor3)

valor1, valor2, *valor3 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3)
valor1, valor2, *valor3, valor4, valor5 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3, valor4, valor5)
valor1, valor2, *valor3, valor4, valor5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(valor1, valor2, valor3, valor4, valor5)


def regresa_varios_datos():
    return 1, 2, 3


valor1, valor2, valor3 = regresa_varios_datos()
print(valor1, valor2, valor3)
valor1, *_ = regresa_varios_datos()
print(valor1, _)

# EJEMPLO DE PARTICION
#help(str.partition)

hora, separador, minutos = '17:30'.partition(':')
#print(type(variable))
print(hora, separador, minutos)
