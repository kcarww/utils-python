from dataclasses import dataclass
from abc import ABC, abstractmethod
from solid_workshop.costumer import Costumer
from solid_workshop.product import Product
from solid_workshop.metodo_pagamento import MetodoPagamento

@dataclass
class Order:
    id: int
    costumer_id: str
    product: list[Product]
    total: float = None
    meio_de_pagamento: MetodoPagamento

    def calculate_total(self):
        total_sem_taxa = sum([product.price for product in self.product])
        self.total = self.meio_de_pagamento.calcular_pagamento(total_sem_taxa)

    def __post_init__(self):
        self.validate()

    def __str__(self):
        return f"{self.costumer.name} - {self.product.name} - {self.quantity}"

    def validate(self):
        if not self.costumer:
            raise ValueError("Costumer is required")
        if not self.product:
            raise ValueError("Product is required")
        if not self.quantity:
            raise ValueError("Quantity is required")
        return True