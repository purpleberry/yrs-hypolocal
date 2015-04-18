import pickle
users_file = open('users.dat', 'rb')
users = pickle.load(users_file)
users_file.close()

def make_acc(username, password):
    if username in users:
        return False
    else:
        users[username]=password
        user_file = open ('users.dat', 'wb')
        pickle.dump(users, user_file)
        user_file.close()
        return True

while True:
    print("make an account")
    username = input ("chose your username DO NOT use your real name!!!!")
    password = input ("chose your password and don't tell anyone.")
    confirm_password = input ("please confirm your password")
    if password == confirm_password:
        if make_acc(username, password) == True:
            print ('welldone account made.')
        else:
            print ('Username already taken')
    else:
        print ('Passwords don\'t match. Please try again.')


