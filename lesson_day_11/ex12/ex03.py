class User:
    def __init__(self, first_name, last_name, login_attemps = 0):
        self.attemps = login_attemps
        self.fname = first_name
        self.lname = last_name
    def describe_user(self):
        print(f"Users first name is {self.fname}")
        print(f"Users last name is {self.lname}")
    def greet_user(self):
        print(f"Hello {self.fname} {self.lname}")
    def increment_login_attempts(self):
        self.attemps = self.attemps + 1
        print(f'{self.attemps} attempted')
    def reset_login_attempts(self):
        self.attemps = 0
        print(f'{self.attemps} attempted')
user1 = User('Serlen' , 'Jam')
user2 = User('Mungun', 'Jiguur')
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
user2.describe_user()
user2.greet_user()