class MiClase:

    variables_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia


clase = MiClase('Variable instancia')
print(clase.variable_instancia)
print(MiClase.variables_clase)

# Creacion de variable de clase al vuelo
MiClase.variables_clase2 = 'Valor variable clase 2'
print(MiClase.variables_clase2)
print(clase.variables_clase2)