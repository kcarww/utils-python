from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int

    def __post_init__(self):
        self.validate()

    def __str__(self):
        return f"{self.name} - {self.price}"

    def validate(self):
        if not self.name:
            raise ValueError("Name is required")
        if not self.price:
            raise ValueError("Price is required")
        if not self.stock:
            raise ValueError("Stock is required")
        return True