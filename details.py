from main import User,Credentials


def main():
    while True:
        print("Welcome to Password Locker!!")
        print('\n')
        print("Use these short codes:\n NA -Create new account \n LG -LogIn to your account \n or EX -exit")
        short_code = input().lower().strip()
        print('\n')

        if short_code == "NA":
            print('Create New Account')
            created_user_name = input()

            print('create password')
            created_password = input()

            print('Confirm Password')
            confirmed_password = input()







if __name__ == '__main__':
    main()