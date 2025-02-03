from celery import Celery
app_celery = Celery('tasks', broker='amqp://guest@localhost//', broker_transport_options={"queue_name_prefix": "email-webhook-"})
# app_celery = Celery('tasks', broker='amqp://guest@localhost//')

#Celery
# -A ou --app é de aplication
# pra rodar tem que mandar o celery -A tasks worker -l INFO
#
# Adicionei o flower (visualizador de celery) pra dar uma olhada
# ele sobe na porta 5555, pra rodar:
# celery -A tasks flower -l INFO
@app_celery.task
def envio_pra_fila(data):
    #aqui eu salvo no banco
    print('opa entrou no celery')
    return str(data["results"][0]["bulkId"])
