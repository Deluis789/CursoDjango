""" BUSQUEDA EN ARBOLES """


def arbol():
    ar = {'S':['A'], 'A':['C', 'D'], 'C': ['F'], 'D': ['G', 'H'],
          'B': ['E'], 'E': ['I']}
    return ar


def bha(nin, nob, arb):
    """BUSQUEDA HORIZONTAL EN ARBOLES"""
    cerrados = []
    abiertos = [nin]
    while abiertos:
        n = abiertos[0]
        cerrados.append(n)
        if n == nob:
            return cerrados
        abiertos.remove(n)
        hijos = arb[ n ]
        abiertos = abiertos + hijos

    return "FALLA"


print(bha('S', 'D', arbol()))


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
        hijos = arb[n]
        abiertos = hijos + abiertos

    return "FALLA"


print(bva('S', 'D', arbol()))