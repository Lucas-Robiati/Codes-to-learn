from robo import Robo
from random import uniform,randint

class RoboLutador(Robo):
    dano_maximo = 0.2
    def __init__(self, nome:str):
        super().__init__(nome)
        self.__poder = uniform(self.dano_maximo, 1)
    
    @property
    def poder(self):
        return self.__poder

    def atacar(self, outro):
        outro.vida *= (1 - self.__poder)
        if (isinstance(outro, RoboLutador) == True):
            self.vida *= (1 - outro.poder)
    
    def __add__(self, outro):
        string1 = self.nome
        string2 = outro.nome

        if(string1.find('-') != -1):
            string1 = string1.partition('-')[0]
        
        if(string2.find('-') != -1):
            string2 = string2.partition('-')[0]
        
        nome_f = string1 + '-' + string2
        
        return type(self)(nome_f)

    def __repr__(self):
        return f'{self.nome}: vida:{self._vida:.2f} | poder: {self.__poder:.2f}'