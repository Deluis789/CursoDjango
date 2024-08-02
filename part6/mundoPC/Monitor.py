class Monitor:
    CONTADOR_MONITORES = 0

    def __init__(self, marca, tamano):
        Monitor.CONTADOR_MONITORES += 1
        self._idMonitor = Monitor.CONTADOR_MONITORES
        self._marca = marca
        self._tamano = tamano

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self, tamano):
        self._tamano = tamano

    def __str__(self):
        return f'[Id Monitor:{self._idMonitor} Marca:{self._marca} Tamaño:{self._tamano}]'


if __name__ == '__main__':
    mon1 = Monitor('Samsung', '42px')
    print(mon1)
