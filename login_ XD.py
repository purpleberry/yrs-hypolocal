import pickle
users_file = open('users.dat', 'rb')
users = pickle.load(users_file)
users_file.close()

def login(username, password):
    if username in users:
        if users[username] == password:
            return True
    return False

while True:
    print("Login")
    username = input ("Username. (Caps sensitive)")
    password = input ("Password. Comes in letters. So make sure no one is behind u!!")
    if login(username, password) == True:
        print ('Congats U have made it this far. I am not sure how. But there you are!!.')
    else:
        print ('Try again. If u dare')


