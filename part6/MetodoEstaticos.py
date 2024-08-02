class MiClase:

    variables_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
# Este metodo estatico no puede acceder a contexto dinamico ni a variables
# ni metodos de instancias
    @staticmethod
    def metodo_estatico():
        print(MiClase.variables_clase)


MiClase.metodo_estatico()