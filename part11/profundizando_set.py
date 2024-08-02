# Profundizar en set
# Un set es una coleecion de elementos únicos y es mutable
# Los elementos de un set deben ser inmutables
# conjunto = {[1, 2], [3, 4]}
conjunto = {'Juan', True, 18.0}
print(conjunto)
# set vacio
# conjunto = {} genera un dict vacio
# print(type(conjunto))
# set vacio correcto
conjunto = set()
print(type(conjunto))
# Mutable
conjunto.add('Juan')
print(conjunto)
# Contiene valores unicos no pueden tener dos iguales
# Crear un set a partir de una iterable
conjunto = set([4, 5, 6, 1, 4])
print(conjunto)
# Podemos agregar mas elementos o incluso otros set
conjunto2 = {100, 230, 222, 300, 300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20, 30, 32, 55, 23])
print(conjunto)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
# Verificar igualdad
print(f'Es igual en contenido: {conjunto == conjunto_copia}')
print(f'Es la misma referencia: {conjunto is conjunto_copia}')

# Operaciones conjuntos con set
# Personas con distintas caracteristicas
pelo_negro = {'Juan', 'Karla', 'Pedro', 'Maria'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'Maria'}
# Todos con ojos_cafe y pelo rubio (union) no se repiten los elemntos
print(ojos_cafe.union(pelo_rubio))

# Intersection solo las personas con ojo cafe y pelo rubio (conmutativa)
print(ojos_cafe.intersection(pelo_rubio))

# Funcion (Difference) pelo negro sin ojos cafe (no es conmutativa)
# las personas que se encuentran en el primer set pero no en el segundo

print(pelo_negro.difference(ojos_cafe))

# (Symmetric Difference) simtetrica diferencia  (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))

""" PREGUNTAS CON SET"""
print('Preguntas con set'.center(50, '*'))
# Preguntar si un set esta contenido en otro (subset)
# revisamos si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issubset(pelo_negro))
# Preguntar si un set contiene a otro set (superset)
# revisar si los elemntos del primer set estan contenidos en el segundo set
print(menores_30.issuperset(pelo_negro))
# Preguntas si los de pelo negro no tienen pelo rubio (distjoin)
print(pelo_negro.isdisjoint(pelo_rubio))