# tarefas.py
from celery import Celery
import time

# Cria uma instância do Celery. O primeiro parâmetro é o nome do módulo (não precisa ser o nome do arquivo).
# O broker é o RabbitMQ, e o backend é usado para armazenar os resultados das tarefas.
app = Celery('tarefas', broker='pyamqp://guest@localhost//', backend='rpc://')

# Define uma tarefa assíncrona usando o decorador @app.task
@app.task
def soma(x, y):
    time.sleep(3) # um sleep pra fazer ela demorar um pouco
    print('Aguarda 3s e soma')  # Isso será exibido no terminal do worker, não no terminal onde a tarefa foi chamada.
    return x + y

# Esse arquivo tem é a definição da task/tarefa é necessário ligar o worker pra deixar ela disponível
# celery -A tarefas worker -l INFO0