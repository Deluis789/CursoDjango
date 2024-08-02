# Profundizando en el tipo str

# Caracteres bytes
caracteres_en_bytes = b'Hola mundo'
print(caracteres_en_bytes)

mensaje = b'Universidad Python'
print(mensaje[0])
print(chr(mensaje[0]))

lista_caracteres = mensaje.split()
print(lista_caracteres)

# Convertir de str a bytes

string = 'Programación con Python'
print('string original', string)

bytes = string.encode('UTF-8')
print(bytes)

# Convertir de bytes a str
string2 = bytes.decode('UTF-8')
print('String decodificado', string2)

print(string == string2)