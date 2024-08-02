from mundoPC.Monitor import Monitor
from mundoPC.Raton import Raton
from mundoPC.Teclado import Teclado


class Computadora:
    CONTADOR_COMPUTADORAS = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.CONTADOR_COMPUTADORAS += 1
        self._idComputadora = Computadora.CONTADOR_COMPUTADORAS
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'''\nNombre:{self._nombre} Id computadora:{self._idComputadora}
        Monitor:{self._monitor}
        Teclado:{self._teclado}
        Raton:{self._raton}
        '''


if __name__ == '__main__':
    monitor1 = Monitor('Samsung', '45px')
    teclado1 = Teclado('USB', 'Dragons')
    raton1 = Raton('USB', 'Fex')
    compu1 = Computadora('Hp', monitor1, teclado1, raton1)
    print(compu1)
