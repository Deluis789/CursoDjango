from mundoPC.DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    ID_CONTADOR = 0

    def __init__(self, tipoEntrada, marca):
        Teclado.ID_CONTADOR += 1
        self._idTeclado = Teclado.ID_CONTADOR
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f'[id teclado:{self._idTeclado} Tipo Entrada:{self.tipoEntrada} Marca:{self.marca}]'


if __name__ == '__main__':
    teclado1 = Teclado('USB', 'Rysen')
    print(teclado1)
