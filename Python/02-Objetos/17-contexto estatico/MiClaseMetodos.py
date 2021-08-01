class MiClase:

    # VARIABLE DE CLASE (se comparte entre objetos)
    variable_clase = 'Valor variable clase'

    # VARIABLE DE INSTANCIA (no se comparte entre objetos)
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    # METODO ESTATICO (son funciones propias que no necesitan objetos para operar)
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    # METODO DE CLASE (reciben información de la clase y permite acceder a las variables y metodos de clase)
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    # METODO DE INSTANCIA
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)


# Llamada metodo estático
MiClase.metodo_estatico()
# Llamada metodo de clase 
MiClase.metodo_clase()

miObjeto1 = MiClase('valor variable instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()