from banco_de_dados import bd
from buscar_conta import buscarConta

def deletarConta(numero: int):
    conta = buscarConta(numero)
    if conta:
        bd.remove(conta)
        print('Conta removida com sucesso!')
    else:
        print(f'Conta, {numero} não encontrada!')

if __name__ == '__main__':
    deletarConta(1)
    deletarConta(2)
    print(bd)