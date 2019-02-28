import abc


class Coffee(abc.ABC):
    @abc.abstractmethod
    def get_cost(self) -> int:
        pass

    @abc.abstractmethod
    def get_description(self) -> str:
        pass

    def __str__(self):
        return f'{self.get_description()}: ${self.get_cost()}'

    def __repr__(self):
        return self.__str__()


class SimpleCoffee(Coffee):
    def get_cost(self):
        return 2

    def get_description(self):
        return 'Simple Coffee'


class CoffeeMixin(Coffee):
    @abc.abstractmethod
    def __init__(self, coffee: Coffee, cost: int, desc: str):
        self._coffee = coffee
        self._cost = cost
        self._desc = desc

    def get_cost(self):
        return self._coffee.get_cost() + self._cost

    def get_description(self):
        return f'{self._coffee.get_description()}, {self._desc}'


class MilkMixin(CoffeeMixin):
    def __init__(self, coffee):
        super().__init__(coffee, cost=2, desc='milk')


class WhipMixin(CoffeeMixin):
    def __init__(self, coffee):
        super().__init__(coffee, cost=5, desc='whip')


class VanillaMixin(CoffeeMixin):
    def __init__(self, coffee):
        super().__init__(coffee, cost=3, desc='vanilla')


if __name__ == '__main__':
    order = SimpleCoffee()
    print(order)

    order = MilkMixin(order)
    print(order)

    order = VanillaMixin(order)
    print(order)

    order = WhipMixin(order)
    print(order)
