from flask import Flask, abort

app = Flask(__name__)

@app.route('/api/<tipo>', methods=['GET'])
def index(tipo):
    print(f"Requisição de lista do tipo: {tipo}")
    if tipo.lower() == 'livros':
       return ["Dom Casmurro", "Harry Potter e a criança amaldiçoada", "O Caibalion"]
    else:
       abort(403, f"O tipo {tipo} não é permitido neste endpoint.")

if __name__ == '__main__':
 app.run(debug=True, host='192.168.15.64', port=5001)