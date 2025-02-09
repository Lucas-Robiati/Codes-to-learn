class SuperLista:
    def __init__(self):
        self.__lista = []
    
    def __gt__(self, valor):
        self.__lista.append(valor)
        return self
    
    def __str__(self):
        if not self.__lista:
            return "Lista vazia"
        else:
            return '\n'.join([f'{i} = {elem}' for i, elem in enumerate(self.__lista)])

lis = SuperLista()
print(lis) 

lis > 10
lis > 'Adoro programar'
lis > 42

print(lis) 
