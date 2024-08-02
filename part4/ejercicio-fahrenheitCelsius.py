# Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


celsius = float(input('Proporcione su valor en celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius:.2f} C a F: {resultado:.2f}')


# Funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


fahrenheit = float(input('Proporcione el valor en fahrenheit:'))
res = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit:.2f} F a C: {res:.2f}')



