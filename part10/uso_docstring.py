class MiClase:
    '''
    Este es un ejemplo de la documentacion
    de nuestra clase
    '''

    def __init__(self):
        '''
        Metodo de inicio de nuestra
        clase
        '''

    def mi_metodo(self, param1, param2):
        '''
        Esta  es la documentacion de nuestro metodo
        :param param1: Este es el parametro1
        :param param2: Este es el parametro2
        :return: Este es el valor de retorno
        '''


# help(MiClase)
print(MiClase.__doc__)
print(MiClase.__init__.__doc__)
'''AQUI SE SABE QUE ES UN OBJETO'''
print(MiClase.mi_metodo.__doc__)
print(MiClase.mi_metodo)
print(type(MiClase.mi_metodo))