# hora de aprender Flask
from flask import Flask
from pages import home_view
#Criando uma instancia de flask
app = Flask(__name__)

@app.route('/')
def home():
    return home_view

if (__name__) == '__main__':
    # faz reload quando muda alguma coisa na aplicação
    app.run(debug=True)