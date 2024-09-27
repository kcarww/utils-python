from buscar_conta import buscarConta
from criar_conta import addConta
from deletar_conta import deletarConta
from editar_conta import editarConta
from listar_conta import listar

def inputAddConta():
    nome = input('Digite o nome da conta: ')
    addConta(nome)

def inputDeletarConta():
    numero = int(input('Digite o número da conta: '))
    deletarConta(numero)

def inputEditarConta():
    numero = int(input('Digite o número da conta: '))
    nome = input('Digite o nome do cliente: ')
    editarConta(numero, nome)

def inputBuscarConta():
    numero = int(input('Digite o número da conta: '))
    print(buscarConta(numero))

opcoes = {
    '1': inputAddConta,
    '2': inputEditarConta,
    '3': inputDeletarConta,
    '4': inputBuscarConta,
    '5': listar,
    '6': exit
}

def menuPrincipal():
    while True:
        print('--- BEM VINDO ---')
        print('1 - Adicionar conta')
        print('2 - Editar Conta')
        print('3 - Apagar conta')
        print('4 - Buscar Conta')
        print('5 - Listar Contas')
        print('6 - Sair')
        opcao = input('Digite a opção: ')
        if opcao in opcoes:
            opcoes[opcao]()
        else:
            print('Opção inválida!')