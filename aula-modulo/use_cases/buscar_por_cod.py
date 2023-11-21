from repositorio import banco

def buscarPorCodigo(codigo: int) -> dict or None:
    for produto in banco:
        if produto['codigo'] == codigo:
            return produto
    return None

