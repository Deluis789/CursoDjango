class Person:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona:{self.nombre}, {self.apellido}, {self.edad}')


persona1 = Person('Luis', 'Diaz', 25)
persona1.mostrar_detalle()
persona1.telefono = '69874561'
# Agregamos el atributo telefono a la persona 1
print(persona1.telefono)
# Otra forma de mostrar y acceder al metodo
# Person.mostrar_detalle(persona1)
persona2 = Person('Alicia', 'Torrez', 22)
persona2.mostrar_detalle()
