# Clase:Persona
# Atributos: nombre, apellido y edad 
# Metodos: mostrarDetalle()
#
# Objetos instanceOf: persona1
# Objetos instanceOf: persona2

class Persona:
    def __init__(self, nombre, apellido, edad):  # self operador this referencia al objeto que se está ejecutando en cierto momento
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    # metodo de instancia mostrarDetalle()
    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('Juan', 'Perez', 21)
# Agrego un nuevo atributo al objeto persona1
persona1.telefono = '123456789'
persona1.mostrarDetalle()
print(persona1.telefono)

persona2 = Persona('Maria', 'Gomez', 34)
persona2.mostrarDetalle()
