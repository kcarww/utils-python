from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar
from solid_workshop.order import Order

T = TypeVar("T")

class RepositoryInterface(ABC, Generic[T]):
    @abstractmethod
    def create(self, entity: T) -> None:
        pass


@dataclass
class OrderRepositoryInterface(ABC, RepositoryInterface[Order]):
    @abstractmethod
    def create(self, order):
        pass

    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def update(self, order):
        pass

    @abstractmethod
    def delete(self, id):
        pass

@dataclass
class InMemoryOrderRepository(OrderRepositoryInterface):
    orders = []

    def create(self, order):
        self.orders.append(order)

    def find_by_id(self, id):
        return next((order for order in self.orders if order.id == id), None)

    def list(self):
        return self.orders

    def update(self, order):
        self.delete(order.id)
        self.create(order)

    def delete(self, id):
        self.orders = [order for order in self.orders if order.id != id]