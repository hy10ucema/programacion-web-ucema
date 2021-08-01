#función que recibe una cantidad de desconocida de elementos se usa *
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

#función que recibe argumentos variables como un diccionario de datos
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarNombres('Juan', 'Maria', 'Ernesto')
listarNombres('Laura', 'Carlos')

listarTerminos(IDE='Integrated development environment', PK='Primary key')
listarTerminos(DBMS='Database management system')
