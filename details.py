from main import User, Credentials

def add_new_user(username, password):
    """
    creating a new user from user class with a username and password
    """
    new_user = User(username,password)
    return  new_user

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

            password = input("Create Password: ")

            password = input("Confirm Password: ")







if __name__ == '__main__':
    main()