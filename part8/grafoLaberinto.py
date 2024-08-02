""" GRAFO DE LABERINTO """


def laberinto():
    ar = {'s': ['a'], 'a': ['s', 'b', 'c'], 'b': ['a', 'd', 'j'], 'c': ['a', 'e', 'f'],
          'd': ['b'], 'j': ['b', 'g', 'i'], 'e': ['c', 'i', 'f'], 'f': ['c', 'e', 'i'],
          'g': ['j'], 'i': ['j', 'f', 'e']}
