from mundoPC.Computadora import Computadora
from mundoPC.Monitor import Monitor
from mundoPC.Raton import Raton
from mundoPC.Teclado import Teclado


class Orden:
    CONTADOR_ORDENES = 0

    def __init__(self, computadoras):
        Orden.CONTADOR_ORDENES += 1
        self._idOrden = Orden.CONTADOR_ORDENES
        self._computadora = computadoras

    @property
    def computadora(self):
        return self._computadora

    @computadora.setter
    def computadora(self, computadora):
        self._computadora = computadora

    def agregar_computadora(self, computadora):
        return self._computadora.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadora:
            computadoras_str += computadora.__str__()
        return f'''Orden:{self._idOrden} 
        Computadoras: {computadoras_str}
        '''


if __name__ == '__main__':
    monitor1 = Monitor('Samsung', '45px')
    teclado1 = Teclado('USB', 'Dragons')
    raton1 = Raton('USB', 'Fex')
    compu1 = Computadora('Hp', monitor1, teclado1, raton1)
    Orden1 = Orden(compu1)
    print(Orden1)

