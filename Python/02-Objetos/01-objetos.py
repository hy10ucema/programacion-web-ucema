# Objetos
# Clase plantilla que permite crear objetos
# Atributos y métodos
# Pass crear objeto sin contenido por el momento

class Persona:
    #pass
    def __init__(self):
        self.nombre = 'Juan'
        self.apellido = 'Perez'
        self.edad = 28

print(type(Persona))
persona1 = Persona()
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)