from Empleado import Empleado

# POLIMORFISMO es ejecutar multiples métodos en tiempo de ejecución dependiendo del objeto al cual está apuntando 
# metodo de la clase padre o hija
# GERENTE hereda de empleado y agrega atributo departamento
# En python puede no necesiamente debe haber relacion entre las clases para tener polimorfismo 

class Gerente(Empleado):
    
    def __init__(self, nombre, sueldo, departamento):
        # HEREDO clase padre
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    # SOBREESCRIBIMOS EL METODO STR DE LA CLASE PADRE
    def __str__(self):
        return f'Gerente [Departamento: {self.departamento}] {super().__str__()}'

    # def mostrar_detalles(self):
    #     return self.__str__()