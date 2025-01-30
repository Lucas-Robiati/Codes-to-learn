class Pais:
    def __init__(self,codigo:str,nome:str,populacao:str,dimencao:str, lista:list):
        self.codigo = codigo
        self.nome = nome
        self.populacao = populacao
        self.dimencao = dimencao
        self.lista = lista

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def populacao(self):
        return self.__populacao

    @populacao.setter
    def populacao(self, populacao):
        self.__populacao = populacao

    @property
    def dimencao(self):
        return self.__dimencao

    @dimencao.setter
    def dimencao(self, dimencao):
        self.__dimencao = dimencao

    @property
    def lista(self):
        return self.__lista

    @lista.setter
    def lista(self, lista):
        self.__lista = lista

    def verif(self, p:'Pais'):
        return ("Os Paises sao iguais" if (self.codigo == p.codigo) else "Os paises sao diferentes")

    def densidade_p(self):
        populacao = self.populacao.replace('.','').replace(',','.')
        dimencao = self.dimencao.replace('.','').replace(',','.')
        return (float(populacao)/float(dimencao))

    def limitrofe(self, p:'Pais'):
        for i in p.lista:
            if(i == self.nome):
                print(p.nome," e limitrofe de ",self.nome)
                return
        print(p,nome," nao e limitrofe de ",self.nome)
        return

    def list_paises_comun(self, pais:'Pais'):
        l = []
        for i in self.lista:
            for j in pais.lista:
                if(i == j):
                    l.append(j)
        return l


Brasil = Pais("3166-1", "Brasil", "193.946.886", "8.515.767,049", 
            ("Guiana Francesa", "Suriname", "Guiana", "Venezuela", "Colombia", "Peru", "Bolivia","Paraguai", "Argentina", "Uruguai"))

Brazil = Pais("3166-1", "Brasil", "193.946.886", "8.515.767,049", 
            ("Guiana Francesa", "Suriname", "Guiana", "Venezuela", "Colombia", "Peru", "Bolivia","Paraguai", "Argentina", "Uruguai"))

Chile = Pais("23455-1","Chile","20.057.261","756.626,23", ("Argentina","Bolivia","Peru"))

Paraguai = Pais("3166-2","Paraguai","6.348.917","406.752",("Brasil","Argentina","Bolivia"))

print(Brasil.verif(Brazil))
print(Brasil.densidade_p())

print(Brasil.list_paises_comun(Chile)) 

Brasil.limitrofe(Paraguai)
