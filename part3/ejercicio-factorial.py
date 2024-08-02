def fac(n):
    p = 1
    for c in range(1, n + 1):

        p = p * c
        print(p)
    return p


print(f'El factorial es : {fac(5)}')


def pot(n, x):
    a = 0
    for p in range(1, n + 1):
        a = p ** x
        print(a)

    return a


print(f'La potencia es: {pot(4, 4)}')
