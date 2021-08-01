# Encapsulamiento
# Utiliza un __ adelante del nombre del atribuo para indicar que solo son accesibles por la clase y no puede modificarse
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad
        

    def mostrar_detalle(self):
        print(f'Persona: {self.__nombre} {self.apellido} {self.edad}')
 
persona2 = Persona('Dulcinea', 'Gomez', 30)
persona2.__nombre = 'Juan'
persona2.mostrar_detalle()
