from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name: str, salary: int):
        self._name = name
        self._salary = salary

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def salary(self) -> int:
        pass

    @salary.setter
    @abstractmethod
    def salary(self, salary: int):
        pass


class Developer(Employee):
    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary


class Designer(Employee):
    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary


class Organization:
    def __init__(self):
        self._employees = []

    def add_employee(self, employee):
        self._employees.append(employee)

    def get_net_salaries(self):
        net_salary = 0

        for employee in self._employees:
            net_salary += employee.salary

        return net_salary


if __name__ == '__main__':
    # Create two new employees
    john = Developer('John Doe', 12000)
    jane = Designer('Jane Doe', 15000)

    # Create an org and add the new employees
    organization = Organization()
    organization.add_employee(john)
    organization.add_employee(jane)

    # Display net salaries for all employees
    print('Net Salaries ' + str(organization.get_net_salaries()))

    # Give a raise to john
    john.salary = 15000

    # Display updated net salaries for all employees
    print('Net Salaries ' + str(organization.get_net_salaries()))
