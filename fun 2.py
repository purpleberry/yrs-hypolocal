import pickle
valid = False

users_file = open('users.dat', 'rb')
users = pickle.load(users_file)
users_file.close()

response = input("have you got an account (yes/no)")
if response == "no":
    while valid is False:
        print("make an account")
        username = input ("chose your username DO NOT use your real name!!!!")
        password = input ("chose your password and don't tell anyone.")
        confirm_password = input ("please confirm your password")
        if password == confirm_password:
            if username in users:
                print ('username already taken')
            else:
                valid = True
                users[username]=password
                print ('welldone account made.')
                user_file = open ('users.dat', 'wb')
                pickle.dump(users, user_file)
                user_file.close()
if response == "yes":
   import pickle

users_file = open('users.dat', 'rb')
users = pickle.load(users_file)
users_file.close()

#print (users['ik']

print('welcome to login')
loop = 'true'
while (loop == 'true'):
    username = input("username please : ")   
    password = input("password please : ")
    if username not in users :
        print("try user again")
    else:
        if users[username] != password :
            print ("try password again") 
            print('logged in well ' + username)
            loop = 'false'
            loop1 = 'true'
            while (loop1 == 'true'):
                command = input(username + " next bit will be on website")
            if (command == "exit" or "Exit"):
                break
            else:
                print ("'" + command + "' is not a valid password!!!!!")
        else:
            print ("welldone logged in XD") 
            
          

            
