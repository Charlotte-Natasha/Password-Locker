class User:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def user_details(self):
        print("My name is" + self.username)



#username
username = str(input("Your username: "))

#website
website = str(input("Website: "))

#password
rand = "K34jndnks"
print(rand.isalnum())


def search():
    pass