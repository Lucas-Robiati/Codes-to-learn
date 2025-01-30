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

t1 = Ponto2D(2.2, 1.5)
t2 = Ponto2D(2.2,1.5)

print(t1.compara(t2))
t2.x = 5.6
t2.y = 2.3
print(t2.compara(t1))

print("Distancia euclidiana: ", t1.dis_euclidiana(t2))

print(t1.clone())


