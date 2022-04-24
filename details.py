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







if __name__ == '__main__':
    main()