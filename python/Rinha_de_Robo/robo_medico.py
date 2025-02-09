from robo import Robo
from random import uniform,randint

class RoboMedico(Robo):
    def __init__(self, nome:str):
            super().__init__(nome)
            self.__poder_de_cura = uniform(0,1)

    def curar(self, outro):
        if((self.vida >= outro.vida) and (outro.vida != 1)):
            outro.vida += self.__poder_de_cura
            print("Robo curado, pronto para o combate")
        else:
            print("Não foi possivel realizar o tratamento")

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
        return f'{self.nome}: vida:{self._vida:.2f} | poder_cura: {self.__poder_de_cura:.2f}'