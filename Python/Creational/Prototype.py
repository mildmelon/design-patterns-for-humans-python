import copy


class Sheep:
    def __init__(self, name: str, category: str = 'Mountain Sheep'):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category


if __name__ == '__main__':
    original = Sheep('Jolly')
    print(original.name)
    print(original.category)

    cloned = copy.copy(original)
    cloned.name = 'Dolly'
    print(cloned.name)
    print(cloned.category)
    print(original.name)
