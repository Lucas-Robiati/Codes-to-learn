from math import sqrt

class Ponto2D:
    def __init__(self, x:float = 0.0, y:float = 0.0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valor):
        self.__x = valor

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, valor):
        self.__y = valor

    def compara(self, ponto:'Ponto2D') -> bool:
        return (True if(self.x == ponto.x and self.y == ponto.y) else False)
    
    def __str__(self):
        return f"ponto x: {self.x}\nponto y: {self.y}"

    def dis_euclidiana(self, ponto:'Ponto2D'):
        return sqrt( ((ponto.x - self.x)**2) + ((ponto.y - self.y)**2) )

    def clone(self):
        return Ponto2D(self.x, self.y)


class Circulo:
    def __init__(self, raio:float, ponto:'Ponto2D' = Ponto2D()):
        self.raio = raio
        self.ponto = ponto.clone()

    @property
    def raio(self):
        return self.__raio
    
    @raio.setter
    def raio(self, raio):
        self.__raio = raio

    @property
    def ponto(self):
        return self.__ponto

    @ponto.setter
    def ponto(self, ponto):
        self.__ponto = ponto

    def inflar(self, valor):
        self.raio += valor

    def desinflar(self, valor):
        self.raio = abs(self.raio - valor)

    def area(self) -> float:
        return (3.1415*(self.raio**2))

p1 = Ponto2D(2,3)
c1 = Circulo(3,p1)
c2 = Circulo(raio=2)

c1.inflar(5)
print(c1.raio)
c1.desinflar(2)
print(c1.raio)

print(c2.ponto.x, c2.ponto.y, c2.raio)
c1.ponto.x = 4
print(c1.ponto.x, c1.ponto.y)
print(p1)
print(c1.area())
