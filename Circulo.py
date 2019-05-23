"""
>>> circulo = Circulo()
>>> circulo.calcularArea(2)
>>> circulo.getArea()
12.566370614359172

>>> circulo.calcularPerimetro(2)
>>> circulo.getPerimetro()
12.566370614359172
"""

import math

class Circulo:
    __radio = float(0)
    __perimetro = float(0)
    __area = float(0)

    def calcularArea(self, radio):
        if (radio < 0):
            self.__radio = 0
        else:
            self.__radio = radio
        self.__area = math.pi * (self.__radio * self.__radio)
        return self.__area

    def calcularPerimetro(self, radio):
        if (radio < 0):
            self.__radio = 0
        else:
            self.__radio = radio
        self.__perimetro = (2 * math.pi) * self.__radio
        return self.__perimetro


if __name__==  '__main__':
    import doctest
    doctest.testmod()