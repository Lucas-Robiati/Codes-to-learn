from random import uniform,randint

class Robo:
    nivel_critico = 0.60
    def __init__(self, nome:str):
        self._nome = nome
        self._vida =round(uniform(0,1), 2)

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
        
        return type(outro)(nome_f) 

    def precisa_de_medico(self):
        return (True if (self.vida  < self.nivel_critico) else False)
    
    def __repr__(self):
        return f'{self.nome}: vida:{self._vida:.2f}'