# funcion input para procesar entrada del usuario


numero1 = int(input('Digite el primer numero: '))
numero2 = int(input('Digite el segundo numero: '))
resultado = numero1 + numero2
print('El resultado de la suma es:', resultado)

# Ejercicio
mensaje = int(input('Como estuvo tu dia (1 al 10):'))
if mensaje <= 10:
    print('Mi dia estuvo de:', mensaje)
else:
    print('No es un dato correcto')

# Ejericio 2
# Proporciona el titulo
# Proporciona el autor => resupuesta <titulo> fue escrito por <autor>
titulo = input('Proporciona el titulo del libro:')
autor = input('Proporciona el autor del libro:')
print(titulo,'fue escrito por',autor)



