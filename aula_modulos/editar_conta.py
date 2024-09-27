from buscar_conta import buscarConta
from banco_de_dados import bd

def editarConta(numero: int, nome: str):
    contaBancaria = buscarConta(numero)
    if contaBancaria:
        contaBancaria['cliente'] = nome
        print('Dados alterados com sucesso!')
    else:
        print('Cliente não encontrado!!')

if __name__ == '__main__':
    editarConta(1, 'Jonas Lopes')
    editarConta(2, 'Maria')
    print(bd)
