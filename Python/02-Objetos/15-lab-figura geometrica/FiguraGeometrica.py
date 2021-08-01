class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    # AGREGO GETTER Y SETTER
    # GET ANCHO 
    @property
    def ancho(self):
        return self._ancho
    # SET ANCHO
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    # GET ALTO
    @property
    def alto(self):
        return self._alto
    # SET ALTO
    @alto.setter
    def alto(self, alto):
        self._alto = alto

    # AGREGO EL METODO STR 
    # para sobreescribirlo de la clase object y mandar a imprimir los valores de ancho y alto 
    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self.alto} ]'