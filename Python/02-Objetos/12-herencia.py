# CLASE: Object (especificado de forma implicita)
# CLASE PADRE: Persona 
# CLASE HIJA: Empleado 

# Clase Padre
# Atributos: nombre y edad
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Clase Hija
# Atributos: hereda nombre y edad
# Atributo propio: sueldo
class Empleado(Persona): # heredo de Persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad) # super heredo atributos de Persona
        self.sueldo = sueldo

empleado1 = Empleado('Juan', 28, 5000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)