class User():

    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        user_info = f"{self.first_name} {self.last_name}"

        print(user_info.title())

    def greet_user(self):

        message = f"Hello {self.first_name}"

        print(message)


class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):

        if self.privileges:
            for privilege in self.privileges:
                print(privilege)
        else:
            print("This admin currently has no special privileges.")


class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

        self.privileges = Privileges()


privileges = [
    "can add post",
    "can delete post",
    "can ban user"
]

user_is_admin = Admin("nika", "lukadze")

user_is_admin.privileges.privileges = privileges

user_is_admin.describe_user()

user_is_admin.privileges.show_privileges()