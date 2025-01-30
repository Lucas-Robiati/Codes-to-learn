class Funcionario:
    def __init__(self, nome:str,cpf:str, salario:float, departamento:int):
        self.nome = nome
        self.__cpf = cpf
        self.__salario = salario
        self.departamento = departamento

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def cpf(self):
        return self.__cpf

    @property
    def salario(self):
        return self.__salario

    @property
    def departamento(self):
        return self.__departamento
    @departamento.setter
    def departamento(self, valor):
        self.__departamento = valor

    def bonificar(self):
        self.__salario += (self.salario*0.1)
    
    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nSalario: {self.salario}\nDepartamento: {self.departamento}\n"

class Gerente(Funcionario):
    def __init__(self, nome:str,cpf:str, salario:float, departamento:int, senha:str, numero_f:int):
        super().__init__(nome, cpf, salario, departamento)
        self.__senha = senha
        self.numero_f = numero_f

    @property
    def senha(self):
        return self.__senha

    @property
    def numero_f(self):
        return self.__numero_f

    @numero_f.setter
    def numero_f(self, numero_f):
        self.__numero_f = numero_f
    
    def bonificar(self):
        self._Funcionario__salario += (self.salario*0.15)

    def autentificar_senha(self, senha:str):
        return (True if(self.__senha == senha) else False)

F = Funcionario("Luan", "124.793.568-22", 1080, 68)
print(F)
F.bonificar()
print(F)

boss = Gerente("Lauriano", "467.908.405-23", 8500, 1, "Ltwqfz", 32)
print(boss)
boss.bonificar()
print(boss)

print(boss.autentificar_senha("Ltwqfz"))
print(boss.autentificar_senha("test"))
