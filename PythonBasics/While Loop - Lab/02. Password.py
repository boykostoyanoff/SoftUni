username = input()
password = input()

while True:
    login_password = input()
    if login_password == password:
        print(f'Welcome {username}!')
        break
