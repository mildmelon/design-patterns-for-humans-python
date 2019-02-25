class Account:
    _successor = None
    _balance = None

    def set_next(self, account):
        self._successor = account

    def pay(self, amount_to_pay):
        instance_class_name = self.__class__.__name__
        if self.can_pay(amount_to_pay):
            print('Paid $' + str(amount_to_pay) + ' using ' + instance_class_name)
        elif self._successor:
            print('Cannot pay using ' + instance_class_name + '...')
            print('\t...checking next payment method')
            self._successor.pay(amount_to_pay)
        else:
            raise ValueError('None of the accounts have enough _balance')

    def can_pay(self, amount: int):
        return self._balance >= amount


class Bank(Account):
    _balance = None

    def __init__(self, balance):
        self._balance = balance


class Paypal(Account):
    _balance = None

    def __init__(self, balance):
        self._balance = balance


class Bitcoin(Account):
    _balance = None

    def __init__(self, balance):
        self._balance = balance


if __name__ == '__main__':
    bank = Bank(100)
    paypal = Paypal(200)
    bitcoin = Bitcoin(300)

    bank.set_next(paypal)
    paypal.set_next(bitcoin)

    bank.pay(259)
