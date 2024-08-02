from EjercicioHerenciaMultiple import Cuadrado
from EjercicioHerenciaMultiple import Rectangulo

print('Creacion de objeto cuadrado'.center(50,'*'))
cuadrado1 = Cuadrado(-5, 'azul')
cuadrado1.alto = 6
print(f'Cálculo del área cuadrado: {cuadrado1.area_cuadrado()}')
print(cuadrado1)

print('Creacion de objeto rectangulo'.center(50,'*'))
rectangulo1 = Rectangulo(4, 'fuxia')
print(f'Cálculo del área rectangulo:  {rectangulo1.area_rectamgulo()}')
print(rectangulo1)