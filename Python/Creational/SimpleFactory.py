import abc


class Door(abc.ABC):
    @abc.abstractmethod
    def get_width(self):
        pass

    @abc.abstractmethod
    def get_height(self):
        pass

    def __str__(self):
        return f'Size: {self.get_width()} x {self.get_height()}'


class WoodenDoor(Door):
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


class DoorFactory:
    @staticmethod
    def make_door(width, height):
        return WoodenDoor(width, height)


if __name__ == '__main__':
    door = DoorFactory.make_door(width=10, height=20)
    print('Width:', door.get_width())
    print('Height:', door.get_height())
    print(door)
