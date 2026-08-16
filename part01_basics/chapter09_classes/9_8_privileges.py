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


class Moderator(User):
    """Model a Moderator."""

    def __init__(self, first_name, last_name, gender, field):
        super().__init__(first_name, last_name, gender, field)

        # Moderator privileges
        self.privileges = Privileges(["can delete comments", "can mute user"])


admin_1 = Admin("khoa", "hoang", "male", "IT")
print("Admin privileges list:")
admin_1.privileges.show_privileges()

mod_1 = Moderator("le", "dung", "female", "God")
print("Moderator privileges list:")
mod_1.privileges.show_privileges()


# Admin privileges list:
#    -can add post
#    -can delete post
#    -can ban user

# Moderator privileges list:
#    -can delete comments
#    -can mute user


#                  User
#                 /    \
#                /      \
#           Admin      Moderator
#              │            │
#              │ HAS-A      │ HAS-A
#              ▼            ▼
#         Privileges     Privileges
#              │            │
#        ┌─────┴─────┐   ┌──┴─────────────┐
#        │           │   │                │
#    add post    ban user  delete comments  mute user
