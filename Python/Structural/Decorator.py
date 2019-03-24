from abc import ABC, abstractmethod


class Coffee(ABC):
    @property
    @abstractmethod
    def cost(self) -> int:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    def __str__(self):
        return f'{self.description}: ${self.cost}'

    def __repr__(self):
        return self.__str__()


class SimpleCoffee(Coffee):
    @property
    def cost(self):
        return 2

    @property
    def description(self):
        return 'Simple Coffee'


class CoffeeMixin(Coffee):
    def __init__(self, coffee: Coffee, cost: int, description: str):
        self._coffee = coffee
        self._cost = cost
        self._description = description

    @property
    def cost(self):
        return self._coffee.cost + self._cost

    @property
    def description(self):
        return f'{self._coffee.description}, {self._description}'


class MilkMixin(CoffeeMixin):
    def __init__(self, coffee):
        super().__init__(coffee, cost=2, description='milk')


class WhipMixin(CoffeeMixin):
    def __init__(self, coffee):
        super().__init__(coffee, cost=5, description='whip')


class VanillaMixin(CoffeeMixin):
    def __init__(self, coffee):
        super().__init__(coffee, cost=3, description='vanilla')


if __name__ == '__main__':
    order = SimpleCoffee()
    print(order)

    order = MilkMixin(order)
    print(order)

    order = WhipMixin(order)
    print(order)

    order = VanillaMixin(order)
    print(order)
