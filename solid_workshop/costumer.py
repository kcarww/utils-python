from dataclasses import dataclass

@dataclass(kw_only=True)
class Costumer:
    id: int
    name: str
    email: str
    phone: str


    def __post_init__(self):
        self.validate()

    def __str__(self):
        return f"{self.name} ({self.email})"
    
    def validate(self):
        if not self.name:
            raise ValueError("Name is required")
        if not self.email:
            raise ValueError("Email is required")
        if not self.phone:
            raise ValueError("Phone is required")
        return True