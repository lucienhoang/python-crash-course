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


class Admin(User):
    """Model an Administrator."""

    def __init__(self, first_name, last_name, gender, field):
        super().__init__(first_name, last_name, gender, field)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"   -{privilege}")


admin_1 = Admin("khoa", "hoang", "male", "IT")
print("Admin privileges list:")
admin_1.show_privileges()

# Admin privileges list:
#    -can add post
#    -can delete post
#    -can ban user


# User
#  │
#  ├── first_name
#  ├── last_name
#  ├── gender
#  ├── field
#  │
#  ├── describe_user()
#  └── greet_user()
#        │
#        ▼
#      Admin
#        │
#        ├── inherit entire User
#        │
#        ├── privileges
#        │
#        └── show_privileges()
