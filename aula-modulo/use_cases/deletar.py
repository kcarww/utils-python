from use_cases.buscar_por_cod import buscarPorCodigo
from repositorio import banco


def deletarProduto(codigo: int) -> None:
    produto = buscarPorCodigo(codigo)
    if produto:
        banco.remove(produto)
        print('Produto deletado com sucesso!')
    else:
        print('Produto não encontrado!')
