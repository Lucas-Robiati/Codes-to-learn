from random import uniform,randint

class Robo:
    nivel_critico = 0.60
    def __init__(self, nome:str):
        self._nome = nome
        self._vida = uniform(0,1)

    @property
    def nome(self):
        return self._nome
    
    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):   
        self._vida = round(valor, 2)
        
        if(self._vida > 1):
            self._vida = 1
        
        if(self._vida < 0.001):
            self._vida = 0

    def __add__(self, outro):
        string1 = self.nome
        string2 = outro.nome

        if(string1.find('-') != -1):
            string1 = string1.partition('-')[0]
        
        if(string2.find('-') != -1):
            string2 = string2.partition('-')[0]
        
        nome_f = string1 + '-' + string2
        
        if((isinstance(self, RoboLutador)) or (isinstance(self, RoboMedico))):
            return type(self)(nome_f)
        else:
            return type(outro)(nome_f) 

    def precisa_de_medico(self):
        return (True if (self.vida  < self.nivel_critico) else False)
    
    def __repr__(self):
        return f'{self.nome}: vida:{self._vida:.2f}'


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

    def __repr__(self):
        return f'{self.nome}: vida:{self._vida:.2f} | poder_cura: {self.__poder_de_cura:.2f}'

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
    
    def __repr__(self):
        return f'{self.nome} vida:{self._vida:.2f} | poder: {self.__poder:.2f}'



lRobo = [Robo("Alfredo"), Robo("Arnaldo")]
lMedico = [RoboMedico("Paloma"), RoboMedico("Paula"), RoboMedico("Gabriel")]
lLutador = [RoboLutador("Cleithon"), RoboLutador("Silvestre"), RoboLutador("Rosa")]

print(lRobo)
print(lMedico)
print(lLutador)

print('\n')

R1 = lRobo[1] + lMedico[0]
print(R1)
print(type(R1))
print(R1.precisa_de_medico())

R2 = lLutador[1] + lMedico[2]
print(R2)
print(type(R2))

R3 = R1 + R2
print(R3)
print(type(R3))

print('\n')

print(lRobo[0])
print(lMedico[2])
lMedico[2].curar(lRobo[0])
print(lRobo[0])


while(lLutador[2].vida > 0 and lLutador[1].vida > 0):

    print("\nLutadores...")
    print(lLutador[1])
    print(lLutador[2])

    if((lLutador[1].vida <= 0.1) and (randint(0,1) == 0)):
       print(lMedico[0])
       lMedico[0].curar(lLutador[1])
    
    if((lLutador[2].vida <= 0.1) and (randint(0,1) == 0)):
       print(lMedico[2])
       lMedico[2].curar(lLutador[2])

    lLutador[2].atacar(lLutador[1])
    
    print("\nLutadores...")
    print(lLutador[1])
    print(lLutador[2])