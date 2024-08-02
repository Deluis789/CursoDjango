# Ejercicio Operador AND
valor = int(input('Ingrese el valor:'))

if (valor >= 0) and (valor <= 10):
    print(f'Si esta en el rango el valor {valor}')
else:
    print(f'No se encuentra en el rango el valor {valor}')
# Ejercicio Operador OR
vacaciones = False
diaDescanso = False

if vacaciones or diaDescanso:
    print(f'Si puede asistir al juego')
else:
    print(f'No podra asistir al juego')

# Ejercicio Operador not
if not (vacaciones or diaDescanso):
    print(f'Si puede asistir al juego')
else:
    print(f'No podra asistir al juego')
