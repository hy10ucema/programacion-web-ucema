class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc
    """

    # Metodo inicializador (constructor) que define los atributos de la clase
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # Metodos que realizan las operaciones o acciones de la clase
    def sumar(self):
        return self.operandoA + self.operandoB 
    def restar(self):
        return self.operandoA - self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(5,3)
print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Dividir: {aritmetica1.dividir():.2f}')
print(f'Multiplicar: {aritmetica1.multiplicar()}')