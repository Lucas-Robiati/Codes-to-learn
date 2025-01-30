class ContaBancaria:
    def __init__(self, nome:str, saldo:float):
        self._nome = nome
        self._saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def exibir_saldo(self):
        print("Saldo: ",self._saldo)

    def depositar(self, valor:float):
        self._saldo += valor

    def sacar(self, valor):
        if(self._saldo < valor):
            print("Saldo insuficiente - Nao e possivel sacar a quantia desejada")
        else:
            self._saldo -= valor

    def __str__(self):
        return f"Nome: {self._nome}\nSaldo: {self._saldo:.2f}"

class ContaCorrente(ContaBancaria):
    def __init__(self, nome:str, saldo:float, limite_cheque_especial:float):
        super().__init__(nome, saldo)
        self.__limite_cheque_especial = limite_cheque_especial

    def exibir_saldo(self): 
        print("Saldo: ",self._saldo)
        print("Cheque especial: ",self.__limite_cheque_especial)

    def sacar(self,valor):
        if((valor <= self.__limite_cheque_especial) and (self._saldo != -self.__limite_cheque_especial)):
            self._saldo -= valor
        else:
            print("Ultrapassa o limite do cheque especial - Nao e possivel sacar a quantia desejada")

class ContaPoupanca(ContaBancaria):
    def __init__(self, nome:str, saldo:float, taxa_juro:float):
        super().__init__(nome, saldo)
        self.__taxa_juro = taxa_juro

    @property
    def taxa_juro(self):
        return self.__taxa_juro

    @taxa_juro.setter
    def taxa_juro(self, valor):
        self.__taxa_juro = valor

    def aplicar_juros(self):
        self._saldo += (self._saldo*(self.__taxa_juro/100)) 

contaC = ContaCorrente("Lucas", 50000, 5000)
contaP = ContaPoupanca("Lucas", 100000, 1)

print(contaC)
print()
print(contaP)
print()

contaC.exibir_saldo()
contaP.exibir_saldo()

contaC.sacar(5000)
contaP.aplicar_juros()

print()
print(contaC)
print()
print(contaP)


