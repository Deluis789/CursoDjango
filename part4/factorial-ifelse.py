def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)


numero = int(input('Inserte el número:'))
print(f'El fatorial de {numero} es {factorial(numero)}')