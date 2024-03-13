from user2 import User

class Privileges:
    """A separate privileges class."""

    def __init__(self):
        self.privileges = ['can add post',
                           'can delete post',
                           'can ban user']

    def show_privileges(self):
        print(f"\nThe privileges of administrator are: ")
        for privilege in self.privileges:
            print(f"\t{privilege}")

class Admin(User):
    """A new admin class definition."""

    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()