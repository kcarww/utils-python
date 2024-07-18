from bit import Key

key = Key()

address = key.address
print(f'My address: {address}')


ballance = key.get_balance()
print(f'Balance: {ballance}')


import requests

# Obtendo informações de um bloco específico
block_hash = '0000000000000000000b4d0b7bda2b8657f8e982f6e7fdf2f5b71e8b1b4cfc1c'
url = f'https://blockchain.info/rawblock/{block_hash}'
response = requests.get(url)
block_data = response.json()

print(f"Altura do bloco: {block_data['height']}")
print(f"Tempo: {block_data['time']}")
print(f"Número de transações: {len(block_data['tx'])}")
