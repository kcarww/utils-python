cod_atual = 0
def criarProduto(nome, categoria, preco) -> dict:
    global cod_atual
    cod_atual += 1
    produto = {
        "codigo": cod_atual,
        "nome": nome,
        "categoria": categoria,
        "preco": preco
    }
    return produto
