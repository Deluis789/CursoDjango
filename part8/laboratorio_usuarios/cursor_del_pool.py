from laboratorio_usuarios.logger import log
from laboratorio_usuarios.conexion import Conexion


class CursorPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Inicio del método with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_exepcion, valor_execepcion, detalle_execepcion):
        log.debug(f'Se ejecuta método __exit__')
        if valor_execepcion:
            self._conexion.rollback()
            log.error(f'Ocurrio una execepcion: {valor_execepcion} {tipo_exepcion} {detalle_execepcion}')
        else:
            self._conexion.commit()
            log.debug(f'Commit de la transacción')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == '__main__':
    with CursorPool() as cursor:
        log.debug(f'Dentro del bloque with')
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())