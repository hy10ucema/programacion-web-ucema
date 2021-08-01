# En python no existe realmente constantes y todo puede cambiarse. 
# Sin embargo, se utiliza la convención de mayusculas para saber que es una constante 
 
from constantes import MI_CONSTANTE
from constantes import Matematicas as Mate

print(MI_CONSTANTE)
print(Mate.PI)
Mate.PI = 1
print(Mate.PI)

