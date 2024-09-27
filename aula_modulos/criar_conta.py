from banco_de_dados import bd

contaAtual = 1


def criarConta(nome: str):
    global contaAtual
    contaAtual += 1
    conta = {
        'conta': contaAtual,
        'cliente': nome,
        'saldo': 0,
        'ativo': True
    }
    return conta

def addConta(nome: str):
    conta = criarConta(nome)
    bd.append(conta)


# Testando o módulo
if __name__ == '__main__':
    addConta('Lucas')
    addConta('Luana')
    addConta('Maria')
    print(bd)