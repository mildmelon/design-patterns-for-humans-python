class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            cls.__instances[cls].__init__(*args, **kwargs)
        return cls.__instances[cls]


class President(metaclass=Singleton):
    def __init__(self, name: str = None):
        if name is not None:
            self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name


if __name__ == '__main__':
    president1 = President(name='George Washington')
    print('President 1:', president1.name)

    president2 = President(name='John Adams')
    print('President 2:', president2.name)

    # Even without passing in a name parameter
    # We still have access to the singleton's attributes
    president3 = President()
    print('President 3:', president3.name)

    # Compare all the president instances against one another
    print('President 1 is President 2:', president1 is president2)
    print('President 1 is President 3:', president1 is president3)
    print('President 2 is President 3:', president2 is president3)

    # Attempt to set only the first president's name
    president1.name = 'George Washington'
    print('President 1:', president1.name)
    print('President 2:', president2.name)

    # Attempt to set only the second president's name
    president2.name = 'John Adams'
    print('President 1:', president1.name)
    print('President 2:', president2.name)
