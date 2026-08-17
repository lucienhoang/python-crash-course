# Module Privileges
class Privileges:
    """Model the privileges of user."""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"   -{privilege}")
