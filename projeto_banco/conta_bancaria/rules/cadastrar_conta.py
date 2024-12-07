from conta_bancaria.repositorio.conta_repositorio import contas
import random

def add_conta(nome: str) -> None:
  nova_conta = {
    "numero": random.randint(2, 10000),
    "nome": nome,
    "saldo": 0,
    "ativo": True,
    "extrato": []
  }
  contas.append(nova_conta)
