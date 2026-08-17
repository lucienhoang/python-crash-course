# Module Admin
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


class Privileges:
    """Model the privileges of user."""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"   -{privilege}")


class Admin(User):
    """Model an Administrator."""

    def __init__(self, first_name, last_name, gender, field):
        super().__init__(first_name, last_name, gender, field)

        # Admin privileges
        self.privileges = Privileges(
            ["can add post", "can delete post", "can ban user"]
        )
