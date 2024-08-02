from laboratorio_usuarios.cursor_del_pool import CursorPool
from laboratorio_usuarios.logger import log
from laboratorio_usuarios.usuario import Usuario


class UsuarioDao:
    """ DAO - Data Acces Object para la tabla de usuario
    CRUD - Create - Read - Update - Delete para la tabla de Usuario
    """

    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERT = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _UPDATE = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _DELETE = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            log.debug(f'Seleccionando usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERT, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorPool() as cursor:
            log.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._UPDATE, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorPool() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._DELETE, valores)
            return cursor.rowcount


# if __name__ == '__main__':
#     usuario1 = Usuario(1, 'Juanes', '23234')
#     usuario_actualizados = UsuarioDao.actualizar(usuario1)
#     log.debug(f'Personas actualizadas:{usuario_actualizados}')

