def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Calixto', 'Maria', 'Ernesto']
#envio una lista a la función
desplegarNombres(nombres)
#envio una cadena de caracteres a la función
desplegarNombres('CALIXTO')
#envio un entero a la función pero da error por que es un objeto no iterable
#desplegarNombres(1)
#envio una tupla a la función 
desplegarNombres((1,10))
#envio una lista a la función 
desplegarNombres([1,10])