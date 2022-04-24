import random
import string


class User:
    user_details = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
        User.user_details.append(self)

    def show_user(close):
        return close.user_details

    def delete_user(self):
        User.user_details.remove(self)


class Credentials:
    credentials_details = []

    def __init__(self, account, username, password):
        self.account = account
        self.username = username
        self.password = password

    def save_credentials(self):
        Credentials.credentials_details.append(self)

    def delete_credentials(self):
        Credentials.credentials_details.remove(self)

    def generate_password(stringLength=10):
        password = string.hexdigits + "k&%)@#$"
        return ''.join(random.choice(password) for i in range(stringLength))

    @classmethod
    def find_by_account(cls, param):
        pass

    @classmethod
    def credential_exists(cls, param):
        pass

    @classmethod
    def display_credentials(cls):
        pass

    @classmethod
    def credential_list(cls):
        pass

    @classmethod
    def copy_password(cls, param):
        pass

#username
#username = str(input("Your username: "))

#website
#website = str(input("Website: "))

#password
#rand = "K34jndnks"
#print(rand.isalnum())


#def search():
    #pass