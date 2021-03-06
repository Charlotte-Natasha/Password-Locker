from main import User, Credentials


def add_new_user(username, password):
    """
    creating a new user from user class with a username and password
    """
    new_user = User(username, password)
    return new_user


def save_user(user):
    """
    Function to save a new user
    """
    user.adduser()


def show_user():
    """
    Function to display existing user
    """
    return User.show_user()


def account_user(username, password):
    """
    Checks whether a user exists and the logs in the user
    """
    check_user = Credentials.account_user(username, password)
    return check_user


def new_credentials(account, username, password):
    """
    Creates new credentials for the persons user accounts
    """
    new_credential = Credentials(account, username, password)
    return new_credential


def save_credentials(credentials):
    """
    saves credentials from the list
    """
    credentials.save_details()


def display_account_details():
    """
    Returns all the saved account credentials
    """
    return Credentials.display_credentials()


def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()


def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)


def check_credentials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false
    """
    return Credentials.if_credential_exist(account)


def generate_password():
    """
    Generate a random password for the user
    """
    auto_password = Credentials.generate_password()
    return auto_password


def main():
    while True:
        print("Welcome to Password Locker!!")
        print('\n')
        print("Enter one of the following to proceed:\n na -Create new account \n lg -LogIn to your account \n ex -exit")
        short_code = input().lower().strip()
        print('\n')

        if short_code == "na":
            print('Create New Account')
            username = input("Provide username: ")

            #print("Create password")
            password = input("Create Password: ")

            #print("Confirm Password")
            confirm_password = input("Confirm Password: ")

            while confirm_password != password:
                print("Invalid password. Did not match!!")
                print("Enter your password")
                password = input()
                confirm_password = input()
                print("Confirm your password")

            else:
                print("Congrats. Account was created successfully")
                print('\n')
                print("Proceed to login")
                print('Username')
                enter_username = input()
                print("Your password")
                enter_password = input()

            while enter_username != username or enter_password or password:
                print("Invalid username or password")
                print("Enter username")
                enter_username = input()
                print("Your password")
                enter_password = input()

            else:
                print("Welcome to your account")
                print("\n")

        elif short_code == "lg":
            print("Welcome")
            print("Enter your username")
            default_username = input()

            print("Enter your password")
            default_password = input()
            print('\n')

            while default_username != 'test' or default_username:
                print("Wrong username or Password")
                print("Enter user name")
                default_username = input()

                print("Enter password")
                default_password = input()
                print('\n')

            else:
                print("Login Success")
                print('\n')

        elif short_code == 'ex':
            print("Thankyou for using Password-Locker. See you soon :)")
            break

        else:
            print("Wrong entry try again")


if __name__ == '__main__':
    main()
