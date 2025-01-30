class Pagamento:
    def __init__(self, valor:float, data:str):
        self._valor = valor
        self._data = data

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def data(self):
        return self.__data

    @valor.setter
    def data(self, data):
        self.__data = data

    def processar_pagamento(self):
        print("Processando pagamento generico")

class PagamentoCartao(Pagamento):
    def __init__(self, numero_cartao:str, validade:str, valor:float, data:str):
        super().__init__(valor, data)
        self.__numero_cartao = numero_cartao
        self.__validade = validade

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    def processar_pagamento(self):
        print("Pagamento realizado em seu cartao no valor de ",self._valor)

class PagamentoPix(Pagamento):
    def __init__(self, chave:str, valor:float, data:str):
        super().__init__(valor, data)
        self.__chave = chave

    @property
    def chave(self):
        return self.__chave

    def processar_pagamento(self):
        print("Pagamento realizado via pix no valor de ", self._valor)

p1 = PagamentoCartao("1235.1239.4568.2345", "25/12/2001", 10000000000001.50, "30/11/2001")
p2 = PagamentoPix("477165325/63", 1000, "08/03/1963")

p1.processar_pagamento()
p2.processar_pagamento()
    


