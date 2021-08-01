# Mejoro el metodo init agregando argumentos variables como tuplas o diccionarios *valores y **terminos
class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

# Agrego valores como '44553322', 2 ,3, 5 
# Agrego termimos diccionario m=manzana, p=pera
persona1 = Persona('Calixto', 'Perez', 28, '44553322', 2, 3, 5, m='manzana', p='pera')
persona1.mostrar_detalle()

persona2 = Persona('Dulcinea', 'Gomez', 30)
persona2.mostrar_detalle()
