c = 'a' < 'b'
print(c)

n = 1
print('uno' if n == 1 else 'no es uno')

x = -5
abs_x = x if x > 0 else -x

print(abs_x)

"""CICLO WHILE"""

lst = [(1, 'a'), (2, 'b'), (3, 'c')]
# Itera en cada elementos de tuplas
for i1, i2 in lst:
    print(i1, i2)

lista = [[1, 2, 3], ['a', 'b', 'c']]
for i1, i2, i3 in lista:
    print(i1, i2, i3)

for e in enumerate(['a', 'b']):
    print(e)


def pot(n, x):
    a = 0
    for p in range(1, n + 1):
        a = p ** x
    return a


print(pot(5, 5))

def pot(x, n):
    f = 1
    for c in range(1, n + 1):
        f = f * x
    return f


def potencia(a, b):
    if x == 0 and n == 0:
        print('Nan')
    elif n < 0:
        print(1 / pot(a, -b))
    else:
        print(pot(a, b))


def fac(n):
    p = 1
    for c in range(1, n + 1):
        p = p * c
        # print(p)
    return p


def coef(r, n):

    if n >= r:
        print(fac(n) / (fac(r) * fac(n - r)))
    else:
        print('Nan')


coef(5,8)
