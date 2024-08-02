class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto


class Color:
    def __init__(self, color):
        self.color = color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super().__init__()
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho


""" TEST PRINCIPAL """

cuadrado1 = Cuadrado(5, 'Rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(cuadrado1.calcular_area())


# MRO - Method Resolution Order
print(Cuadrado.mro())