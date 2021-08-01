# FUNCIÓN
# Es un bloque de código que voy a poder a invocar n cantidad de veces

#1:defino mi primera función
def miFuncionEnPython():
    print('saludos desde mi función')

#2:función con parametros y argumentos 
#parametros son las variables declaremos en nuestra a función
#argumentos es el valor que enviamos a la función 
#ejemplo: nombre es el parametro y juan el argumento
def miFuncionNombre(nombre, apellido):
    print(f'nombre: {nombre}, apellido: {apellido}')

#3:funcion devuelve un resultado con ruturn
def funcionSumar(a,b):
    return (a + b)

#4:valores por default 
# -> pista del tipo de dato que regresará la función
def funcionSumarDefault(a = 0, b:int = 0) -> int:
    return (a + b)

#MAIN invoco la función desde mi programa principal
miFuncionEnPython()

miFuncionNombre('Calixto', 'Valepanada')
miFuncionNombre('Cesar', 'Juan')

resultado = funcionSumar(5,3)
print(resultado)
print(f'Resultado de la función sumar: {funcionSumar(5,4)}')

print(f'Resultado de la función sumar: {funcionSumarDefault()}')
print(f'Resultado de la función sumar: {funcionSumarDefault(1,4)}')
