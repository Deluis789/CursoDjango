# Profundizando en el tipo str

# Dar formatp a un str
nombre = 'Juan'
edad = 28
sueldo = 2000
# ESTO ES UN PLACEHOLDER {}
mensaje_con_formato = 'Nombre: {}, Edad: {}, Sueldo: {:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)
# CON POSICIONES (INDICE)
mensaje_con_formato = 'Edad: {1}, Sueldo: {2:.2f}, Nombre: {0}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)
# PARTE 2
mensaje_con_formato = 'Nombre: {n}, Edad: {e}, Sueldo: {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
print(mensaje_con_formato)

"""Ejemplo"""

diccionario = {'nombre': 'Jorge Diaz', 'edad': 28, 'sueldo': 3000 }
mensaje = 'Nombre: {n[nombre]}, Edad: {e[edad]}, Sueldo: {s[sueldo]:.2f}'.format(n=diccionario, e=diccionario, s=diccionario)
print(mensaje)

diccionario = {'nombre': 'Jorge Diaz', 'edad': 28, 'sueldo': 3000 }
mensaje = 'Nombre: {dic[nombre]}, Edad: {dic[edad]}, Sueldo: {dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)