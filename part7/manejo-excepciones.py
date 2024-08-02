from excepcionPersonalizada import NumerosIdenticosException
resultado = None
try:
    a = int(input('Primer número:'))
    b = int(input('Segundo número:'))
    if a == b:
        # Raise nos permite lanzar o arrojar una excepcion
        raise NumerosIdenticosException('Numeros identicos')
    resultado = a / b
except ZeroDivisionError as e:
    print(f'ZeroDivionError - Ocurrio un error: {e}, {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {e}, {type(e)}')
except ValueError as er:
    print(f'ValueError - Ocurrio un error: {e}, {type(er)}')
except Exception as e:
    print(f'Exeception - Ocurrio un error: {e}, {type(e)}')

    """------BLOQUES OPICIONALES---"""
# Se ejecuta cuando no ocurre errores
else:
    print('No ocurrio ninguna execepcion')
# Siempre se ejecuta al ultimo
finally:
    print(f'Ejecucion del bloque finally')
print(f'Resultado: {resultado}')
print('Continuamos.....')