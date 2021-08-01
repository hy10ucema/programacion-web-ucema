# LISTAS 
# Conjuntos de elemetos

nombres = ['calixto', 'carla', 'ricardo', 'maria']
# índice      0       1         2         3

print(nombres)

print(nombres[0])
print(nombres[1])
print(nombres[-1])
print(nombres[-2])

#Imprimir un rango
print(nombres[0:2])
#Desde el inicio hasta el índice indicado
print(nombres[ :3])
#Desde el índice indicado hasta el final 
print(nombres[1:])

#Cambiar un valor de la lista
nombres[3] = 'ruperto'
print(nombres)

for nombre in nombres:
    print(nombre)
else:
    print('no existen mas nombres en la lista')

#cantidad de elementos de una lista
print(len(nombres))
#agregar un elemento al final de la lista
nombres.append('lorenzo')
print(nombres)
#insertar un elemento en un índice en especifico
nombres.insert(1 ,'valepanada')
print(nombres)
#quitar elemento de la lista
nombres.remove('valepanada')
print(nombres)
#quitar último elemento de la lista
nombres.pop()
print(nombres)
#quitar un elemento especificando un índice
del nombres[0]
print(nombres)
#quitar todos los elementos de la lista
nombres.clear()
print(nombres)
#eliminar la lista 
del nombres
#print(nombres)


# TUPLAS
# Lista inmutable

frutas = ('naranja', 'banana', 'durazno')
#largo de la tupla
print(len(frutas))
#acceder a un elemento
print(frutas[0])
#tupla de un solo elemento debe llevar una ,
fruta = ('naranja',)

for fruta in frutas:
    print(fruta)

#convierto una tupla en lista para poder modificar valores
print(frutas)
frutaLista = list(frutas)
frutaLista[0] = 'pera'
frutas = tuple(frutaLista)
print(frutas)

#eliminar tupla frutas
del frutas


# SET
# Lista de elementos no ordenados (sin índice), no permite elementos duplicados, no se pueden modificar los elementos pero si agregar o quitar elementos

planetas = {'marte', 'jupiter', 'saturno'}
print(planetas)  
#tamaño del set
print(len(planetas))
#saber si existe un elemento en el set 
print('marte' in planetas)
#agregar un elemento
planetas.add('tierra')
print(planetas)
#no soporta elementos duplicados
planetas.add('tierra')
planetas.add('Tierra')
print(planetas)
#eliminar elemento
planetas.remove('Tierra')
print(planetas)
#eliminar elemento sin mostrar error de no existir elemento
planetas.discard('tierrita')
print(planetas)
#limpiar elementos del set
planetas.clear()
print(planetas)
#eliminar set
del planetas

# DICCIONARIOS
# CLAVE - VALOR | key - value

diccionario = {
    'IDE' : 'Integrated Development Environment',
    'OOP' : 'Object oriented programming',
    'DBMS': 'Database management system'
}
print(diccionario)
#largo
print(len(diccionario))
#acceder a un elemento
print(diccionario['IDE'])
#otra forma de acceder a un elemento
print(diccionario.get('OOP'))
#modificar elementos
diccionario['IDE'] = 'ambiente de desarrollo integrado'
print(diccionario)
#recorrer los elementos
for termino, valor in diccionario.items():
    print(termino, valor)
#recorrer solo las claves
for termino in diccionario.keys():
    print(termino)
#recorrer solo las valores
for valor in diccionario.values():
    print(valor)
#comprobar existencia de algún elemento
print('IDE' in diccionario)
#agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)
#remover un elemento
diccionario.pop('PK')
print(diccionario)
#limpiar
diccionario.clear()
print(diccionario)
#eliminar el diccionario
del diccionario


