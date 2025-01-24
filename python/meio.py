# aqui estou vendo como funcionam os módulos e importações
# operações assíncronas e talvez orientação a objetos

from inicio import funcao
# então quando importa o código de inicio é executado :O
# que loucura


# com o comando pip show aiohttp dá pra ver onde está instalada a lib
# ou seja mesmo sem tem instalado com o pip install o python acho ela no anaconda3.
import aiohttp # Async http client/server framework (asyncio)
import asyncio # essa é padrão do python

#aqui pra saber onde estão os arquivos
print(aiohttp.__file__) # /home/jorgeviana/anaconda3/lib/python3.11/site-packages/aiohttp/__init__.py
print(asyncio.__file__) # /home/jorgeviana/anaconda3/lib/python3.11/asyncio/__init__.py

async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.sampleapis.com/futurama/info') as response:
            data = await response.json()
            print(data)

asyncio.run(fetch_data())
