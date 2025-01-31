# Aqui é só um estudo de python

def funcao():
    print('Função funcao:')
    return "Rodando, rodando!"


def escopo():
    if True:
        if True:
            x = 10
            y = 20
    print('Função escopo:')
    print(x)  # 10
    print(y)  # 20


# if (__name__ == '__main__'):
print(funcao)
print(funcao())

escopo()

print(__name__)