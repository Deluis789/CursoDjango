""" FUNCION  SIN PARAMETROS Y QUE RETORNA VALORES
CALCULO DEL AREA Y VOLUMEN DEL PARALELEPIPEDO"""


def paral():
    x = float(input('x = '))
    y = float(input('y = '))
    z = float(input('z = '))
    vol = x * y * z
    area = 2 * (x * y + x * z + y * z)
    print(f'area = {area}, volumen =  {vol}')


paral()
