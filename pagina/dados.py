import requests

class Dados:
    def __init__(self) -> None:
        self.Disciplinas = ['Álgebra Linear', 'Cálculo 3', 'Física']
        self.Lugares = ['Chile', 'Marrocos', 'Tailândia']
        self.Livros = ['A Cabana', '1984', 'Agua para elefantes']
        
        self.url_disciplinas = 'http://localhost:5001/api/disciplinas'
        self.url_lugares = 'http://localhost:5001/api/lugares'
        self.url_livros = 'http://localhost:5001/api/livros'
        

    # NÃO UTILIZA API        
    def retorna_disciplinas(self):
        return self.Disciplinas

    def retorna_lugares(self):
        return self.Lugares
    
    def retorna_livros(self):
        return self.Livros
    

    # UTILIZA API
    def obtem_dados_api(self, url):
        try:
            resposta = requests.get(url)
            if resposta.status_code == 200:
                return resposta.json()
        except Exception as e:
            print(f"Ocorreu um erro ao tentar se conectar á API URL {url}")
            print(f"Erro {e}")
        return ['', '', '']
 

if __name__ == '__main__':
    dados = Dados()
    livros_api = dados.obtem_dados_api(dados.url_livros)
    print(livros_api)

    lugares_api = dados.obtem_dados_api(dados.url_lugares)
    print(lugares_api)

    disciplinas_api = dados.obtem_dados_api(dados.url_disciplinas)
    print(disciplinas_api)

    #disciplinas = dados.retorna_disciplinas()
    #print(disciplinas)

    #lugares = dados.retorna_lugares()
    #print(lugares)

    #livros = dados.retorna_livros()
    #print(livros)