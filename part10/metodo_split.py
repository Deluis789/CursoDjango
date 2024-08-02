""" SPLIT SEPARAR O DIVIDIR LO MISMO QUE EL METODO JOIN PERO INVERSO """

# help(str.split)
# PARA ESTE METODO TIENE QUE HABER UN ESPACION EN LA CADENA
cursos = 'Java Angular Python JS'
lista_cursos = cursos.split()
print(f'Lista de cursos: {lista_cursos}')
print(type(lista_cursos))

# AQUI COMO TIENE LAS COMAS SE VUELVE EN UN ELEMNTO YA QUE NO HAY ESPACION
cursos_separados_coma = 'Java,Python,JS,Spring,Angular'
lista_cursos = cursos_separados_coma.split()
print(f'Lista de cursos: {lista_cursos}')
print(len(lista_cursos))

# OTRA FORMA PARA QUE SE SEPAREN CON COMAS Y SEAN VARIOS ELEMENTOS
cursos_separados_coma = 'Java,Python,JS,Spring,Angular'
lista_cursos = cursos_separados_coma.split(',')
print(f'Lista de cursos: {lista_cursos}')
print(len(lista_cursos))

# CON MAXSPLIT
cursos_separados_coma = 'Java,Python,JS,Spring,Angular'
lista_cursos = cursos_separados_coma.split(',', 2)
print(f'Lista de cursos: {lista_cursos}')
print(len(lista_cursos))