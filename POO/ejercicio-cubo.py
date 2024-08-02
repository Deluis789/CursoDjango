class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def volumen_cubo(self):
        return self.ancho * self.alto * self.profundo


anchoInput = int(input('Proporciona el ancho:'))
altoInput = int(input('Proporicona el Alto:'))
profundoInput = int(input('Proporciona la Profundidad:'))
cubo1 = Cubo(anchoInput, altoInput, profundoInput)
print(f'Volúmen del cubo:{cubo1.volumen_cubo()}')