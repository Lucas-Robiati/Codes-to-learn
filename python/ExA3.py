class Midia:
    def __init__(self, titulo:str, autor:str, ano:int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"Midia({self.titulo}, {self.autor}, {self.ano})"

class Livro(Midia):
    def __init__(self, titulo:str, autor:str, ano:int, paginas:int, editora:str):
        super().__init__(titulo, autor, ano)
        self.paginas = paginas
        self.editora = editora

    def __str__(self):
        return f"Livro({self.titulo}, {self.autor}, {self.ano}, {self.paginas}, {self.editora})"


class Filme(Midia):
    def __init__(self, titulo:str, autor:str, ano:int, diretor:str, duracao:int):
        super().__init__(titulo, autor, ano)
        self.diretor = diretor
        self.duracao = duracao

    def __str__(self):
        return f"Filme({self.titulo}, {self.autor}, {self.ano}, {slef.diretor}, {self.duracao})"

m1 = Livro(titulo="bili", autor="boton", ano=2023, paginas=100, editora="vagalume")
print(m1)
