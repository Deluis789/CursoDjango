# Profundizando diccionarios
# Los dic guardan un orden a diferencia de un  set
diccionario = {'Nombre': 'Juan','Apellido': 'Perez', 'Edad': 28 }
print(diccionario)
# Los dic son mutables, pero las llaves deben ser inmutables
# diccionario = {[1, 2]: 'valor1'} // no puede ser una llave una lista
# diccionario = {(1, 2): 'valor1'} //Pero si puede ser una tupla ya que es inmutable
# print(diccionario)

# agregar una llave si no se encuentra al diccionario
diccionario['Departamento'] = 'Sistemas'
print(diccionario)
# Modificar valores
# No hay valores duplicados en las llaves de un diccionario(si ya existe se reemplaza)
diccionario['Nombre'] = 'Juan carlos'
print(diccionario)
# Recuperar un valor indicando una llave
print(diccionario['Nombre'])
# si no encuentra la llave lanza una execepcion
print(diccionario['Nombre'])
# Metodo get recupera una llave, y si en caso no existe No lanza excepcion
# Ademas podemos regresar un valor en caso que no exista la llave
print(diccionario.get('Nombres', 'No se encontro la llave.'))
# setdefault si modifica el diccionario, ademas se puede agregar un valor default
nombre = diccionario.setdefault('Nombres', 'Valor por defecto')
print(nombre)
print(diccionario)
# Imprimir con pprint
from pprint import pprint as pp
# help(pp)
pp(diccionario, sort_dicts=False)
