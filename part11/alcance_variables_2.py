def funcion_externa():
    variable_local_externa = 'Variables local externa'

    def funcion_anidada():
        variable_local_anidada = 'Variable local anidada'

        nonlocal variable_local_externa
        variable_local_externa = 'Nuevo valor variable local externa'

    funcion_anidada()
    print(f'Valor varaible local externa: {variable_local_externa}')


funcion_externa()