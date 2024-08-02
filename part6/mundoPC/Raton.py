from mundoPC.DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    CONTADOR_RATONES = 0

    def __init__(self, dispositivoEntrada, marca):
        Raton.CONTADOR_RATONES += 1
        self._idRaton = Raton.CONTADOR_RATONES
        super().__init__(dispositivoEntrada, marca)

    def __str__(self):
        return f'[Id Raton:{self._idRaton} Dispositivo Entrada:{self.tipoEntrada} Marca:{self.marca}]'


if __name__ == '__main__':
    raton1 = Raton('USB', 'Dragon')
    print(raton1)

