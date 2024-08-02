def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Jorge', 'Luis', 'Maria', 'Karla')


# Ejercicio sumar todos los numero con *args
def sumarTodo(*args):
    resultado = 0
    for valor in args:
        # resultado = resultado + valor  ->Seria lo mismo que esta linea
        resultado += valor
    return resultado


# Llamada a la funcion
print('La suma total es:', sumarTodo(5, 6, 3, 7, 8))


# Ejercicio multiplicar todos los numero con *args
def multiplicarTodo(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado


print('La multiplicacion total es:', multiplicarTodo(5, 6, 2, 2))
