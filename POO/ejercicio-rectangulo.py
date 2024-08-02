class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


baseInput = int(input('Proporcione la base:'))
alturaInput = int(input('Proporcione la altura:'))
rectangulo1 = Rectangulo(baseInput, alturaInput)
print(f'Area del Rectangulo:{rectangulo1.area()}')
