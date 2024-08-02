class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad



persona1 = Persona('Jorge', 'Diaz', 23)
print(f'Persona 1: {persona1.nombre},{persona1.apellido},{persona1.edad}')
# Modificacion de valores de atributos
persona1.nombre = 'Luis'
persona1.apellido = 'Rios'
print(f'Persona 1: {persona1.nombre},{persona1.apellido},{persona1.edad}')
persona2 = Persona('Maria', 'Cruz', 25)

print(f'Persona 2: {persona2.nombre},{persona2.apellido},{persona2.edad}')
