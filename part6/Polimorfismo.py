class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado [Nombre:{self.nombre}, Sueldo: {self.sueldo}]'

    def mostrar_detalle(self):
        return self.__str__()


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f'Gerente[Departamento: {self.departamento}] {super().__str__()}'


""" TEST """


def imprimir_detalles(objeto):
    print(objeto.mostrar_detalle()) # LLama al metodo STR en esta linea
    print(type(objeto))
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado('Luis', 1500)
imprimir_detalles(empleado)
gerente = Gerente('Maria', 2330, 'Sistemas')
imprimir_detalles(gerente)