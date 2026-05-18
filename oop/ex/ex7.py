class User():

    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        user_info = f"{self.first_name} {self.last_name}"

        print(user_info.title())

    def greet_user(self):

        massage = f"Hello {self.first_name}"

        print(massage)

class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)

        self.privileges = privileges

    def show_privileges(self):
        for admin in self.privileges:
            print(f"Admin can {admin}")

privileges =["can add post", "can delete post", "can ban user"]

user_is_admin = Admin("nika", "lukadze", privileges)

user_is_admin.describe_user()
user_is_admin.show_privileges()