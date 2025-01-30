class ContaCorrente:
    def __init__(self, numero:str,titular:str,saldo:float, limite:float):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if(saldo > 0):
            self.__saldo = saldo
        else:
            self.__saldo = 0

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite:float):
        if(limite > 0):
            self.__limite = limite
        else:
            self.__limite = 0

    def depositar(self, valor:float):
        if(valor > 0):
            self.saldo += valor
        else:
            print("Nao e possivel depositar valores negativos ao saldo")

    def sacar(self, valor:float):
        if(self.limite >= valor):
            if(self.saldo >= valor):
                self.saldo -= valor
            else:
                print("Saldo insuficiente")
        else:
            print("Sem limite disponivel")

    def transferir(self, conta:'ContaCorrente', valor:float):
        if(self.limite >= valor):
            if(self.saldo >= valor):
                self.saldo -= valor
                conta.saldo += valor
            else:
                print("Saldo insuficiente")
        else:
            print("Sem limite disponivel")

    def __str__(self):
        return f"numero: {self.numero}\ntitular: {self.titular}\nsaldo: {self.saldo}\nlimite: {self.limite}\n"

C = ContaCorrente("01834-45", "Lucas",89470.50, 10000)
B = ContaCorrente("63029-93", "Arnaldo",903412.23, 50000)

test = ContaCorrente("23785-02","Amanda", -12213,-13132.23)
print(test)

print(C)
print(B)

C.sacar(20000)
B.depositar(500)

print(C)
print(B)

B.transferir(C, 50000)
print(B)

