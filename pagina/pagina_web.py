from flask import Flask

app = Flask(__name__)
import dados
endpoint = dados.Dados()


@app.route('/')
def index():
 return '''
    <title> Mini curso de API com Python Flask </title>
    <body>
    <h1> Hello, SEMAC 2023 </h1>
        <ul>
            <li><a href="/lugares"> Lugares</a></li>
            <li><a href="/livros"> Livros</a></li>
            <li><a href="/disciplinas"> Disciplinas</a></li>
        </ul>
        <br/>
        <a href='/'> Voltar </a>
    </body>
'''

@app.route('/lugares')
def lugares():
 #lista_lugares = endpoint.retorna_lugares()
 lista_lugares = endpoint.obtem_dados_api(endpoint.url_lugares)
 return f'''
    <title> Mini curso de API com Python Flask </title>
    <body>
    <h1> Lugares </h1>
        <ul>
            <li>{lista_lugares[0]}</li>
            <li>{lista_lugares[1]}</li>
            <li>{lista_lugares[2]}</li>
        </ul>
        <br/>
        <a href='/'> Voltar </a>
    </body>
'''

@app.route('/livros')
def livros():
 #lista_livros = endpoint.retorna_livros()
 lista_livros = endpoint.obtem_dados_api(endpoint.url_livros)
 return f'''
    <title> Mini curso de API com Python Flask </title>
    <body>
    <h1> Livros </h1>
        <ul>
            <li>{lista_livros[0]}</li>
            <li>{lista_livros[1]}</li>
            <li>{lista_livros[2]}</li>
        </ul>
        <br/>
        <a href='/'> Voltar </a>
    </body>
'''

@app.route('/disciplinas')
def disciplinas():
 #lista_disciplinas = endpoint.retorna_disciplinas()
 lista_disciplinas = endpoint.obtem_dados_api(endpoint.url_disciplinas)
 return f'''
    <title> Mini curso de API com Python Flask </title>
    <body>
    <h1> Disciplinas </h1>
        <ul>
            <li>{lista_disciplinas[0]}</li>
            <li>{lista_disciplinas[1]}</li>
            <li>{lista_disciplinas[2]}</li>
        </ul>
        <br/>
        <a href='/'> Voltar </a>
    </body>
'''


if __name__ == '__main__':
 app.run(debug=True)
