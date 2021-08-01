# CLASE: Object (especificado de forma implicita)
# CLASE PADRE: Persona 
# CLASE HIJA: Empleado 

# Clase Padre
# Atributos: nombre y edad
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Sobreescritura de la clase Persona
    def __str__(self):
        return f'Persona[Nombre: {self.nombre}, Edad: {self.edad}]'

# Clase Hija
# Atributos: hereda nombre y edad
# Atributo propio: sueldo
class Empleado(Persona): # heredo de Persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad) # super heredo atributos de Persona
        self.sueldo = sueldo

    def __str__(self): 
        return f'Empleado: Sueldo: {self.sueldo} | {super().__str__()}' # accedo a los atributos de clase padre