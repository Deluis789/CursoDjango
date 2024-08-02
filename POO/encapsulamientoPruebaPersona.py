from encapsulamiento import Person

print('Creacion de objetos'.center(50, '-'))
persona1 = Person('Karla', 'Gomez', 30)
persona1.mostrar_detalle()
print('Eliminacion de objetos'.center(50, '*'))
del persona1
