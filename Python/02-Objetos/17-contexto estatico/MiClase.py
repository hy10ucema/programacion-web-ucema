class MiClase:

    # VARIABLE DE CLASE (se comparte entre objetos)
    variable_clase = 'Valor variable clase'

    # VARIABLE DE INSTANCIA (no se comparte entre objetos)
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia


print(MiClase.variable_clase)
miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)

# Creo una nueva variable de clase al vuelo
MiClase.variable_clase2 = 'Valor variable clase 2'

miClase2 = MiClase('Otro valor de variable instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

# Imprimo variable de clase creada al vuelo
print(miClase2.variable_clase2)