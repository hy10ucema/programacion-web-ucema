# condicion = True

# while condicion:
#     print('ejecutando ciclo while')
# else:
#     print('fin del ciclo while')

# CICLO WHILE
contador = 0
while contador < 3:
    print(contador)
    contador += 1
else:
    print('fin ciclo')

# CICLO FOR
cadena = 'hola'
for letra in cadena:
    print(letra)
else:
    print('fin ciclo')

for i in range(6):
    print(f'Valor: {i}')

for i in range(6):
    if i % 2  == 0:
        print(f'Valor: {i}')


# USO DE BREAK
cadena = 'holanda'
for letra in cadena:
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break  #rompo el ciclo for
else:
    print('fin ciclo')

# USO DE CONTINUE
for i in range(6):
    if i % 2  != 0:
        continue  #ejecuta la siguiente iteración   
    print(f'Valor: {i}')