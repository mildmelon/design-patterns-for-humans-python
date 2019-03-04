import abc


class Door(abc.ABC):
    @abc.abstractmethod
    def get_width(self) -> int:
        pass

    @abc.abstractmethod
    def get_height(self) -> int:
        pass

    def __str__(self):
        return f'{self.get_width()} x {self.get_height()}'


class WoodenDoor(Door):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height


class DoorFactory:
    @staticmethod
    def make_door(width=3, height=7) -> Door:
        return WoodenDoor(width, height)


if __name__ == '__main__':
    # The factory will produce a basic sized door by default
    basic_door = DoorFactory.make_door()
    print('basic door:', str(basic_door))
    print('width:', basic_door.get_width())
    print('height:', basic_door.get_height())

    # We need a large door, so we can define a custom width and height
    large_door = DoorFactory.make_door(width=6, height=14)
    print('large door:', str(large_door))
    print('width:', large_door.get_width())
    print('height:', large_door.get_height())
