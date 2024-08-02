import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)
# print(conexion)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores=(
                    ('David', 'Suarez', 'jcjuarez34x@gmail.com', 1),
                    ('Melania', 'Erner', 'melan@gmail.com', 2)
            )
            # cursor.execute(sentencia, valores) PARA ACTUALIZAR UN SOLO REGISTRO
            """ PARA ACTUALIZAR VARIOS REGISTRO executemany"""
            cursor.execute(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrio error modificar: {e}')
finally:
    conexion.close()
