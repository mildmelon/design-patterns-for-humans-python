class Bulb:
    def turn_on(self):
        print('Bulb has been lit')

    def turn_off(self):
        print('Darkness!')


class Command:
    def execute(self):
        pass

    def undo(self):
        pass

    def redo(self):
        pass


class TurnOn(Command):
    _bulb = None

    def __init__(self, bulb):
        self._bulb = bulb

    def execute(self):
        self._bulb.turn_on()

    def undo(self):
        self._bulb.turn_off()

    def redo(self):
        self.execute()


class TurnOff(Command):
    _bulb = None

    def __init__(self, bulb: Bulb):
        self._bulb = bulb

    def execute(self):
        self._bulb.turn_off()

    def undo(self):
        self._bulb.turn_on()

    def redo(self):
        self.execute()


class RemoteControl:
    def submit(self, command: Command):
        command.execute()


if __name__ == '__main__':
    bulb = Bulb()

    turnOn = TurnOn(bulb)
    turnOff = TurnOff(bulb)

    remote = RemoteControl()
    remote.submit(turnOn)  # Bulb has been lit!
    remote.submit(turnOff)  # Darkness!
