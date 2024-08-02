# archivo = open('C:\\Users\\luisc\\OneDrive\\Área de Trabalho\\CursoPython\\part7\\prueba.txt', 'r', encoding='utf8')
archivo = open('prueba.txt', 'r', encoding='utf8')
# print(archivo.read())  # para leer Todo
# leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))
# leer lineas completas
# print(archivo.readline())

# Iterar el archivo
# for linea in archivo:
#     print(linea)

# Leer lineas
# print(archivo.readlines())

# Accede a una linea de la lista
# print(archivo.readlines()[0])

# Abrimos un nuevo archivo
# a - anexar informacion
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('Se ha terminado el proceso de leer y copiar')

