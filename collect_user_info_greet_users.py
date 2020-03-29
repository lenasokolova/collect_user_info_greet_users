class User():
    def __init__(self, first_name, last_name, country, location):
        self.name = first_name.title()
        self.surname = last_name.title()
        self.country = country.title()
        self.location = location.title()

    def describe_user(self):
         print("\nUsername: ", {self.name}, {self.surname})
         print("Country: ", {self.country})
         print("City: ", {self.location})


    def greet_user(self):
        msg = "Hello, "+ self.name + " " + self.surname + "!"
        print(msg)

user_0 = User('lily', 'allen', 'usa', 'new york')
user_1 = User('monica', 'bellucci', 'italy', 'rome')
user_2 = User('antonio', 'banderaz', 'spain', 'madrid')

user_0.describe_user()
user_0.greet_user()

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()