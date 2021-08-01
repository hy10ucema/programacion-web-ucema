#FUNCION RECURSIVA es una función que se manda a llamar a si misma para completar una cierta tarea
#Ejemplo el factorial de un nro 5! = 5 * 4 * 3 * 2 * 1 = 120

def funcionFactorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * funcionFactorial(numero-1)

numero = 5
resultado = funcionFactorial(numero)
print(f'El factorial de {numero} es {resultado}')