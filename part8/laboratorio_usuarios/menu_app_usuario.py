from laboratorio_usuarios.usuario import Usuario
from laboratorio_usuarios.usuario_dao import UsuarioDao
from laboratorio_usuarios.logger import log

opcion = None
while opcion != 5:
    print('Opciones:')
    print('1. Listar usuarios')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opcion = int(input('Escribe tu opcion (1-5): '))
    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            # log.info(usuario)  # PARA QUE NO MUESTRE TODOS LOS MENSAJES EN DEBUG CAMBIA EL LOGGER EN INFO
            print(usuario)
    elif opcion == 2:
        username_var = input('Escriba el nombre del usuario:')
        password_var = input('Escriba el password:')
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertados = UsuarioDao.insertar(usuario)
        log.info(f'Usuarios Insertados:{usuarios_insertados}')
    elif opcion == 3:
        id_var = int(input('Ingrese el id_usuario a modificar: '))
        username_var = input('Escriba el nombre de usuario a modificar: ')
        password_var = input('Escriba el password a modificar: ')
        usuario = Usuario(id_var, username_var, password_var)
        usuarios_modificados = UsuarioDao.actualizar(usuario)
        log.info(f'Usuario Modificado: {usuarios_modificados}')
    elif opcion == 4:
        id_var = int(input('Escriba el id_usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_var)
        usuarios_eliminados = UsuarioDao.eliminar(usuario)
        log.info(f'Usuario eliminado: {usuarios_eliminados}')
else:
    log.info('Salimos de la aplicación')
