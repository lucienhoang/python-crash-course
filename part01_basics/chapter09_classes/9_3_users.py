class User:
    """Model a User"""

    def __init__(self, first_name, last_name, gender, field):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.field = field

    def describe_user(self):
        print("\nUser information:")
        print(f"First name: {self.first_name.title()}")
        print(f"Last name: {self.last_name.title()}")
        print(f"Gender: {self.gender}")
        print(f"Field: {self.field}")

    def greet_user(self):
        print("---")
        # name = self.first_name.title() + " " + self.last_name.title()
        name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Hello {name}!")


user_1 = User("Khoa", "Hoang", "Male", "IT")
user_2 = User("Dung", "Le", "Female", "Korean culture")
user_3 = User("Laurence", "Huynh", "Male", "English")

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()


# User information:
# First name: Khoa
# Last name: Hoang
# Gender: Male
# Field: IT
# ---
# Hello Khoa Hoang!

# User information:
# First name: Dung
# Last name: Le
# Gender: Female
# Field: Korean culture
# ---
# Hello Dung Le!

# User information:
# First name: Laurence
# Last name: Huynh
# Gender: Male
# Field: English
# ---
# Hello Laurence Huynh!
