from conta_bancaria.repositorio.conta_repositorio import contas

def listar() -> None:
	print('--- CONTAS CADASTRADAS ---')
	for cliente in contas:
		print(f"Numero: {cliente['numero']}")
		print(f"Nome: {cliente['nome']}")
		print(f"Saldo: {cliente['saldo']}")
		print('-'*50)