import requests


block_hash = '00000000000000000000c2cc7cddf5b387529a7e2d7149ace58bb202fbac06af'
url = f'https://blockchain.info/rawblock/{block_hash}'
response = requests.get(url)
block_data = response.json()


print(f"Altura do bloco: {block_data['height']}")
print(f"Tempo: {block_data['time']}")
print(f"Número de transações: {len(block_data['tx'])}")
