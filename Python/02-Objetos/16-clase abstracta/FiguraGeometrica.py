# CLASE ABSTRACTA
# Permite definir métodos que luego una clase hija esta obligada a implementar al momento de heredar
# En nuestro ejemplo el método a implementar es calcular_area cuyo método ya esta definido
# ABC = Abstract Base Class
# Importo la libreria para clases abstractas
from abc import ABC, abstractmethod

# Extiendo de clase abstracta ABC
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo ancho: {ancho}')
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo alto: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')

    # Defino el método abstracto para obligar a las clases hijas a implementarlo al heredarlo
    # Se define la clase pero el objeto no puede instanciar de una clase abstracta
    # con pass defino sin implementar
    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self.alto} ]'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False