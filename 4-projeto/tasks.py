from celery import Celery
import time
app_celery = Celery('tasks', broker='amqp://guest@localhost//')

#Celery
#pra rodar tem que mandar o celery -A tasks worker -l INFO
@app_celery.task
def envio_pra_fila(data):
    #aqui eu salvo no banco
    print('opa entrou no celery')
    return str(data["results"][0]["bulkId"])
