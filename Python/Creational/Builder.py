class BurgerBuilder:
    size = None
    cheese = False
    pepperoni = False
    lettuce = False
    tomato = False

    def __init__(self, size):
        self.size = size

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_lettuce(self):
        self.lettuce = True
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_tomato(self):
        self.tomato = True
        return self

    def build(self):
        return Burger(self)


class Burger:
    _size = None
    _cheese = False
    _pepperoni = False
    _lettuce = False
    _tomato = False

    def __init__(self, builder: BurgerBuilder):
        self._size = builder.size
        self._cheese = builder.cheese
        self._pepperoni = builder.pepperoni
        self._lettuce = builder.lettuce
        self._tomato = builder.tomato

    def __str__(self):
        ticket_order = ('New Order: Burger',
                        f'Size: {self._size}',
                        f'Cheese: {self._cheese}',
                        f'Pepperoni: {self._pepperoni}',
                        f'Lettuce: {self._lettuce}',
                        f'Tomato: {self._tomato}')
        return '\n' + '\n  '.join(ticket_order)


if __name__ == '__main__':
    burger = BurgerBuilder(10).add_pepperoni().add_lettuce().add_tomato().build()
    print(burger)
    
    burger2 = BurgerBuilder(10).add_cheese().add_pepperoni().add_lettuce().add_tomato().build()
    print(burger2)
