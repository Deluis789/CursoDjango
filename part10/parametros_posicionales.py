# PROFUNDIZANDO STR

# dar formato a un str
nombre = 'Juan'
edad = 28
mensaje_con_formato = 'Mi nombre es %s y tengo %s años:' % (nombre, edad)
print(mensaje_con_formato)

# EJEMPLO DOS COM TUPLA
persona = ('Karal', 'Gomez', 50000.0)
# OTRA FORMA
# mensaje_con_formato = 'Soy %s %s. mi sueldo es: %.2f'
# print(mensaje_con_formato%persona)
mensaje_con_formato = 'Soy %s %s. mi sueldo es: %.2f' % persona
print(mensaje_con_formato)

