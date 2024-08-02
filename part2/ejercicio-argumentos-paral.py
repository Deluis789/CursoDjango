
""" FUNCION  CON PARAMETROS Y QUE RETORNA VALORES
CALCULO DEL AREA Y VOLUMEN DEL PARALELEPIPEDO"""


def paral2(x, y,z):

    vol = x * y * z
    area = 2 * (x * y + x * z + y * z)
    #print(f'area = {area}, volumen =  {vol}')
    return vol,area

print('volumen y area:',paral2(5,2,6))