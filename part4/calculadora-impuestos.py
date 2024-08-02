"""CALCULADORA DE IMPUESTOS """


def calculadora():
    sinImpuesto = float(input('Proporciones el pago sin impuesto:'))
    montoImpuesto = float(input('Proporcione el monto de impuesto:'))
    pagoTotal = sinImpuesto + sinImpuesto * (montoImpuesto / 100)
    return print('Pago con impuesto',pagoTotal)


calculadora()
