from mundoPC.LaboratorioMonitor4 import Monitor
from mundoPC.LaboratorioRaton3 import Raton
from mundoPC.LaboratorioTeclado2 import Teclado


class Computadora(Monitor, Teclado, Raton):
    CONTADOR_COMPUTADORAS = 0

    def __init__(self, nombre, raton):
        self.__raton = raton
        self.idComputadora = Computadora.CONTADOR_COMPUTADORAS
        self.nombre = nombre

    def __str__(self):
        return f'[id Computadora: {self.idComputadora}]{self.__raton}'

""" Prueba """
if __name__ == '__main__':
    comp1 = Computadora('Gamer','Gamer','32pulg','USB')
    print(comp1)