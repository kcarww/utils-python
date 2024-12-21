from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class MetodoPagamento(ABC):
    name: str

    def calcular_pagamento(self, total: float) -> float:
        pass


@dataclass
class CartaoCredito(MetodoPagamento):
    def calcular_pagamento(self, total: float) -> float:
        return total * 1.1
    

@dataclass
class Boleto(MetodoPagamento):
    def calcular_pagamento(self, total: float) -> float:
        return total * 0.9
    

@dataclass
class Pix(MetodoPagamento):
    def calcular_pagamento(self, total: float) -> float:
        return total * 0.95