"""DICCIONARIO ESTA SE CONFORMA (LLAVE,VALOR) NO TIENE INDICE"""
# Declaracion de tipo diccionario
diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programing',
    'DBMS': 'Database Management System'
}
# Para imprimir ambos valores tanto como llaves y valores
for terminos, valores in diccionario.items():
    print(terminos, valores)

# Para imprimir las llaves de un diccionario
for llaves in diccionario.keys():
    print(llaves)
# Para imprimir los valores de un diccionario
for valores in diccionario.values():
    print(valores)
# Para agregar un nuevo elemento al diccionario
diccionario['PK'] = 'Primary Key'
print(diccionario)
# Para eliminar un elemento del diccionario
diccionario.pop('IDE')
print(diccionario)
# Para limpiar el diccionario y que la variable quede vacia
diccionario.clear()
print(diccionario)
# Para eliminar de la memoria la variable
del diccionario
# print(diccionario)
# # Saber el largo del diccionario
# print(len(diccionario))
# # Acceder a un elemento
# print(diccionario['IDE'])
# # Otra forma de recuperar un elemento
# print(diccionario.get('OOP'))
# # Modificando elementos
# diccionario['IDE'] = 'Integrated Completed'
# print(diccionario)
a = 'Hola'
print(a)