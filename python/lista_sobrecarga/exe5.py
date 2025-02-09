class Retangulo:
    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura

    @property
    def area(self):
        return self.__largura * self.__altura

    def __lt__(self, outro:'Retangulo'):
        return (self.area < outro.area)

    def __gt__(self, outro:'Retangulo'):
        return (self.area > outro.area)

    def __eq__(self, outro:'Retangulo'):
        return (self.area == outro.area)

r1 = Retangulo(3, 4)  # Área = 12
r2 = Retangulo(2, 6)  # Área = 12
r3 = Retangulo(5, 2)  # Área = 10

print(r1 == r2)  
print(r1 > r3) 
print(r3 < r2)  
