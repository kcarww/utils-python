from banco_de_dados import bd

def listar():
    print('---- CONTAS CADASTRADAS ----')
    for cliente in bd:
        print(f"Número: {cliente['conta']}")
        print(f"Nome: {cliente['cliente']}")
        print(f"Saldo: R${cliente['saldo']}")
        print(f"Ativo: {cliente['ativo']}")
        print('-'*30)

if __name__ == '__main__':
    from criar_conta import addConta
    addConta('Luiz')
    addConta('Maria')
    listar()
