from conta_bancaria.rules.cadastrar_conta import add_conta, contas
from conta_bancaria.rules.buscar_conta import get_conta
from conta_bancaria.rules.listar_contas import listar
from conta_bancaria.rules.deletar_conta import delete_conta
from conta_bancaria.rules.editar_conta import edit_conta
from conta_bancaria.rules.saque import sacar

sacar(1, 1000)
sacar(1, 500)
sacar(1, 500)
sacar(-1, 500)


# teste cadastro
add_conta("Joana Marta")
print(contas)

# teste busca
print(get_conta(1))
print(get_conta(-1))

# listar
listar()

# deletar
# delete_conta(1)
# delete_conta(-1)
# print(contas)

# editar 
edit_conta(1, "Carlos Felino")
edit_conta(-1, "asasa")
print(contas)