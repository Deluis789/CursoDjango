class Persona:
    contador_personas = 0

    # Otra forma de incrementar al contador de personas
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        # Persona.contador_personas += 1
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona:[{self.id_persona} {self.nombre} {self.edad}]'


persona1 = Persona('Ana', 23)
print(persona1)
persona2 = Persona('Albert', 26)
print(persona2)

print(f'Contador de Personas: {Persona.contador_personas}')
