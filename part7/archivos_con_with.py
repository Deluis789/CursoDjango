# with open('prueba.txt', 'r', encoding='utf8') as archivo:
from ManejoArchivos import ManejoArchivos

# Con la palabra with manda a llamar el metodo enter de Manejo de arhivos
with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
# Se manda a llamar el metodo exit
