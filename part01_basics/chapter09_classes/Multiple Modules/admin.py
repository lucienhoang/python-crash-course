from user import User
from privileges import Privileges


# Module Admin
class Admin(User):
    """Model an Administrator."""

    def __init__(self, first_name, last_name, gender, field):
        super().__init__(first_name, last_name, gender, field)

        # Admin privileges
        self.privileges = Privileges(
            ["can add post", "can delete post", "can ban user"]
        )
