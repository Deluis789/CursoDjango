class Person:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    #METODO GETTER
    @property
    def nombre(self):
        print('Llamando metodo getter nombre')
        return self._nombre
    # METODO SETTER
    @ nombre.setter
    def nombre(self, nombre):
        print('Usando metodo setter')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    # METODO MOSTRAR
    def mostrar_detalle(self):
        print(f'¨Persona:{self._nombre},{self._apellido},{self._edad}')

    def __del__(self):
        print(f'{self._nombre},{self._apellido},{self._edad}')

if __name__ == '__main__':
    persona1 = Person('Luis', 'Diaz', 24)
    print(persona1.mostrar_detalle())
    persona1.nombre = 'Juan'
    print(persona1.nombre)

    print(__name__)