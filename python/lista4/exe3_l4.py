class Atleta:
    def __init__(self, nome:str, idade:int, sexo:str, aposentado:bool, peso:float):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self._aposentado = aposentado
        self.peso = peso

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        if (len(sexo) > 1):
            self.__sexo = sexo[:1]
        else:
            self.__sexo = sexo

    def aposentar(self):
        self._aposentado = True

    def aquecer(self):
        print("Atleta aquecendo...")

class Corredor(Atleta):
    def __init__(self, nome:str, idade:int, sexo:str, aposentado:bool, peso:float):
        super().__init__(nome, idade, sexo,aposentado, peso)
    
    def correr(self):
        print("Atleta correndo...")


class Nadador(Atleta):
    def __init__(self, nome:str, idade:int, sexo:str, aposentado:bool, peso:float):
        super().__init__(nome, idade, sexo,aposentado, peso)
    
    def nadar(self):
        print("Atleta nadando...")

class Ciclista(Atleta):
    def __init__(self, nome:str, idade:int, sexo:str, aposentado:bool, peso:float):
        super().__init__(nome, idade, sexo,aposentado, peso)

    def pedalar(self):
        print("Atleta pedalando...")

class Triatleta(Corredor, Nadador, Ciclista):
    def __init__(self, nome:str, idade:int, sexo:str, aposentado:bool, peso:float):
        super().__init__(nome, idade, sexo, aposentado, peso)

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nSexo: {self.sexo}\nPeso: {self.peso}\nAposentado: {self._aposentado}"

T = Triatleta("Dona Lurdes", 68, "Fe", False, 76.5)
print(T,"\n")
T.aquecer()
T.correr()
T.nadar()
T.pedalar()
T.aposentar()
print("\n")
print(T)
