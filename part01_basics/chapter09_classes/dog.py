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


my_dog = Dog("bi xanh", 3)
your_dog = Dog("lucy", 2)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()


# My dog's name is Bi Xanh.
# My dog is 3 years old.
# Bi Xanh is now sitting.
# Bi Xanh rolled over!

# Your dog's name is Lucy.
# Your dog is 2 years old.
# Lucy is now sitting.
