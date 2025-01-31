from flask import Flask, request

from tasks import envio_pra_fila

print('Iniciando o servidor')
app = Flask(__name__)

#Flask
#aqui vou fazer o projeto com tudo funcionando
@app.route("/email", methods=['POST'])
def receber_requisicao():
    json_do_post = request.get_json()
    while range(0, 1_000_000):
        resposta = envio_pra_fila.delay(json_do_post)
    return resposta.id

if __name__ == '__main__':
    app.run(debug=True)