def main():
    userResponse = 0
    while (userResponse != 3): 
        print("""
        1) Create  Username and Password
        2) Log In
        3) Exit Program
        """)
        try: 
            userResponse = int(input("Please enter which option you'd like: "))
        except ValueError as e: 
            print(e)
            quit()
            
        if (userResponse > 3 or userResponse < 1):
            print('\nThose are not valid options. Select between 1-3 only.')
        
        elif userResponse == 1:
            createAccount()
    
        elif userResponse == 2:
            logIn()

    print('\nThe program has been exited.')
    

def createAccount():
    print()
    try: 
        UserPassFile = open('UserPass.txt', 'a+')
    except Exception as e:
            print(e)
            quit() 
    
# User creates and new user name
    print('Your username must be an email with an .edu extension.')
    newUser = makeUsername()
   
# User creates a password.
    print('\nYour Password must be 6-10 characters and include at least one number.')
    newPass =  makePassword()
    
    print('\nCongragulations, your account has been created.')
    
# Store the new username and password into the text file              
    UserPassFile.write(newUser)
    UserPassFile.write(' ')
    UserPassFile.write(newPass)
    UserPassFile.write('\n')
    UserPassFile.close


def makeUsername():
    while True:
        newUser = input('Enter in your desired username: ')
        # Checks to see if it is an email and has the proper extension
        if '@' in newUser and '.edu' in newUser:
            # if userExist returns True
            if userExist(newUser):
                print('\nThat email already exists. Please enter a new one.')
            else:
                break
        else:
            print('\nThis is not a proper email. Please enter a new one.')
    return newUser


def makePassword():
    while True:                
        newPass = input('Enter in your desired password: ')
        if len(newPass) < 6:
            print('\nYour password is too short. Please enter a new one.')
        elif len(newPass) > 10:
            print('\nYour password is too long. Please enter a new one.')
        elif any(i.isdigit() for i in newPass) == False :
            print('\nYour password has no numbers. Please enter a new one.')
        else:
            break
    return newPass


def logIn():
    print()
    try:
        UserPassFile = open('UserPass.txt', 'r')
    except Exception as e:
        print("No database with accounts exists for this program yet.")
        print(e)
        quit()

# Take the lines in the text file, convert them into a list and then store them into a dictionary
    UserPassDict = {}
    # For each line in the text file,
    for UserPass in UserPassFile:
        splitUserPass = UserPass.split()
        # Make element in index 0 our username
        username = splitUserPass[0]
        # Make element in index 1 our password
        password = splitUserPass[1]
        # Store those variables into a dictionary
        UserPassDict[username] = password

# Verified login        
    while True:        
        UserUserInput = input('Please enter your username: ')
        UserPassInput = input('Please enter your password: ')
        # If the username inputed by the user exists as a key in the dictionary AND if that key's key value is equal to the password inputed by the user
        if UserUserInput in UserPassDict and UserPassDict[UserUserInput] == UserPassInput:
            print('\nLogin in successful')
            break
        else:
            print('\nYour password is incorrect, please try again.')          
 
            
def userExist(userName):
    try:
        with open('UserPass.txt', 'r') as UserPassFile:
            for line in UserPassFile:
                # Take the lines from the text file and put them into the list, 
                splitUserPass = line.split()
                # and check if the inputed username is equal to a username already exists in the text file
                if userName == splitUserPass[0]:
                    # Desired username is taken
                    return True
    except Exception as e:
        print(e)
    # Desired username is acceptable
    return False


main()


