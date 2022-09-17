# user_name = input('Ani Maghlakvelidze')

# user_password =input('ABCCBABCC')

# letters = input(9)

# print(f'Hello {user_name} , your password {user_password} is {letters} long')

username = input('What is your username ?')

password = input('what is your password')

password_length = len(password)

hidden_password = '*' * password_length

print(f'{username} , your password , {password} is {len(password)} letters long')