from celery import Celery
from salvar_messagem_no_banco import salva_messagem_por_status
app_celery = Celery('tasks', broker='amqp://guest@localhost//', broker_transport_options={"queue_name_prefix": "email-webhook-"})
# app_celery = Celery('tasks', broker='amqp://guest@localhost//')

# Celery
# -A ou --app é de aplication
# pra rodar tem que mandar o celery -A tasks worker -l INFO
# Flower
# Adicionei o flower (visualizador de celery) pra dar uma olhada
# ele sobe na porta 5555, pra rodar:
# celery -A tasks flower -l INFO
@app_celery.task
def envia_pra_fila(data):
    print('opa entrou no celery')
    # aqui salva no banco
    salva_messagem_por_status(data)
    return str(data["results"][0]["bulkId"])
