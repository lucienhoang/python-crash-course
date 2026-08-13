# In object-oriented programming wou write classes that represent real-world things and
# situations, and you create objects based on these classes. When you wite a class,
# you define the general behavior that a whole category of objects can have.


class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attribute"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name.title()} rolled over!")
