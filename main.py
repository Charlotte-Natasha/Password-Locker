import string


class User:
    user_details = []

    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def save_user(self):
        User.user_details.append(self)

    def show_user(close):
        return close.user_details

    def delete_user(self):
        User.user_details.remove(self)

    def generate_password(stringLength=10):
        password = string.hexdigits

#username
#username = str(input("Your username: "))

#website
#website = str(input("Website: "))

#password
#rand = "K34jndnks"
#print(rand.isalnum())


#def search():
    #pass