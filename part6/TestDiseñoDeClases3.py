from DiseñoDeClases import Producto
from DiseñoDeClases2 import Orden

producto1 = Producto('Camisa', 150.0)
producto2 = Producto('Pantalon', 200.0)
producto3 = Producto('Chompas', 800.0)
producto4 = Producto('Blusa', 175.0)
productos = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos)
orden1.agregar_producto(producto3)
orden2 = Orden(productos2)
print(orden1)
print(f'Total de la orden1: {orden1.calcular_total()}')
print(orden2)
print(f'Total de la orden2: {orden2.calcular_total()}')
