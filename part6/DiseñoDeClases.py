class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f'Id producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'


# Para que se ejecute solo en este modulo
if __name__ == '__main__':
    producto1 = Producto('Camisa', 150.0)
    print(producto1)
    producto2 = Producto('Pantalon', 200.0)
    print(producto2)