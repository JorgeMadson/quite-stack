# hora de aprender Flask
from flask import Flask, render_template
#Criando uma instancia de flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', nome="visitante")

if (__name__) == '__main__':
    # faz reload quando muda alguma coisa na aplicação
    app.run(debug=True)

@app.route('/post', methods=['POST'])
def post_example():
    return "Você fez uma requisição POST!"