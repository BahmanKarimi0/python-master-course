while (user_name := input("Enter your name: ")).strip() == '':
    print("Please enter a valid name.")


def greet_user(user_name):
    print(f'Hello, {user_name}! Welcome aboard. 👋')


greet_user(user_name)
