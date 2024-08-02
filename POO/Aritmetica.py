class Aritmetica:
    """
    Clase aritmetica para suma, restar ,etc
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(5, 6)
print('Suma:', aritmetica1.sumar())
print('Resta:', aritmetica1.restar())
print('Multiplicacion:', aritmetica1.multiplicar())
print(f'Division:{aritmetica1.dividir():.2f}')
