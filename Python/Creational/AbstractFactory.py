import abc


class Door(abc.ABC):
    @abc.abstractmethod
    def get_description(self):
        pass


class WoodenDoor(Door):
    def get_description(self):
        print('I am a wooden door')


class IronDoor(Door):
    def get_description(self):
        print('I am an iron door')


class DoorFittingExpert(abc.ABC):
    @abc.abstractmethod
    def get_description(self):
        pass


class Welder(DoorFittingExpert):
    def get_description(self):
        print('I can only fit iron doors')


class Carpenter(DoorFittingExpert):
    def get_description(self):
        print('I can only fit wooden doors')


class DoorFactory(abc.ABC):
    @abc.abstractmethod
    def make_door(self):
        pass

    @abc.abstractmethod
    def make_fitting_expert(self):
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
    woodenFactory = WoodenDoorFactory()

    door = woodenFactory.make_door()
    expert = woodenFactory.make_fitting_expert()

    door.get_description()
    expert.get_description()

    ironFactory = IronDoorFactory()

    door = ironFactory.make_door()
    expert = ironFactory.make_fitting_expert()

    door.get_description()
    expert.get_description()
