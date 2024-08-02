import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)
# print(conexion)   para comproba si se creo bien el objeto conexion
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s' # Parametro posicional placeholder
            id_persona = input('Proporciona el valor de id persona:')
            cursor.execute(sentencia, (id_persona,))   # una coma para que sea una tupla y no una variable
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(f'Ocurrio un error:{e}')
finally:
    conexion.close()

