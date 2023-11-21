from use_cases.adicionar import adicionarProduto
from use_cases.listar import listarProdutos
from use_cases.editar import editarProduto
from use_cases.deletar import deletarProduto
def menu():
    while True:
        print('-- Menu de produtos --')
        print('1 - Cadastrar produto')
        print('2 - Editar produto')
        print('3 - Deletar produto')
        print('4 - Listar todos os produtos')
        print('5 - Sair')
        opcao = input('Selecione a sua opção: ')
        if opcao == '1':
            nome = input('Digite o nome do produto: ')
            categoria = input('Digite a categoria do produto: ')
            preco = float(input('Digite o preço do produto: '))
            adicionarProduto(nome, categoria, preco)
        elif opcao == '2':
            codigo = int(input('Digite o código do produto: '))
            nome = input('Digite o nome do produto: ')
            categoria = input('Digite a categoria do produto: ')
            preco = float(input('Digite o preço do produto: '))
            editarProduto(codigo, nome, categoria, preco)
        elif opcao == '3':
            codigo = int(input('Digite o código do produto: '))
            deletarProduto(codigo)
        elif opcao == '4':
            listarProdutos()
        else:
            print('Você saiu do programa')

menu()