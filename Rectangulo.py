import math

class Figura:
    _area = float(0)
    _perimetro = float(0)

    def calcularArea(self):
        return 0

    def calcularPerimetro(self):
        return 0

    def getArea(self):
        return self._area

    def getPerimetro(self):
        return self._perimetro

class Rectangulo(Figura):
    __base = float(0)
    __altura = float(0)

    def calcularArea(self, base, altura):
        if (base < 0 or altura < 0):
            self.__base = 0
            self.__altura = 0
        else:
            self.__base = base
            self.__altura = altura
        self._area = (self.__base * self.__altura)
        return self._area

    def calcularPerimetro(self, base, altura):
        if (base < 0 or altura < 0):
            self.__base = 0
            self.__altura = 0
        else:
            self.__base = base
            self.__altura = altura
        self._perimetro = (self.__base * 2) + (self.__altura * 2)
        return self._perimetro