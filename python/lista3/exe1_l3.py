class Data:
    def __init__(self, ano:int, mes:int, dia:int) -> None:
        self.ano = ano
        self.mes = mes
        self.dia = dia

    @property
    def dia(self):
        return self.__dia;

    @dia.setter
    def dia(self, valor):

        if(self.mes == 2):
            if(1 > valor > 28):
                print("Dia invalido")
                selft.__dia = -1
                return
            self.__dia = valor
            return

        if(self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11):
            if(1 > valor > 30):
                print("Dia invalido")
                self.__dia = -1
                return
            self.__dia = valor
            return
        
        else:
            if(1 > valor and valor > 31):
                print("Dia invalido")
                self.__dia = -1
                return
            self.__dia = valor    
    
    @property
    def mes(self):
        return self.__mes;

    @mes.setter
    def mes(self, valor):
        if(0 < valor and valor < 13):
            self.__mes = valor
        else:
            print("Mes invalido")
            self.__mes = -1;
            return

    @property
    def ano(self):
        return self.__ano;

    @ano.setter
    def ano(self, valor):
        self.__ano = valor

    def next_date(self):
        
        if(self.dia == -1 or self.mes == -1):
            print("Data invalida: Não é possivel executar o procedimento")

        if(self.mes == 2 and self.dia == 28):
                self.mes += 1
                self.dia = 1
                return
        
        if((self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11) and self.dia == 30):
            self.mes += 1
            self.dia = 1
            return
        
        if((self.mes == 1 or self.mes == 3 
           or self.mes == 5 or self.mes == 7 
           or self.mes == 8 or self.mes == 10 
           or self.mes == 12) and self.dia == 31):
            
            if(self.mes == 12 and self.dia == 31):
                self.mes = 1
                self.ano += 1
                self.dia = 1
                return
            self.mes += 1
        
        self.dia += 1

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}";

d = Data(dia=31, mes=12, ano=2004)
print(d)
d.next_date()
print(d)
