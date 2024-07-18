from bit import Key

key = Key()

address = key.address
print(f'My address: {address}')


ballance = key.get_balance()
print(f'Balance: {ballance}')
