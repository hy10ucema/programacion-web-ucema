from Persona import Persona

print('Creación de objetos'.center(30,'-'))
persona1 = Persona('Calixto', 'Gomez', 30)
persona1.mostrar_detalle()

# Muestra que módulo manda a imprimir
#print(__name__)

print('Eliminación de objetos'.center(30,'-'))
del persona1