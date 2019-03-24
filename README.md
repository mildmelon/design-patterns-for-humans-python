![Design Patterns For Humans](https://cloud.githubusercontent.com/assets/11269635/23065273/1b7e5938-f515-11e6-8dd3-d0d58de6bb9a.png)

***

<p align="center">
🎉 Ultra-simplified explanation to design patterns! 🎉
<br>
...demonstrated with PEP8 compliant python.
</p>
<p align="center">
A topic that can easily make anyone's mind wobble. Here I try to make them stick in to our minds by explaining them in the <i>simplest</i> way possible, while showing best practices.
</p>

<b>This version has been updated with the assumption that the reader has a strong understanding of python, all examples use python 3.5+</b>

***


Introduction 🚀
=================

Design patterns are solutions to recurring problems; **guidelines on how to tackle certain problems**. They are not classes, packages or libraries that you can plug into your application and wait for the magic to happen. These are, rather, guidelines on how to tackle certain problems in certain situations.
> Design patterns are solutions to recurring problems; guidelines on how to tackle certain problems

Wikipedia describes them as
> In software engineering, a software design pattern is a general reusable solution to a commonly occurring problem within a given context in software design. It is not a finished design that can be transformed directly into source or machine code. It is a description or template for how to solve a problem that can be used in many different situations.


Be Careful ⚠
-----------------

- Design patterns are not a silver bullet to all your problems.
- Do not try to force them; bad things are supposed to happen, if done so. Keep in mind that design patterns are solutions **to** problems, not solutions **finding** problems; so don't overthink.
- If used in a correct place in a correct manner, they can prove to be a savior; or else they can result in a horrible mess of a code.


Types of Design Patterns
-----------------

* [Creational](#creational-design-patterns)
* [Structural](#structural-design-patterns)
* [Behavioral](#behavioral-design-patterns)


Creational Design Patterns
==========================

In plain words
> Creational patterns are focused towards how to instantiate an object or group of related objects.

Wikipedia says
> In software engineering, creational design patterns are design patterns that deal with object creation mechanisms, trying to create objects in a manner suitable to the situation. The basic form of object creation could result in design problems or added complexity to the design. Creational design patterns solve this problem by somehow controlling this object creation.

 * [Simple Factory](#simple-factory-)
 * [Factory Method](#factory-method-)
 * [Abstract Factory](#abstract-factory-)
 * [Builder](#builder-)
 * [Prototype](#prototype-)
 * [Singleton](#singleton-)


Simple Factory 🏠
--------------

In plain words
> Simple factory simply generates an instance for client without exposing any instantiation logic to the client

Real world example
> Consider, you are building a house and you need doors. It would be a mess if every time you need a door, you put on your carpenter clothes and start making a door in your house. Instead you get it made from a factory.

Wikipedia says
> In object-oriented programming (OOP), a factory is an object for creating other objects – formally a factory is a function or method that returns objects of a varying prototype or class from some method call, which is assumed to be "new".

**Programmatic Example**

First off, we create an interface `Door` and it's implementation `WoodenDoor`
```python
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
```

Then we have our door factory that makes a door instance (with default size) and returns it
```python
class DoorFactory:
    @staticmethod
    def make_door(width=3, height=7) -> Door:
        return WoodenDoor(width, height)
```

And then it can be used like
```python
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
```
```bash
basic door: 3 x 7
width: 3
height: 7
large door: 6 x 14
width: 6
height: 14
```

**When to Use?**

When creating an object is not just a few assignments and involves some logic, it makes sense to put it in a dedicated factory instead of repeating the same code everywhere.


Factory Method 🏭
--------------

In plain words
> It provides a way to delegate the instantiation logic to child classes.

Real world example
> Consider the case of a hiring manager. It is impossible for one person to interview for each of the positions. Based on the job opening, she has to decide and delegate the interview steps to different people.

Wikipedia says
> In class-based programming, the factory method pattern is a creational pattern that uses factory methods to deal with the problem of creating objects without having to specify the exact class of the object that will be created. This is done by creating objects by calling a factory method—either specified in an interface and implemented by child classes, or implemented in a base class and optionally overridden by derived classes—rather than by calling a constructor.

 **Programmatic Example**

Taking our hiring manager example above. First of all we have an interviewer interface and some implementations for it
```python
import abc


class Interviewer(abc.ABC):
    @abc.abstractmethod
    def ask_questions(self):
        pass


class Developer(Interviewer):
    def ask_questions(self):
        print('Developer: asking about design patterns')


class CommunityExecutive(Interviewer):
    def ask_questions(self):
        print('Community Executive: asking about community building')
```

Now let us create our `HiringManager`
```python
class HiringManager(abc.ABC):
    @abc.abstractmethod
    def make_interviewer(self) -> Interviewer:
        pass

    def take_interview(self):
        interviewer = self.make_interviewer()
        interviewer.ask_questions()
```

Now any child can extend it and provide the required interviewer
```python
class DevelopmentManager(HiringManager):
    def make_interviewer(self):
        return Developer()


class MarketingManager(HiringManager):
    def make_interviewer(self):
        return CommunityExecutive()
```

and then it can be used as
```python
if __name__ == '__main__':
    devManager = DevelopmentManager()
    devManager.take_interview()

    marketingManager = MarketingManager()
    marketingManager.take_interview()
```
```bash
Developer: asking about design patterns
Community Executive: asking about community building
```

**When to use?**

Useful when there is some generic processing in a class but the required sub-class is dynamically decided at runtime. Or putting it in other words, when the client doesn't know what exact sub-class it might need.


Abstract Factory 🔨
----------------

In plain words
> A factory of factories; a factory that groups the individual but related/dependent factories together without specifying their concrete classes.

Real world example
> Extending our door example from Simple Factory. Based on your needs you might get a wooden door from a wooden door shop, iron door from an iron shop or a PVC door from the relevant shop. Plus you might need a guy with different kind of specialities to fit the door, for example a carpenter for wooden door, welder for iron door etc. As you can see there is a dependency between the doors now, wooden door needs carpenter, iron door needs a welder etc.

Wikipedia says
> The abstract factory pattern provides a way to encapsulate a group of individual factories that have a common theme without specifying their concrete classes

**Programmatic Example**

Translating the door example above. First of all we have our `Door` interface and some implementation for it
```python
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
```

Then we have some fitting experts for each door type
```python
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
```

Now we have our abstract factory that would let us make family of related objects i.e. wooden door factory would create a wooden door and wooden door fitting expert and iron door factory would create an iron door and iron door fitting expert
```python
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
```

And then it can be used as
```python
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
```
```bash
I am a wooden door
I can only fit wooden doors
I am an iron door
I can only fit iron doors
```

As you can see the wooden door factory has encapsulated the `carpenter` and the `wooden door` also iron door factory has encapsulated the `iron door` and `welder`. And thus it had helped us make sure that for each of the created door, we do not get a wrong fitting expert.   

**When to use?**

When there are interrelated dependencies with not-that-simple creation logic involved


Builder 👷
-------

In plain words
> Allows you to create different flavors of an object while avoiding constructor pollution. Useful when there could be several flavors of an object. Or when there are a lot of steps involved in creation of an object.

Real world example
> Imagine you are at Hardee's and you order a specific deal, lets say, "Big Hardee" and they hand it over to you without *any questions*; this is the example of simple factory. But there are cases when the creation logic might involve more steps. For example you want a customized Subway deal, you have several options in how your burger is made e.g what bread do you want? what types of sauces would you like? What cheese would you want? etc. In such cases builder pattern comes to the rescue.

Wikipedia says
> The builder pattern is an object creation software design pattern with the intentions of finding a solution to the telescoping constructor anti-pattern.

Having said that let me add a bit about what telescoping constructor anti-pattern is. At one point or the other we have all seen a constructor like below:
```python
def __init__(self, size, cheese=True, pepperoni=True, tomato=False, lettuce=True):
    pass
```

As you can see; the number of constructor parameters can quickly get out of hand and it might become difficult to understand the arrangement of parameters. Plus this parameter list could keep on growing if you would want to add more options in future. This is called telescoping constructor anti-pattern.

**Programmatic Example**

The sane alternative is to use the builder pattern. First of all we have our burger that we want to make
```python
class Burger:
    _size = None
    _meat = False
    _cheese = False
    _tomato = False
    _lettuce = False

    def __init__(self, builder: BurgerBuilder):
        self._size = builder.size
        self._meat = builder.meat
        self._cheese = builder.cheese
        self._tomato = builder.tomato
        self._lettuce = builder.lettuce

    def __str__(self):
        order = (f'Order: Burger',
                 f'Size: {self._size}',
                 f'Meat: {self._meat}',
                 f'Cheese: {self._cheese}',
                 f'Tomato: {self._tomato}',
                 f'Lettuce: {self._lettuce}')
        return '\n  '.join(order) + '\n'
```

And then we have the builder
```python
class BurgerBuilder:
    size = None
    meat = False
    cheese = False
    tomato = False
    lettuce = False

    def __init__(self, size):
        self.size = size

    def add_meat(self):
        self.meat = True
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_tomato(self):
        self.tomato = True
        return self

    def add_lettuce(self):
        self.lettuce = True
        return self

    def build(self):
        return Burger(self)
```

And then it can be used as:
```python
if __name__ == '__main__':
    burger = BurgerBuilder(size=10).add_meat().add_lettuce().add_tomato().build()
    print(burger)
    
    burger2 = BurgerBuilder(size=15).add_meat().add_cheese().add_lettuce().build()
    print(burger2)
```
```bash
Order: Burger
  Size: 10
  Meat: True
  Cheese: False
  Tomato: True
  Lettuce: True

Order: Burger
  Size: 15
  Meat: True
  Cheese: True
  Tomato: False
  Lettuce: True
```

**When to use?**

When there could be several flavors of an object and to avoid the constructor telescoping. The key difference from the factory pattern is that; factory pattern is to be used when the creation is a one step process while builder pattern is to be used when the creation is a multi step process.


Prototype 🐑
---------

In plain words
> Create object based on an existing object through cloning.

Real world example
> Remember dolly? The sheep that was cloned! Lets not get into the details but the key point here is that it is all about cloning

Wikipedia says
> The prototype pattern is a creational design pattern in software development. It is used when the type of objects to create is determined by a prototypical instance, which is cloned to produce new objects.

In short, it allows you to create a copy of an existing object and modify it to your needs, instead of going through the trouble of creating an object from scratch and setting it up.

**Programmatic Example**

```python
class Sheep:
    def __init__(self, name: str, category: str = 'Mountain Sheep'):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category
```

Then it can be cloned like below
```python
import copy


if __name__ == '__main__':
    original = Sheep('Jolly')
    print(original.name)
    print(original.category)

    cloned = copy.copy(original)
    cloned.name = 'Dolly'
    print(cloned.name)
    print(cloned.category)
    print(original.name)
```
```bash
Jolly
Mountain Sheep
Dolly
Mountain Sheep
Jolly
```

NOTE: `copy.copy()` returns a *shallow copy* of the original object, and changes to data in a shallow copy may cause changes in the original. You can use the magic method `__copy__` to modify the cloning behavior of the prototype object.

**When to use?**

When an object is required that is similar to existing object or when the creation would be expensive as compared to cloning.

Singleton 💍
---------

In plain words
> Ensures that only one object of a particular class is ever created.

Real world example
> There can only be one president of a country at a time. The same president has to be brought to action, whenever duty calls. President here is singleton.

Wikipedia says
> In software engineering, the singleton pattern is a software design pattern that restricts the instantiation of a class to one object. This is useful when exactly one object is needed to coordinate actions across the system.

Singleton pattern is actually considered an anti-pattern and overuse of it should be avoided. It is not necessarily bad and could have some valid use-cases but should be used with caution because it introduces a global state in your application and change to it in one place could affect in the other areas and it could become pretty difficult to debug. The other bad thing about them is it makes your code tightly coupled plus mocking the singleton could be difficult.

**Programmatic Example**

To create a singleton, we will define a metaclass to house all the Singleton instances and override their `__call__` methods to always return only one instance of the Singleton classes.
```python
class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            cls.__instances[cls].__init__(*args, **kwargs)
        return cls.__instances[cls]
```

Now in our President class, we can implement it as a Singleton by using `metaclass=Singleton`. This allows for an easy reusable metaclass for making Singleton objects.
```python
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
```

Then in order to use
```python
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
```
```bash
President 1: George Washington
President 2: John Adams
President 3: John Adams
President 1 is President 2: True
President 1 is President 3: True
President 2 is President 3: True
President 1: George Washington
President 2: George Washington
President 1: John Adams
President 2: John Adams
```


Structural Design Patterns
==========================

In plain words
> Structural patterns are mostly concerned with object composition or in other words how the entities can use each other. Or yet another explanation would be, they help in answering "How to build a software component?"

Wikipedia says
> In software engineering, structural design patterns are design patterns that ease the design by identifying a simple way to realize relationships between entities.

* [Adapter](#adapter-)
* [Bridge](#bridge-)
* [Composite](#composite-)
* [Decorator](#decorator-)
* [Facade](#facade-)
* [Flyweight](#flyweight-)
* [Proxy](#proxy-)


Adapter 🔌
-------

In plain words
> Adapter pattern lets you wrap an otherwise incompatible object in an adapter to make it compatible with another class.

Real world example
> Consider that you have some pictures in your memory card and you need to transfer them to your computer. In order to transfer them you need some kind of adapter that is compatible with your computer ports so that you can attach memory card to your computer. In this case card reader is an adapter.
> Another example would be the famous power adapter; a three legged plug can't be connected to a two pronged outlet, it needs to use a power adapter that makes it compatible with the two pronged outlet.
> Yet another example would be a translator translating words spoken by one person to another

Wikipedia says
> In software engineering, the adapter pattern is a software design pattern that allows the interface of an existing class to be used as another interface. It is often used to make existing classes work with others without modifying their source code.

**Programmatic Example**

Consider a game where there is a hunter and he hunts lions.

First we have an interface `Lion` that all types of lions have to implement
```python
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
```

And hunter expects any implementation of `Lion` interface to hunt.
```python
class Hunter:
    @staticmethod
    def attack(lion: Lion):
        lion.roar()
```

Now let's say we have to add a `WildDog` in our game so that hunter can hunt that also. But we can't do that directly because dog has a different interface. To make it compatible for our hunter, we will have to create an adapter that is compatible
```python
class WildDog:
    @staticmethod
    def bark():
        print('Wild Dog barks...')


class WildDogAdapter(Lion):
    def __init__(self, dog: WildDog):
        self._dog = dog

    def roar(self):
        self._dog.bark()
```

And now the `WildDog` can be used in our game using `WildDogAdapter`
```python
if __name__ == '__main__':
    hunter = Hunter()

    african_lion = AfricanLion()
    hunter.attack(african_lion)

    asian_lion = AsianLion()
    hunter.attack(asian_lion)

    wildDog = WildDog()
    wildDogAdapter = WildDogAdapter(wildDog)
    hunter.attack(wildDogAdapter)
```
```bash
African Lion roars...
Asian Lion roars...
Wild Dog barks...
```


Bridge 🚡
------

In Plain Words
> Bridge pattern is about preferring composition over inheritance. Implementation details are pushed from a hierarchy to another object with a separate hierarchy.

Real world example
> Consider you have a website with different pages and you are supposed to allow the user to change the theme. What would you do? Create multiple copies of each of the pages for each of the themes or would you just create separate theme and load them based on the user's preferences? Bridge pattern allows you to do the second i.e.

![With and without the bridge pattern](https://cloud.githubusercontent.com/assets/11269635/23065293/33b7aea0-f515-11e6-983f-98823c9845ee.png)

Wikipedia says
> The bridge pattern is a design pattern used in software engineering that is meant to "decouple an abstraction from its implementation so that the two can vary independently"

**Programmatic Example**

Translating our WebPage example from above. Here we have the `Theme` hierarchy 
```python
import abc


class Theme(abc.ABC):
    @abc.abstractmethod
    def get_color(self) -> str:
        pass


class DarkTheme(Theme):
    def get_color(self):
        return 'Dark Black'


class LightTheme(Theme):
    def get_color(self):
        return 'Off White'


class AquaTheme(Theme):
    def get_color(self):
        return 'Light Blue'
```

And the `WebPage` hierarchy
```python
class WebPage:
    def __init__(self, name: str, theme: Theme):
        self._name = name
        self._theme = theme

    def get_content(self):
        return f'{self._name} page in {self._theme.get_color()}'


class AboutPage(WebPage):
    def __init__(self, theme: Theme):
        super().__init__('About', theme)


class CareersPage(WebPage):
    def __init__(self, theme: Theme):
        super().__init__('Careers', theme)
```

And their uses
```python
if __name__ == '__main__':
    # Create two lists of all theme and page classes
    themes = [DarkTheme, LightTheme, AquaTheme]
    pages = [AboutPage, CareersPage]

    # Loop through all theme classes
    for theme_class in themes:
        # Create a new instance of the theme
        theme = theme_class()

        # Loop through all pages classes
        for page_class in pages:
            # Create a new instance of the page
            page = page_class(theme)

            # Output the page content to console
            print(page.get_content())
```
```bash
About page in Dark Black
Careers page in Dark Black
About page in Off White
Careers page in Off White
About page in Light Blue
Careers page in Light Blue
```


Composite 🌿
---------

In plain words
> Composite pattern lets clients treat the individual objects in a uniform manner.

Real world example
> Every organization is composed of employees. Each of the employees has the same features i.e. has a salary, has some responsibilities, may or may not report to someone, may or may not have some subordinates etc.

Wikipedia says
> In software engineering, the composite pattern is a partitioning design pattern. The composite pattern describes that a group of objects is to be treated in the same way as a single instance of an object. The intent of a composite is to "compose" objects into tree structures to represent part-whole hierarchies. Implementing the composite pattern lets clients treat individual objects and compositions uniformly.

**Programmatic Example**

Taking our employees example from above. Here we have different employee types
```python
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
```

Then we have an organization which consists of several different types of employees
```python
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
```

And then it can be used as
```python
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
```
```bash
Net Salaries 27000
Net Salaries 30000
```


Decorator ☕
---------

In plain words
> Decorator pattern lets you dynamically change the behavior of an object at run time by wrapping them in an object of a decorator class.

Real world example
> Imagine you run a car service shop offering multiple services. Now how do you calculate the bill to be charged? You pick one service and dynamically keep adding to it the prices for the provided services till you get the final cost. Here each type of service is a decorator.

Wikipedia says
> In object-oriented programming, the decorator pattern is a design pattern that allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class. The decorator pattern is often useful for adhering to the Single Responsibility Principle, as it allows functionality to be divided between classes with unique areas of concern.

**Programmatic Example**

Lets take coffee for example. First of all we have a simple coffee implementing the coffee interface
```python
from abc import ABC, abstractmethod


class Coffee(ABC):
    @property
    @abstractmethod
    def cost(self) -> int:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    def __str__(self):
        return f'{self.description}: ${self.cost}'

    def __repr__(self):
        return self.__str__()


class SimpleCoffee(Coffee):
    @property
    def cost(self):
        return 2

    @property
    def description(self):
        return 'Simple Coffee'
```

We want to make the code extensible to allow options to modify it if required. Lets make some mixins (decorators)
```python
class CoffeeMixin(Coffee):
    def __init__(self, coffee: Coffee, cost: int, description: str):
        self._coffee = coffee
        self._cost = cost
        self._description = description

    @property
    def cost(self):
        return self._coffee.cost + self._cost

    @property
    def description(self):
        return f'{self._coffee.description}, {self._description}'


class MilkMixin(CoffeeMixin):
    def __init__(self, coffee):
        super().__init__(coffee, cost=2, description='milk')


class WhipMixin(CoffeeMixin):
    def __init__(self, coffee):
        super().__init__(coffee, cost=5, description='whip')


class VanillaMixin(CoffeeMixin):
    def __init__(self, coffee):
        super().__init__(coffee, cost=3, description='vanilla')
```

Lets make a coffee now
```python
if __name__ == '__main__':
    order = SimpleCoffee()
    print(order)

    order = MilkMixin(order)
    print(order)

    order = WhipMixin(order)
    print(order)

    order = VanillaMixin(order)
    print(order)
```
```bash
Simple Coffee: $2
Simple Coffee, milk: $4
Simple Coffee, milk, whip: $9
Simple Coffee, milk, whip, vanilla: $12
```


Facade 📦
------

In plain words
> Facade pattern provides a simplified interface to a complex subsystem.

Real world example
> How do you turn on the computer? "Hit the power button" you say! That is what you believe because you are using a simple interface that computer provides on the outside, internally it has to do a lot of stuff to make it happen. This simple interface to the complex subsystem is a facade.

Wikipedia says
> A facade is an object that provides a simplified interface to a larger body of code, such as a class library.

**Programmatic Example**

Taking our computer example from above. Here we have the computer class

```python
class Computer:
    def getElectricShock(self):
        print "Ouch!"

    def makeSound(self):
        print "Beep Beep!"

    def showLoadingScreen(self):
        print "Loading..."

    def bam(self):
        print "Ready to be used..."

    def closeEverything(self):
        print "Bup bup bup buzzz!"

    def sooth(self):
        print "Zzzzz"

    def pullCurrent(self):
        print "Haaah!"
```
Here we have the facade
```python
class ComputerFacade:
    _computer = None

    def __init__(self, computer):
        self.computer = computer

    def turnOn(self):
        self.computer.getElectricShock()
        self.computer.makeSound()
        self.computer.showLoadingScreen()
        self.computer.bam()

    def turnOff(self):
        self.computer.closeEverything()
        self.computer.pullCurrent()
        self.computer.sooth()
```
Now to use the facade
```python
computer = ComputerFacade(Computer())
computer.turnOn()
computer.turnOff()
```

Flyweight 🍃
---------

In plain words
> It is used to minimize memory usage or computational expenses by sharing as much as possible with similar objects.

Real world example
> Did you ever have fresh tea from some stall? They often make more than one cup that you demanded and save the rest for any other customer so to save the resources e.g. gas etc. Flyweight pattern is all about that i.e. sharing.

Wikipedia says
> In computer programming, flyweight is a software design pattern. A flyweight is an object that minimizes memory use by sharing as much data as possible with other similar objects; it is a way to use objects in large numbers when a simple repeated representation would use an unacceptable amount of memory.

**Programmatic example**

Translating our tea example from above. First of all we have tea types and tea maker

```python
class KarakTea:
    pass

class TeaMaker:
    _availableTea = {}

    def make(self, preference):
        if not preference in self._availableTea:
            self._availableTea[preference] = KarakTea()

        return self._availableTea[preference]
```

Then we have the `TeaShop` which takes orders and serves them

```python
class TeaShop:
    _orders = {}
    _teaMaker = None

    def __init__(self, teaMaker):
        self._teaMaker = teaMaker

    def takeOrder(self, teaType, table):
        self._orders[table] = self._teaMaker.make(teaType)

    def serve(self):
        for table, tea in self._orders.iteritems():
            print "Serving tea to table #" + str(table)
```
And it can be used as below

```python
teaMaker = TeaMaker()
shop = TeaShop(teaMaker)

shop.takeOrder('less sugar', 1)
shop.takeOrder('more milk', 2)
shop.takeOrder('without sugar', 5)

shop.serve()
# Serving tea to table# 1
# Serving tea to table# 2
# Serving tea to table# 5
```

Proxy 🎱
-----

In plain words
> Using the proxy pattern, a class represents the functionality of another class.

Real world example
> Have you ever used an access card to go through a door? There are multiple options to open that door i.e. it can be opened either using access card or by pressing a button that bypasses the security. The door's main functionality is to open but there is a proxy added on top of it to add some functionality. Let me better explain it using the code example below.

Wikipedia says
> A proxy, in its most general form, is a class functioning as an interface to something else. A proxy is a wrapper or agent object that is being called by the client to access the real serving object behind the scenes. Use of the proxy can simply be forwarding to the real object, or can provide additional logic. In the proxy extra functionality can be provided, for example caching when operations on the real object are resource intensive, or checking preconditions before operations on the real object are invoked.

**Programmatic Example**

Taking our security door example from above. Firstly we have the door interface and an implementation of door

```python
class Door:
    def open(self):
        pass

    def close(self):
        pass

class LabDoor(Door):
    def open(self):
        print "Opening lab door"

    def close(self):
        print "Closing the lab door"
```
Then we have a proxy to secure any doors that we want
```python
class SecuredDoor():
    _door = None

    def __init__(self, door):
        self.door = door

    def open(self, password):
        if self.authenticate(password):
            self.door.open()
        else:
            print "Big no! It ain't possible."

    def authenticate(self, password):
        return password == '$ecr@t'

    def close(self):
        self.door.close()
```
And here is how it can be used
```python
door = SecuredDoor(LabDoor())
door.open('invalid') # Big no! It ain't possible

door.open('$ecr@t') # Opening lab door
door.close() # Closing Lab Door
```
Yet another example would be some sort of data-mapper implementation. For example, I recently made an ODM (Object Data Mapper) for MongoDB using this pattern where I wrote a proxy around mongo classes while utilizing the magic method `__call()`. All the method calls were proxied to the original mongo class and result retrieved was returned as it is but in case of `find` or `findOne` data was mapped to the required class objects and the object was returned instead of `Cursor`.

Behavioral Design Patterns
==========================

In plain words
> It is concerned with assignment of responsibilities between the objects. What makes them different from structural patterns is they don't just specify the structure but also outline the patterns for message passing/communication between them. Or in other words, they assist in answering "How to run a behavior in software component?"

Wikipedia says
> In software engineering, behavioral design patterns are design patterns that identify common communication patterns between objects and realize these patterns. By doing so, these patterns increase flexibility in carrying out this communication.

* [Chain of Responsibility](#chain-of-responsibility-)
* [Command](#command-)
* [Iterator](#iterator-)
* [Mediator](#mediator-)
* [Memento](#memento-)
* [Observer](#observer-)
* [Visitor](#visitor-)
* [Strategy](#strategy-)
* [State](#state-)
* [Template Method](#template-method-)

Chain of Responsibility 🔗
-----------------------

In plain words
> It helps building a chain of objects. Request enters from one end and keeps going from object to object till it finds the suitable handler.

Real world example
> For example, you have three payment methods (`A`, `B` and `C`) setup in your account; each having a different amount in it. `A` has 100 USD, `B` has 300 USD and `C` having 1000 USD and the preference for payments is chosen as `A` then `B` then `C`. You try to purchase something that is worth 210 USD. Using Chain of Responsibility, first of all account `A` will be checked if it can make the purchase, if yes purchase will be made and the chain will be broken. If not, request will move forward to account `B` checking for amount if yes chain will be broken otherwise the request will keep forwarding till it finds the suitable handler. Here `A`, `B` and `C` are links of the chain and the whole phenomenon is Chain of Responsibility.

Wikipedia says
> In object-oriented design, the chain-of-responsibility pattern is a design pattern consisting of a source of command objects and a series of processing objects. Each processing object contains logic that defines the types of command objects that it can handle; the rest are passed to the next processing object in the chain.

**Programmatic Example**

Translating our account example above. First of all we have a base account having the logic for chaining the accounts together and some accounts

```python
import inspect

class Account:
    _successor = None
    _balance = None

    def setNext(self, account):
        self._successor = account

    def pay(self, amountToPay):
        import inspect
        myCaller = inspect.stack()[1][3]
        if self.canPay(amountToPay):
            print "Paid " + str(amountToPay) + " using " + myCaller
        elif (self._successor):
            print "Cannot pay using " + myCaller + ". Proceeding .."
            self._successor.pay(amountToPay)
        else:
            raise ValueError('None of the accounts have enough balance')
    def canPay(self, amount):
        return self.balance >= amount

class Bank(Account):
    _balance = None

    def __init__(self, balance):
        self.balance = balance

class Paypal(Account):
    _balance = None

    def __init__(self, balance):
        self.balance = balance

class Bitcoin(Account):
    _balance = None

    def __init__(self, balance):
        self.balance = balance
```

Now let's prepare the chain using the links defined above (i.e. Bank, Paypal, Bitcoin)

```python
# Let's prepare a chain like below
#      $bank->$paypal->$bitcoin
#
# First priority bank
#      If bank can't pay then paypal
#      If paypal can't pay then bit coin

bank = Bank(100) # Bank with balance 100
paypal = Paypal(200) # Paypal with balance 200
bitcoin = Bitcoin(300) # Bitcoin with balance 300

bank.setNext(paypal)
paypal.setNext(bitcoin)

bank.pay(259)

'''
Output will be
==============
Cannot pay using bank. Proceeding ..
Cannot pay using paypal. Proceeding ..:
Paid 259 using Bitcoin!
'''
```

Command 👮
-------

Real world example
> A generic example would be you ordering food at a restaurant. You (i.e. `Client`) ask the waiter (i.e. `Invoker`) to bring some food (i.e. `Command`) and waiter simply forwards the request to Chef (i.e. `Receiver`) who has the knowledge of what and how to cook.
> Another example would be you (i.e. `Client`) switching on (i.e. `Command`) the television (i.e. `Receiver`) using a remote control (`Invoker`).

In plain words
> Allows you to encapsulate actions in objects. The key idea behind this pattern is to provide the means to decouple client from receiver.

Wikipedia says
> In object-oriented programming, the command pattern is a behavioral design pattern in which an object is used to encapsulate all information needed to perform an action or trigger an event at a later time. This information includes the method name, the object that owns the method and values for the method parameters.

**Programmatic Example**

First of all we have the receiver that has the implementation of every action that could be performed
```python
# Receiver
class Bulb:
    def turnOn(self):
        print "Bulb has been lit"

    def turnOff(self):
        print "Darkness!"
```
then we have an interface that each of the commands are going to implement and then we have a set of commands
```python
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
        self._bulb.turnOn()

    def undo(self):
        self._bulb.turnOff()

    def redo(self):
        self.execute()

class TurnOff(Command):
    _bulb = None

    def __init__(self, bulb):
        self.bulb = bulb

    def execute(self):
        self.bulb.turnOff()

    def undo(self):
        self.bulb.turnOn()

    def redo(self):
        self.execute()
```
Then we have an `Invoker` with whom the client will interact to process any commands
```python
# Invoker
class RemoteControl:
    def submit(self, command):
        command.execute()
```
Finally let's see how we can use it in our client
```python
bulb = Bulb()

turnOn = TurnOn(bulb)
turnOff = TurnOff(bulb)

remote = RemoteControl()
remote.submit(turnOn) # Bulb has been lit!
remote.submit(turnOff) # Darkness!
```

Command pattern can also be used to implement a transaction based system. Where you keep maintaining the history of commands as soon as you execute them. If the final command is successfully executed, all good otherwise just iterate through the history and keep executing the `undo` on all the executed commands.

Iterator ➿
--------

In plain words
> It presents a way to access the elements of an object without exposing the underlying presentation.

Real world example
> An old radio set will be a good example of iterator, where user could start at some channel and then use next or previous buttons to go through the respective channels. Or take an example of MP3 player or a TV set where you could press the next and previous buttons to go through the consecutive channels or in other words they all provide an interface to iterate through the respective channels, songs or radio stations.  

Wikipedia says
> In object-oriented programming, the iterator pattern is a design pattern in which an iterator is used to traverse a container and access the container's elements. The iterator pattern decouples algorithms from containers; in some cases, algorithms are necessarily container-specific and thus cannot be decoupled.

**Programmatic example**


```python
class RadioStation:
    _frequency = None

    def __init__(self, frequency):
        self._frequency = frequency

    def getFrequency(self):
        return self._frequency
```
Then we have our iterator

```python
class StationList:
    _stations = []
    _counter = 0

    def addStation(self, station):
        self._stations.append(station)

    def removeStation(self, toRemove):
        toRemoveFrequency = toRemove.getFrequency()
        self._stations = filter(lambda station: station.getFrequency() != toRemoveFrequency, self._stations)

    def __iter__(self):
        return iter(self._stations)

    def next(self):
        self._counter += 1
```
And then it can be used as
```python
    stationList = StationList()

    stationList.addStation(RadioStation(89))
    stationList.addStation(RadioStation(101))
    stationList.addStation(RadioStation(102))
    stationList.addStation(RadioStation(103.2))

    for station in stationList:
        print station.getFrequency()

    stationList.removeStation(RadioStation(89))

    for station in stationList:
        print station.getFrequency()
```

Mediator 👽
--------

In plain words
> Mediator pattern adds a third party object (called mediator) to control the interaction between two objects (called colleagues). It helps reduce the coupling between the classes communicating with each other. Because now they don't need to have the knowledge of each other's implementation.

Real world example
> A general example would be when you talk to someone on your mobile phone, there is a network provider sitting between you and them and your conversation goes through it instead of being directly sent. In this case network provider is mediator.

Wikipedia says
> In software engineering, the mediator pattern defines an object that encapsulates how a set of objects interact. This pattern is considered to be a behavioral pattern due to the way it can alter the program's running behavior.

**Programmatic Example**

Here is the simplest example of a chat room (i.e. mediator) with users (i.e. colleagues) sending messages to each other.

First of all, we have the mediator i.e. the chat room

```python
class ChatRoomMediator:
    def showMessage(self, user, message):
        pass

class ChatRoom(ChatRoomMediator):
    def showMessage(self, user, message):
        import datetime
        time = datetime.datetime.now()
        sender = user.getName()

        print str(time) + '[' + sender + ']: ' + message
```

Then we have our users i.e. colleagues
```python
class User:
    _name = None
    _chatMediator = None

    def __init__(self, name, chatMediator):
        self.name = name
        self._chatMediator = chatMediator

    def getName(self):
        return self.name

    def send(self, message):
        self._chatMediator.showMessage(self, message)
```
And the usage
```python
mediator = ChatRoom()

john = User('John Doe', mediator)
jane = User('Jane Doe', mediator)

john.send('Hi There!')
jane.send('Hey!')
# Output will be
# Feb 14, 10:58 [John]: Hi there!
# Feb 14, 10:58 [Jane]: Hey!
```

Memento 💾
-------

In plain words
> Memento pattern is about capturing and storing the current state of an object in a manner that it can be restored later on in a smooth manner.

Real world example
> Take the example of calculator (i.e. originator), where whenever you perform some calculation the last calculation is saved in memory (i.e. memento) so that you can get back to it and maybe get it restored using some action buttons (i.e. caretaker).

Wikipedia says
> The memento pattern is a software design pattern that provides the ability to restore an object to its previous state (undo via rollback).

Usually useful when you need to provide some sort of undo functionality.

**Programmatic Example**

Lets take an example of text editor which keeps saving the state from time to time and that you can restore if you want.

First of all we have our memento object that will be able to hold the editor state

```python
class EditorMemento:
    _content = None

    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content
```

Then we have our editor i.e. originator that is going to use memento object

```python
class Editor:
    _content = ''

    def type(self, words):
        self._content = self._content + ' ' + words

    def get_content(self):
       return self._content

    def save(self):
        return EditorMemento(self._content)

    def restore(self, memento):
        self.content = memento.get_content()
```

And then it can be used as

```python
editor = Editor()
editor.type('This is the first sentence')
editor.type('This is the second.')

#Save the state to restore to : This is the first sentence. This is second.
saved = editor.save()
editor.type('And this is the third')

print editor.get_content() # This is the first sentence. This is second. And this is third.

editor.restore(saved)
editor.get_content() # This is the first sentence. This is second.
```

Observer 😎
--------

In plain words
> Defines a dependency between objects so that whenever an object changes its state, all its dependents are notified.

Real world example
> A good example would be the job seekers where they subscribe to some job posting site and they are notified whenever there is a matching job opportunity.   

Wikipedia says
> The observer pattern is a software design pattern in which an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.

**Programmatic example**

Translating our example from above. First of all we have job seekers that need to be notified for a job posting
```python
class JobPost:
    _title = None

    def __init__(self, title):
        self.title = title

    def getTitle(self):
        return self.title

class JobSeeker:
    _name = None

    def __init__(self, name):
        self.name = name

    def onJobPosted(self, job):
        print 'Hi ' + self.name + '! New job posted: ' + job.getTitle()

```
Then we have our job postings to which the job seekers will subscribe
```python
class EmploymentAgency:
    _observers = []

    def notify(self, jobPosting):
        for observer in self._observers:
            observer.onJobPosted(jobPosting)

    def attach(self, observer):
        self._observers.append(observer)

    def addJob(self, jobPosting):
        self.notify(jobPosting)
```
Then it can be used as
```python
johnDoe = JobSeeker('John Doe')
janeDoe = JobSeeker('Jane Doe')

jobPostings = EmploymentAgency()
jobPostings.attach(janeDoe)
jobPostings.attach(johnDoe)

jobPostings.addJob(JobPost('Software Engineer'))
'''
Output
Hi John Doe! New job posted: Software Engineer
Hi Jane Doe! New job posted: Software Engineer
'''
```

Visitor 🏃
-------

In plain words
> Visitor pattern lets you add further operations to objects without having to modify them.

Real world example
> Consider someone visiting Dubai. They just need a way (i.e. visa) to enter Dubai. After arrival, they can come and visit any place in Dubai on their own without having to ask for permission or to do some leg work in order to visit any place here; just let them know of a place and they can visit it. Visitor pattern lets you do just that, it helps you add places to visit so that they can visit as much as they can without having to do any legwork.

Wikipedia says
> In object-oriented programming and software engineering, the visitor design pattern is a way of separating an algorithm from an object structure on which it operates. A practical result of this separation is the ability to add new operations to existing object structures without modifying those structures. It is one way to follow the open/closed principle.

**Programmatic example**

Let's take an example of a zoo simulation where we have several different kinds of animals and we have to make them Sound. Let's translate this using visitor pattern

```python
# Visitee
class Animal:
    def accept(self, operation):
        pass

# Visitor
class AnimalOperation:
    def visitMonkey(self, monkey):
        pass

    def visitLion(self, lion):
        pass

    def visitDolphin(self, dolphin):
        pass
```
Then we have our implementations for the animals
```python
class Monkey(Animal):
    def shout(self):
        print 'Ooh oo aa aa!'

    def accept(self, operation):
        operation.visitMonkey(self)

class Lion(Animal):
    def roar(self):
        print 'Roaaar!'

    def accept(self, operation):
        operation.visitLion(self)

class Dolphin(Animal):
    def speak(self):
        print 'Tuut tuttu tuutt!'

    def accept(self, operation):
        operation.visitDolphin(self)
```
Let's implement our visitor
```python
class Speak(AnimalOperation):
    def visitMonkey(self, monkey):
        monkey.shout()

    def visitLion(self, lion):
        lion.roar()

    def visitDolphin(self, dolphin):
        dolphin.speak()
```

And then it can be used as
```python
monkey = Monkey()
lion = Lion()
dolphin = Dolphin()

speak = Speak()
monkey.accept(speak) # Ooh oo aa aa!
lion.accept(speak) # Roaaar!
dolphin.accept(speak) #Tuut tutt tuttt!
```
We could have done this simply by having an inheritance hierarchy for the animals but then we would have to modify the animals whenever we would have to add new actions to animals. But now we will not have to change them. For example, let's say we are asked to add the jump behavior to the animals, we can simply add that by creating a new visitor i.e.

```python
class Jump(AnimalOperation):
    def visitMonkey(self, monkey):
        print 'Jumped 20 feet high! on to the tree!'

    def visitLion(self, lion):
        print 'Jumped 7 feet! back on the ground!'

    def visitDolphin(self, dolphin):
        print 'Walked on water a little and disappeared'
```
And for the usage
```python
jump = Jump()

monkey.accept(speak)    # Ooh oo aa aa!
monkey.accept(jump)     # Jumped 20 feet high! on to the tree!

lion.accept(speak)      # Roaaar!
lion.accept(jump)       # Jumped 7 feet! Back on the ground!

dolphin.accept(speak)   # Tuut tutt tuutt!
dolphin.accept(jump)    # Walked on water a little and disappeared
```

Strategy 💡
--------

In plain words
> Strategy pattern allows you to switch the algorithm or strategy based upon the situation.

Real world example
> Consider the example of sorting, we implemented bubble sort but the data started to grow and bubble sort started getting very slow. In order to tackle this we implemented Quick sort. But now although the quick sort algorithm was doing better for large datasets, it was very slow for smaller datasets. In order to handle this we implemented a strategy where for small datasets, bubble sort will be used and for larger, quick sort.

Wikipedia says
> In computer programming, the strategy pattern (also known as the policy pattern) is a behavioural software design pattern that enables an algorithm's behavior to be selected at runtime.

**Programmatic example**

Translating our example from above. First of all we have our strategy interface and different strategy implementations

```python
class SortStrategy:
    def sort(self, dataset):
        pass

class BubbleSortStrategy(SortStrategy):
    def sort(self, dataset):
        print 'Sorting using bubble sort'

        return dataset

class QuickSortStrategy(SortStrategy):
    def sort(self, dataset):
        print 'Sorting using quick sort'
        return dataset
```

And then we have our client that is going to use any strategy
```python
class Sorter:
    _sorter = None

    def __init__(self, sorter):
        self._sorter = sorter

    def sort(self, dataset):
        return self._sorter.sort(dataset)
```
And it can be used as
```python
dataset = [1, 5, 4, 3, 2, 8]

sorter = Sorter(BubbleSortStrategy())
sorter.sort(dataset)

sorter = Sorter(QuickSortStrategy())
sorter.sort(dataset)
```

State 💢
-----

In plain words
> It lets you change the behavior of a class when the state changes.

Real world example
> Imagine you are using some drawing application, you choose the paint brush to draw. Now the brush changes its behavior based on the selected color i.e. if you have chosen red color it will draw in red, if blue then it will be in blue etc.  

Wikipedia says
> The state pattern is a behavioral software design pattern that implements a state machine in an object-oriented way. With the state pattern, a state machine is implemented by implementing each individual state as a derived class of the state pattern interface, and implementing state transitions by invoking methods defined by the pattern's superclass.
> The state pattern can be interpreted as a strategy pattern which is able to switch the current strategy through invocations of methods defined in the pattern's interface.

**Programmatic example**

Let's take an example of text editor, it lets you change the state of text that is typed i.e. if you have selected bold, it starts writing in bold, if italic then in italics etc.

First of all we have our state interface and some state implementations

```python
class WritingState:
    def write(self, words):
        pass

class UpperCase(WritingState):
    def write(self, words):
        print words.upper()

class LowerCase(WritingState):
    def write(self, words):
        print words.lower()

class DefaultText(WritingState):
    def write(self, words):
        print words
```
Then we have our editor
```python
class TextEditor():
    _state = None

    def __init__(self, state):
        self._state = state

    def setState(self, state):
        self._state = state

    def type(self, words):
        self._state.write(words)
```
And then it can be used as
```python
editor = TextEditor(DefaultText())
editor.type('First Line')
editor.setState(UpperCase())

editor.type('Second Line')
editor.type('Third Line')

editor.setState(LowerCase())

editor.type('Fourth Line')
editor.type('Fifth Line')

# Output:
# First line
# SECOND LINE
# THIRD LINE
# fourth line
# fifth line
```

Template Method 📒
---------------

In plain words
> Template method defines the skeleton of how a certain algorithm could be performed, but defers the implementation of those steps to the children classes.

Real world example
> Suppose we are getting some house built. The steps for building might look like
> - Prepare the base of house
> - Build the walls
> - Add roof
> - Add other floors

> The order of these steps could never be changed i.e. you can't build the roof before building the walls etc but each of the steps could be modified for example walls can be made of wood or polyester or stone.

Wikipedia says
> In software engineering, the template method pattern is a behavioral design pattern that defines the program skeleton of an algorithm in an operation, deferring some steps to subclasses. It lets one redefine certain steps of an algorithm without changing the algorithm's structure.

**Programmatic Example**

Imagine we have a build tool that helps us test, lint, build, generate build reports (i.e. code coverage reports, linting report etc) and deploy our app on the test server.

First of all we have our base class that specifies the skeleton for the build algorithm
```python
class Builder:
    def build(self):
        self.test()
        self.lint()
        self.assemble()
        self.deploy()

    def test(self):
        pass

    def lint(self):
        pass

    def assemble(self):
        pass

    def deploy(self):
        pass
```

Then we can have our implementations
```python
class AndroidBuilder(Builder):
    def test(self):
        print 'Running android tests'

    def lint(self):
        print 'Linting the android code'

    def assemble(self):
        print 'Assembling the android build'

    def deploy(self):
        print 'Deploying android build to server'

class IosBuilder(Builder):
    def test(self):
        print 'Running ios tests'

    def lint(self):
        print 'Linting the ios code'

    def assemble(self):
        print 'Assembling the ios build'

    def deploy(self):
        print 'Deploying ios build to server'
```

And then it can be used as
```python
androidBuilder = AndroidBuilder()
androidBuilder.build()

'''
Output:
Running android tests
Linting the android code
Assembling the android build
Deploying android build to server
'''

iosBuilder = IosBuilder()
iosBuilder.build()

'''
Output:
Running ios tests
Linting the ios code
Assembling the ios build
Deploying ios build to server
'''
```


## Wrap Up Folks 🚦

And that about wraps it up. I will continue to improve this, so you might want to watch/star this repository to revisit. Also, I have plans on writing the same about the architectural patterns, stay tuned for it.


## Contribution 👬

- Report issues
- Open pull request with improvements
- Spread the word
- Reach out with any feedback
[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/kamranahmedse.svg?style=social&label=Follow%20%40_mildmelon)](https://twitter.com/_mildmelon)


## License

Creative Commons v4.0
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
