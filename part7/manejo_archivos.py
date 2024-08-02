try:
    archivo = open('prueba.txt', 'w', encoding='utf8') # Lenguaje que soporta acentos
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close() # Aqui ya lo cierra el archivo ya nose puede trabajar
    print('Fin del archivo')