"""
Ejercicio Rectangulo
Proporciona el alto <alto>
Proporciona el ancho <ancho>
Area : <area>
Perimetro: <perimetro>
"""
alto = int(input('Proporciona el alto del rectangulo: '))
ancho = int(input('Proporciona el ancho del rectangulo: '))

area = alto * ancho
perimetro = (alto + ancho) * 2

print(f'Area: {area}')
print(f'Perimetro: {perimetro}')
