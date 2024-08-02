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
            sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s, %s, %s)'
            valores = (
                       ('Carlos', 'Lara', 'clara21@gmail.com'),
                       ('Laura', 'Perez', 'lau23@gmail.com'),
                       ('Vanesa', 'Quispe', 'vane34@gmail.com')
                       )
            # cursor.execute(sentencia, valores) SOLO INSERTA UN REGISTRO
            """ PARA ACTUALIZAR INSERTAR REGISTROS executemany"""
            cursor.executemany(sentencia, valores)
            # conexion.commit() Lo hace automaticamente con el with
            registros_insertados = cursor.rowcount
            print(f'Registros insertados {registros_insertados}')
except Exception as e:
    print(f'Ocurrio error: {e}')
finally:
    conexion.close()
