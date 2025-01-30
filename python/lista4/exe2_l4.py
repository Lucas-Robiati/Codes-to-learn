from math import sqrt

class FormaGeometrica:
    def __init__(self, area:float = 0.0, perimetro:float = 0.0):
        self._area = area
        self._perimetro = perimetro

    @property
    def area(self):
        return self._area

    @property
    def perimetro(self):
        return self._perimetro

    def calcula_area(self):
        pass
    def calcula_perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base:float, altura:float):
        super().__init__(self)
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, base:float):
        self.__base = base

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura:float):
        self.__altura = altura

    def calcula_area(self):
        self._area = (self.base * self.altura)

    def calcula_perimetro(self):
        self._perimetro = ((self.base*2)+(self.altura*2))


class Triangulo(FormaGeometrica):
    def __init__(self, lado1:float, lado2:float, lado3:float):
        super().__init__(self)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcula_area(self):
        p = (self.lado1+self.lado2+self.lado3)/2
        self._area = sqrt( p*((p-self.lado1)*(p-self.lado2)*(p-self.lado3)) )

    def calcula_perimetro(self):
        self._perimetro = (self.lado1+self.lado2+self.lado3)/2

R = Retangulo(20,30)
T = Triangulo(30, 18, 27)

R.calcula_area()
R.calcula_perimetro()

print("Area retangulo: ",R.area)
print("Perimetro retangulo: ",R.perimetro,"\n")

T.calcula_area()
T.calcula_perimetro()

print("Area triangulo: ",T.area)
print("Perimetro triangulo: ",T.perimetro)
