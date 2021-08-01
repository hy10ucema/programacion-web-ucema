from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super().__init__(lado)
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    # Metodo str que llama a las clases padres
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
