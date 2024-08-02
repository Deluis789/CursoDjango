class FiguraGeometrica:
    def __init__(self, alto, ancho):
        if self._validar_valor(alto):
            self.alto = alto
        else:
            self.alto = 0
            print(f'Valor erroneo alto: {alto}')
        if self._validar_valor(ancho):
            self.ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self.alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print('Valor Erroneo Alto.')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print('Valor Erroneo Ancho')
    def __str__(self):
        return f'[Alto y Ancho:{self._alto},{self._ancho}]'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False

class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'[Color:{self._color}]'


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area_cuadrado(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area_rectamgulo(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'


""" MAIN TEST"""
# rectangulo1 = Rectangulo(6, 'Rojo')
# print(''.center(50,'-'))
# print(rectangulo1)
# print(f'El area del rectangulo es: {rectangulo1.area_rectamgulo()}')
#
# cuadrado1 = Cuadrado(7, 'Verde')
# print(''.center(50,'-'))
# print(cuadrado1)
# print(f'El area del cuadrado es: {cuadrado1.area_cuadrado()}')

