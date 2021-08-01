# Objetos
# Clase plantilla que permite crear objetos
# Atributos y métodos
# Pass crear objeto sin contenido por el momento

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
 
persona1 = Persona('Juan', 'Perez', 21)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

# Atributos de objetos o instancias que no se comparten
# No tiene atributos de clase
persona2 = Persona('Maria', 'Gomez', 34)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)

# Modificar un atributo del objeto
persona1.nombre = 'Calixto'
print(persona1.nombre)