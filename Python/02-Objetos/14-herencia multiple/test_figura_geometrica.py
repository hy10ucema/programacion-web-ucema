from Cuadrado import Cuadrado

# Invoco para su utilización la clase Cuadrado
cuadrado1 = Cuadrado(5, 'rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(f'Calculo área del cuadrado: {cuadrado1.calcular_area()}')

# MRO - Method Resolution Order
# Determina el orden de herencia de las clases
print(Cuadrado.mro())