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

user1 = User("nika", "lukadze")
user2 = User("luka", "nikadze")        
        

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()