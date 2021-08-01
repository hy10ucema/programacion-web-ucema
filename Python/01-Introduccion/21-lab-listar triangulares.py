# FUNCION RECURSIVA PARA LISTAR NROS TRIANGULARES
# Tn= n(n+1)/2
# T1=1
# T2=3
# T3=6
# T4=10
# T5=15
# T5=21

# 1
# 1+2=3
# 1+2+3=6
# 1+2+3+4=10
# 1+2+3+4+5=15
# 1+2+3+4+5+6=21

def numerosTriangulares(n):  
  if(n > 0):
    result = n + numerosTriangulares(n - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nNúmeros triangulares")
numerosTriangulares(73)
