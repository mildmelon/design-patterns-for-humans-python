class BurgerBuilder:
    size = None
    meat = False
    cheese = False
    tomato = False
    lettuce = False

    def __init__(self, size):
        self.size = size

    def add_meat(self):
        self.meat = True
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_tomato(self):
        self.tomato = True
        return self

    def add_lettuce(self):
        self.lettuce = True
        return self

    def build(self):
        return Burger(self)


class Burger:
    _size = None
    _meat = False
    _cheese = False
    _tomato = False
    _lettuce = False

    def __init__(self, builder: BurgerBuilder):
        self._size = builder.size
        self._meat = builder.meat
        self._cheese = builder.cheese
        self._tomato = builder.tomato
        self._lettuce = builder.lettuce

    def __str__(self):
        order = (f'Order: Burger',
                 f'Size: {self._size}',
                 f'Meat: {self._meat}',
                 f'Cheese: {self._cheese}',
                 f'Tomato: {self._tomato}',
                 f'Lettuce: {self._lettuce}')
        return '\n  '.join(order) + '\n'


if __name__ == '__main__':
    burger = BurgerBuilder(size=10).add_meat().add_lettuce().add_tomato().build()
    print(burger)
    
    burger2 = BurgerBuilder(size=15).add_meat().add_cheese().add_lettuce().build()
    print(burger2)
