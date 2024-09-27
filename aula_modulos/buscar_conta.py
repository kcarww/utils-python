from banco_de_dados import bd

def buscarConta(numero: int):
    for cliente in bd:
        if cliente['conta'] == numero:
            return cliente

    return None

if __name__ == '__main__':
    print(buscarConta(1))
    print(buscarConta(2))

