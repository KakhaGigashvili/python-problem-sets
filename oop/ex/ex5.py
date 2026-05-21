class User():

    def __init__(self, first_name, last_name, login_attempts = 0):

        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        user_info = f"{self.first_name} {self.last_name}"

        print(user_info.title())

    def greet_user(self):

        message = f"Hello {self.first_name}"

        print(message)

    def increment_login_attempts(self):
       self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("nika", "lukadze")
user2 = User("luka", "nikadze")        
        

user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"login attempts: {user1.login_attempts}")

user1.reset_login_attempts()

print(f"reset: {user1.login_attempts}")




print("="*50)

user2.describe_user()
user2.greet_user()