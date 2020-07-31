import getpass

user = getpass.getuser()
passwd = getpass.getpass()

if svc_login(user, passwd): # You must write svc_login()
    print('Yay!')
else:
    print('Boo!')

# above will default to the system username, can explicitly ask for it like this
user = input('Enter your username: ')
