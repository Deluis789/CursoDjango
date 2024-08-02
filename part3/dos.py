def tres(dc):
    print('Diccionario: ', dc)
    print('Valor de la clave nombre')
    print(dc['nombre'], dc['Edad'])
    print('Modificar el valor de la edad')
    dc['Edad'] = 22
    print(dc)
    print(len(dc))
    print('Añadir un Elemento: ')
    dc['email'] = 'ana@gmail.com'
    print('Determinar si clave esta')
    print('nombre' in dc)
    print(dc.get('nombre'))
    print(dc)
    print(dc.items())
    dc2 = dc.copy()
    dc2['cel'] = '6987456'
    dc.update(dc2)
    print(dc)
    print(dc.popitem())
    print(dc.pop('nombre'))


tres({'nombre': 'ana', 'Edad': 25, 'sexo': 'Femenino'})
