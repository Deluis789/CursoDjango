""" Pregunta 1"""
print('Pregunta 1------------')
def es_bisiesto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

def main():
    ano = int(input("Introduce un año: "))
    if es_bisiesto(ano):
        print(f"{ano} es un año bisiesto.")
    else:
        print(f"{ano} no es un año bisiesto.")

if __name__ == '__main__':
    main()

"""Pregunta 2"""

print('Pregunta 2-------------------')
def numeros(a, b):
    if a < b:
        c = a + b
        print(f'Los multiplos de tres son:')
        for i in range(1, c):
            if i % 3 == 0:
                print(i)
    else:
        print('El primer numero debe ser menor que el segundo')

    return c
print(numeros(4, 8))

"""Ejercicio 3"""

print('Pregunta 3-------------------')
def numeros(n):
    lp = []
    lo = []
    ln = []
    if n >= 1:
        lp.append(n)
        print(f'Es todo una lista de verdadero{lp}')
    elif n == 0:
        lo.append(n)
        print(f'Es todo una lista de ceros{lo}')
    elif n < 1:
        ln.append(n)
        print(f'Es todo una lista de negativos{ln}')
    else:
        print('Inserte un valor valido')

numeros(0)





""" ARBOL VERTICAL"""

print('Pregunta 4------------------')
def arbol():
    ar = {'S': ['A','B'], 'A': ['C', 'D'], 'C': ['F'], 'D': ['G', 'H'],'F':[],'G':[],'H':[],
          'B': ['E'], 'E': ['I'],'I':[]}
    return ar
def bva(nin, nob, arb):
    """BUSQUEDA VERTICAL EN ARBOLES"""
    cerrados = []
    abiertos = [nin]
    while abiertos:
        n = abiertos[0]
        cerrados.append(n)
        if n == nob:
            return cerrados
        abiertos.remove(n)
        hijos = arb[ n ]
        abiertos = hijos + abiertos

    return "FALLA"


print(bva('S', 'E', arbol()))