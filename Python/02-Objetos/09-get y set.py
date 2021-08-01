# Metodos Get y Set
# Esto permite evitar el acceso directo sobre los atributos del objeto

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    
    # GETTER
    @property
    def nombre(self):
        # print('Llamando método get nombre')
        return self._nombre 
    # SETTER
    @nombre.setter
    def nombre(self, nombre):
        # print('Llamando método set nombre')
        self._nombre = nombre
    
    def mostrarDetalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
 
persona2 = Persona('Dulcinea', 'Gomez', 30)
persona2.nombre = 'Juan Carlos'
print(persona2.nombre) 

# Si bien en posible es recomendable evitar cambios directos sobre el atributo de la clase 
persona2._nombre = 'Romulo' 
persona2.mostrarDetalle()