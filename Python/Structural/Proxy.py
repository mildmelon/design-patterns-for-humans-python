class Door:
    def open(self):
        pass

    def close(self):
        pass

class LabDoor(Door):
    def open(self):
        print('Opening lab door')

    def close(self):
        print('Closing the lab door')


class SecuredDoor():
    _door = None
    __real_password = '$ecr@t'

    def __init__(self, door):
        self.door = door

    def open(self, password):
        if self.authenticate(password):
            self.door.open()
        else:
            print('Big no! It ain\'t possible.')

    def authenticate(self, password):
        return password == self.__real_password

    def close(self):
        self.door.close()


if __name__ == '__main__':
    door = SecuredDoor(LabDoor())
    door.open('invalid')

    door.open('$ecr@t')
    door.close()
