class Dados:
    def __init__(self) -> None:
        self.Disciplinas = ['Álgebra Linear', 'Cálculo 3', 'Física']
        self.Lugares = ['Chile', 'Marrocos', 'Tailândia']
        self.Livros = ['A Cabana', '1984', 'Agua para elefantes']

    def retorna_disciplinas(self):
        return self.Disciplinas

    def retorna_lugares(self):
        return self.Lugares
    
    def retorna_livros(self):
        return self.Livros


if __name__ == '__main__':
    dados = Dados()
    disciplinas = dados.retorna_disciplinas()
    print(disciplinas)

    lugares = dados.retorna_lugares()
    print(lugares)

    livros = dados.retorna_livros()
    print(livros)
