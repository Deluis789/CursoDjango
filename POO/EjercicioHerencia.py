class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'[Vehiculo: {self.color}, {self.ruedas}]'


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'[Coche:{self.velocidad}] [{super().__str__()}]'


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'[Tipo: {self.tipo}] [{super().__str__()}]'


vehiculo1 = Vehiculo('Rojo', 'Dos')
print(vehiculo1)
coche1 = Coche('Verde', 'Dos', '70km')
print(coche1)
bicicleta1 = Bicicleta('Plomo', 'Dos', 'Urbana')
print(bicicleta1)