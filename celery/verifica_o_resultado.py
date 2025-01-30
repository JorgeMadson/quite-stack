from celery.result import AsyncResult
from tarefas import app

resultado = AsyncResult('tarefas', app=app)
if resultado.ready():
    print(resultado.get())