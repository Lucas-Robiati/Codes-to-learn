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


class Retangulo:
    def __init__(self, largura:float, altura:float, ponto:'Ponto2D' = Ponto2D()):
        self.largura = largura
        self.altura = altura
        self.ponto = ponto.clone()

    @property
    def largura(self) -> float:
        return self.__largura

    @property
    def altura(self) -> float:
        return self.__altura

    @largura.setter
    def largura(self, valor):
        if(valor <= 0):
            print("Valor negativos nao sao admitidos aplicando modulo na largura..")
            self.__largura = abs(valor)
            return
        self.__largura = valor
         
    @altura.setter
    def altura(self, valor):
        if(valor <= 0):
            print("Valor negativos nao sao admitidos aplicando modulo na altura..")
            self.__altura = abs(valor)
            return
        self.__altura = valor
     
    def mover(self, altern:'Ponto2D'):
       self.ponto = altern

    def area(self):
        return (self.altura*self.largura)

    def intersecao(self, comp) -> bool:  
        if ((self.ponto.x >= (comp.ponto.x + comp.largura)) 
            or ((self.largura + self.ponto.x) <= comp.ponto.x) 
            or (self.ponto.y >= (comp.ponto.y + comp.altura))
            or ((self.altura + self.ponto.y) <= comp.ponto.y) ):
            return False
        return True

    def __str__(self):
        return f"altura: {self.altura}\nlargura : {self.largura}\nponto x: {self.ponto.x}\nponto y: {self.ponto.y}"


p1 = Ponto2D(2.5,2.5)
p2 = Ponto2D(-2.5,-2.5)

F1 = Retangulo(2, 4,p1)
F2 = Retangulo(10,10,p2)
print(F1)
print(F2)

print("Ponto alterado")
F2.mover(p1)
print(F2,"\n")

print(F1.area())

print(F2.intersecao(F1))
