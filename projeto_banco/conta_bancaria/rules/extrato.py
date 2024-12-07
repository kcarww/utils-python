from datetime import datetime
import random 
def criar_extrato(tipo: str, valor: float) -> dict:
    transacao = {
        "id": random.randint(1, 10000),
        "tipo": tipo.upper(),
        "data": datetime.now().strftime('%d/%m/%Y:%H:%M:%S'),
        "valor": valor
    }

    return transacao


