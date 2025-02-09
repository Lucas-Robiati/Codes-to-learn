from random import uniform
nivel_c = 0.60
dano = 0.20

class Robo:
    def __init__(self, nome:str):
        self._nome = nome
        self._nivel_critico = nivel_c
        self._vida =round(uniform(0,1), 2)

    @property
    def nome(self):
        return self._nome
    
    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):   
        self._vida = valor
        
        if(self._vida > 1):
            self._vida = 1
        
        if(self._vida < 0):
            self._vida = 0

    def __add__(self, outro:"Robo"):
        string1 = self.nome
        string2 = outro.nome

        if(string1.find('-') != -1):
            string1 = string.partition('-')[2]
        
        if(string2.find('-') != -1):
            string2 = string.partition('-')[2]
        
        nome_f = string1 + '-' + string2
        return Robo(nome_f) 

    def precisa_de_medico(self):
        return (True if (self.nome < self._nivel_critico) else False)
    
    def __repr__(self):
        return f'{self.nome}: {self._vida}'

#--------------Robo-Medico----------------------------
class RoboMedico(Robo):
    def __init__(self, nome:str):
            super().__init__(nome)
            self.__poder_de_cura = round(uniform(0,1), 2)

    def curar(self, outro:'Robo'):
        if((self.vida >= outro.vida) and (outro.vida != 1)):
            outro.vida = self.__poder_de_cura
        else:
            print("Não realizar o tratamento")

    def __add__(self, outro:"Robo"):
        string1 = self.nome
        string2 = outro.nome

        if(string1.find('-') != -1):
            string1 = string.partition('-')[2]
        
        if(string2.find('-') != -1):
            string2 = string.partition('-')[2]
        
        nome_f = string1 + '-' + string2
        return RoboMedico(self)(nome_f) 
    
    def __repr__(self):
        return f'{self.nome}: {self._vida} | poder_cura: {self.__poder_de_cura}'


#----------------Robo-Lutador-------------------
class RoboLutador(Robo):
    def __init__(self, nome:str):
        super().__init__(nome)
        self.__dano_maximo = dano
        self.__poder = round(uniform(dano, 1), 2)
    
    @property
    def poder(self):
        return self.__poder

    def atacar(self, outro:'Robo'):
        outro.vida *= (1 - self.__poder)
        if not isinstance(other, RoboLutador):
            self.vida *= (1 - outro.poder)
    
    def __add__(self, outro:"Robo"):
        string1 = self.nome
        string2 = outro.nome

        if(string1.find('-') != -1):
            string1 = string.partition('-')[2]

        if(string2.find('-') != -1):
            string2 = string.partition('-')[2]

        nome_f = string1 + '-' + string2
        return RoboLutador(self)(nome_f) 
    
    def __repr__(self):
        return f'{self.nome}: {self._vida} | poder: {self.__poder}'

lRobo = [Robo("Alfredo"), Robo("Arnaldo")]
lMedico = [RoboMedico("Paloma"), RoboMedico("Paula"), RoboMedico("Gabriel")]
lLutador = [RoboLutador("Cleithon"), RoboLutador("Silvestre"), RoboLutador("Rosa")]

print(lRobo)


