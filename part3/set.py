"""SET NO MANTIENE UNA ORDEN NI POSEE INDICE"""
planetas = {'Marte', 'Jupiter', 'Pluton', 'Venus'}
print(len(planetas))
print(planetas)
# Revisar un elemento si esta presente en el Set
print('Marte' in planetas)
# Agregar un elemento en Set
planetas.add('Tierra')
print(planetas)
# Tampoco acepta datos Duplicados
planetas.add('Tierra')
print(planetas)
# Para eliminar un elemento
# planetas.remove('Tierra')
print(planetas)
# Para eliminar sin arrojar ni un error
planetas.discard('Tierra')
print(planetas)
# Limpiar set
planetas.clear()
# Para eliminar desde memoria
# del planetas
# print(planetas)