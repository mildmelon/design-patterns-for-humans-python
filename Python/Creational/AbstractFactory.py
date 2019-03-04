import abc


class Door(abc.ABC):
    @abc.abstractmethod
    def get_description(self) -> str:
        pass


class WoodenDoor(Door):
    def get_description(self):
        return 'I am a wooden door'


class IronDoor(Door):
    def get_description(self):
        return 'I am an iron door'


class DoorFittingExpert(abc.ABC):
    @abc.abstractmethod
    def get_description(self) -> str:
        pass


class Welder(DoorFittingExpert):
    def get_description(self):
        return 'I can only fit iron doors'


class Carpenter(DoorFittingExpert):
    def get_description(self):
        return 'I can only fit wooden doors'


class DoorFactory(abc.ABC):
    @abc.abstractmethod
    def make_door(self) -> Door:
        pass

    @abc.abstractmethod
    def make_fitting_expert(self) -> DoorFittingExpert:
        pass


class WoodenDoorFactory(DoorFactory):
    def make_door(self):
        return WoodenDoor()

    def make_fitting_expert(self):
        return Carpenter()


class IronDoorFactory(DoorFactory):
    def make_door(self):
        return IronDoor()

    def make_fitting_expert(self):
        return Welder()


if __name__ == '__main__':
    # Wood
    woodenFactory = WoodenDoorFactory()

    wood_door = woodenFactory.make_door()
    wood_fitting_expert = woodenFactory.make_fitting_expert()

    print(wood_door.get_description())
    print(wood_fitting_expert.get_description())

    # Iron
    ironFactory = IronDoorFactory()

    iron_door = ironFactory.make_door()
    iron_fitting_expert = ironFactory.make_fitting_expert()

    print(iron_door.get_description())
    print(iron_fitting_expert.get_description())
