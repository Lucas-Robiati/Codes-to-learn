class coordenada:
    def __init__(self, x:float = 0.0, y:float = 0.0):
        self.__x = x
        self.__y = y
    
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __str__(self):
        return f'({self.__x},{self.__y})'
   
    def __add__(self, outro:'coordenada'):
        soma_x = self.__x + outro.get_x()
        soma_y = self.__y + outro.get_y()
        return coordenada(soma_x, soma_y)

    def __neg__(self, outro:'coordenada'):
        soma_x = self.__x - outro.get_x()
        soma_y = self.__y - outro.get_y()
        return coordenada(soma_x, soma_y)
    
    def __mul__(self, outro:'coordenada'):
        soma_x = self.__x * outro.get_x()
        soma_y = self.__y * outro.get_y()
        return coordenada(soma_x, soma_y)

    def __rmul__(self, n:float):
        soma_x = self.__x * n
        soma_y = self.__y * n
        return coordenada(soma_x, soma_y)

P1 = coordenada(7.5, 5)
P2 = coordenada(10, 2)

print(P1)
P3 = P1 + P2
print(P3)
P4 = P1 * P2
print(P4)
P5 = 5 * P1
print(P5)

