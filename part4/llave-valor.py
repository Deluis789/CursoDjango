def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}:{valor}')


listarTerminos(IDE='Integrated Developement Environment',PK='Primary Key')


# una lista
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


desplegarNombres(['Juan', 'Jose', 'Maria',22,32])
