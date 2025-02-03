from flask import Flask, request

from tasks import envio_pra_fila

print('Iniciando o servidor')
app = Flask(__name__)

#Flask
@app.route("/")
def health():
    return("API de pé, tudo certinho 👌")

@app.route("/email", methods=['POST'])
def receber_requisicao():
    json_do_post = request.get_json()
    resposta = envio_pra_fila.delay(json_do_post)
    return resposta.id

if __name__ == '__main__':
    app.run(debug=True)