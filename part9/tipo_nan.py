import math
from decimal import Decimal

# NaN - Not a number (no es un número)
# NaN no es sencible a mayusculas/minusculas
# NaN es un tipo de dato numerico indefinido
a = float(2.0)
print(f'a: {a}')
print(f' Es Nan (not a number)?: {math.isnan(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f' Es Nan (not a number)?: {math.isnan(a)}')