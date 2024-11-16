repositorio = []

numero_conta = 0

def add_conta(nome: str):
    global numero_conta
    numero_conta += 1
    conta_bancaria = {
        "numero": numero_conta,
        "nome": nome,
        "saldo": 0,
        "ativo": True
    }
    repositorio.append(conta_bancaria)
    
def listar_contas():
    print('--- CONTAS CADASTRADAS ---')
    for conta_bancaria in repositorio:
        print(f'Número: {conta_bancaria["numero"]}')
        print(f'Nome: {conta_bancaria["nome"]}')
        print(f'Saldo: {conta_bancaria["saldo"]}')
        print(f'Ativo: {conta_bancaria["ativo"]}')
        print('-'*50)
        
def buscar_conta(numero: int):
    for conta_bancaria in repositorio:
        if conta_bancaria["numero"] == numero:
            return conta_bancaria
    return None


def editar_conta(numero: int, nome: str):
    conta_bancaria = buscar_conta(numero)
    if conta_bancaria:
        conta_bancaria["nome"] = nome
        return True
    return False

def remover_conta(numero: int):
    conta_bancaria = buscar_conta(numero)
    if conta_bancaria:
        repositorio.remove(conta_bancaria)
        return True
    return False


def depositar(numero: int, valor: float):
    conta_bancaria = buscar_conta(numero)
    if conta_bancaria:
        conta_bancaria["saldo"] += valor
        return True
    return False


def sacar(numero: int, valor: float):
    conta_bancaria = buscar_conta(numero)
    if conta_bancaria:
        if conta_bancaria["saldo"] >= valor:
            conta_bancaria["saldo"] -= valor
            return True
    return False


def menu():
    print('1 - Adicionar conta')
    print('2 - Listar contas')
    print('3 - Editar conta')
    print('4 - Remover conta')
    print('5 - Depositar')
    print('6 - Sacar')
    print('0 - Sair')
    return int(input('Escolha uma opção: '))

def main():
    while True:
        opcao = menu()
        if opcao == 0:
            break
        elif opcao == 1:
            nome = input('Digite o nome do titular da conta: ')
            add_conta(nome)
        elif opcao == 2:
            listar_contas()
        elif opcao == 3:
            numero = int(input('Digite o número da conta: '))
            nome = input('Digite o novo nome do titular da conta: ')
            if editar_conta(numero, nome):
                print('Conta editada com sucesso!')
            else:
                print('Conta não encontrada!')
        elif opcao == 4:
            numero = int(input('Digite o número da conta: '))
            if remover_conta(numero):
                print('Conta removida com sucesso!')
            else:
                print('Conta não encontrada!')
        elif opcao == 5:
            numero = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor do depósito: '))
            if depositar(numero, valor):
                print('Depósito realizado com sucesso!')
            else:
                print('Conta não encontrada ou saldo insuficiente!')
        elif opcao == 6:
            numero = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor do saque: '))
            if sacar(numero, valor):
                print('Saque realizado com sucesso!')
            else:
                print('Conta não encontrada ou saldo insuficiente!')
        else:
            print('Opção inválida!')
