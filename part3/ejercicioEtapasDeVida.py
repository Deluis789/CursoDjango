""" ETAPAS DE LA VIDA """
edad = int(input('Proporciona tu edad: '))
mensaje = ''
if 0 < edad <= 10:
    mensaje = 'La infancia es increible ....'
elif 10 < edad <= 20:
    mensaje = 'Muchos cambios y muchos estudios..'
elif 20 < edad <= 30:
    mensaje = 'Amor y comienza el trabajo.'
else:
    mensaje = 'Etapa de vida no reconocida'

print(f'La edad es,{edad},{mensaje}')