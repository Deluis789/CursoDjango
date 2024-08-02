import math
def cilindro():
    """ CALCULE EL AREA Y EL VOLUMEN """
    a = float(input('Radio = '))
    b = float(input('Altura = '))
    area = 2 * math.pi * a * (a + b)
    volumen = math.pi * a * a * b

    print('Area = ',area,'Volumen = ',volumen)

cilindro()