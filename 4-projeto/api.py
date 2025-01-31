from flask import Flask, request
from celery import Celery

app_celery = Celery('tasks', broker='amqp://guest@localhost//', backend='rpc://')


#pra rodar tem que mandar o celery -A api worker -l INFO
@app_celery.task
def envio_pra_fila(data):
    print('opa entrou no celery')
    return str(data)

print('Iniciando o servidor')
app = Flask(__name__)


#aqui vou fazer o projeto com tudo funcionando
@app.route("/email", methods=['POST'])
def receber_requisicao():
    json_do_post = request.get_json()
    envio_pra_fila.delay(json_do_post)
    return json_do_post

if __name__ == '__main__':
    app.run(debug=True)