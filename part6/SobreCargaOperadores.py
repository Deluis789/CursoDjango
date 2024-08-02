a = [1, 2, 30]
b = [6, 9]
print(a + b)


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad


persona1 = Persona('Rony', 20)
persona2 = Persona('Usnayo', 14)
print(persona1 + persona2)
print(persona1 - persona2)