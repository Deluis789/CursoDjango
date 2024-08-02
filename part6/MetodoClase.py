class MiClase:

    variables_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
# Este metodo estatico no puede acceder a contexto dinamico ni a variables
# ni metodos de instancias
    @staticmethod
    def metodo_estatico():
        print(MiClase.variables_clase)

    @classmethod
    def metodo_clase(cls):
        #Accedemos a la variable de la clase
        print(cls.variables_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variables_clase)
        print(self.variable_instancia)


MiClase.metodo_clase()
objeto1 = MiClase('Variable instancia..')
objeto1.metodo_clase()
objeto1.metodo_estatico()
print(''.center(50,'*'))
print(objeto1.metodo_instancia())
