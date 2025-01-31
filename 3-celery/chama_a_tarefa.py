#chama_a_tarefa.py
from tarefas import soma

# Chama a tarefa de forma assíncrona
resultado = soma.delay(4, 4)
print("Tarefa enviada. ID:", resultado.id)