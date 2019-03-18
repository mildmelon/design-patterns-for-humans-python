import abc


class Lion(abc.ABC):
    @abc.abstractmethod
    def roar(self):
        pass


class AfricanLion(Lion):
    def roar(self):
        print('African Lion roars...')


class AsianLion(Lion):
    def roar(self):
        print('Asian Lion roars...')


class Hunter:
    @staticmethod
    def attack(lion: Lion):
        lion.roar()


class WildDog:
    @staticmethod
    def bark():
        print('Wild Dog barks...')


class WildDogAdapter(Lion):
    def __init__(self, dog: WildDog):
        self._dog = dog

    def roar(self):
        self._dog.bark()


if __name__ == '__main__':
    hunter = Hunter()

    african_lion = AfricanLion()
    hunter.attack(african_lion)

    asian_lion = AsianLion()
    hunter.attack(asian_lion)

    wildDog = WildDog()
    wildDogAdapter = WildDogAdapter(wildDog)
    hunter.attack(wildDogAdapter)
