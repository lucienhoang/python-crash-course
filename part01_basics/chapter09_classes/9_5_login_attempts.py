class User:
    """Model a User"""

    def __init__(self, first_name, last_name, gender, field):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.field = field
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User("Khoa", "Hoang", "Male", "IT")

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")

user_1.reset_login_attempts()
print(f"\nLogin attempts after reset: {user_1.login_attempts}")

# Login attempts: 4

# Login attempts after reset: 0
