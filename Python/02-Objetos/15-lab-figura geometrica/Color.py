class Color:
    def __init__(self, color):
        self._color = color

    # GET color
    @property
    def color(self):
        return self._color

    # SET color
    @color.setter
    def color(self, color):
        self._color = color

    # Sobreescrimos metodo str
    def __str__(self):
        return f'Color[color: {self._color}]'
