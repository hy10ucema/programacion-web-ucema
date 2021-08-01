#   OPERADORES ARITMÉTICOS
#   +	    Addition	                x + y	
#   -	    Subtraction	                x - y	
#   *	    Multiplication	            x * y	
#   /	    Division	                x / y	
#   %	    Modulus	                    x % y	
#   **	    Exponentiation	            x ** y	
#   //	    Floor division	            x // y  rounds the result down to the nearest whole number

#   OPERADORES DE COMPARACIÓN
#   ==	    Equal	                    x == y	
#   !=	    Not equal	                x != y	
#   >	    Greater than	            x > y	
#   <	    Less than	                x < y	
#   >=	    Greater than or equal to	x >= y	
#   <=	    Less than or equal to	    x <= y	

#   OPERADORES DE LOGICOS
#   and	    Returns True if both statements are true 
#   or	   	Returns True if one of the statements is true
#   not	    Reverse the result, returns False if the result is true

operandoA = 3
operandoB = 2 
resultado = operandoA // operandoB
print(f'nuestro resultado es {resultado}')
#print("el resultado es {} ".format(suma))

# Comparación
a = 4
b = 2

resultado = (a == b)
print(f'Resultado operador == : {resultado}')

resultado = (a != b)
print(f'Resultado operador != : {resultado}')

# Lógicos

a = True
b = True
resultado = a and b 
print(resultado)

resultado = a or b 
print(resultado)

resultado = not a 
print(resultado)