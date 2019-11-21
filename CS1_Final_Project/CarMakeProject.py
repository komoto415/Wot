import re
from os import path

def main():
    # Allow access to these variables in any method without the need of sending them as parameters
    global userName
    global state
    userName = input("What is your name: ")

    # Main Menu Component
    # Will contain all the interacting subcomponents
    mainMenu()

def mainMenu():
    userResponse = -1
    state = 0
    # While will force the user to stay in the main menu until they input a valid entry
    while (userResponse != 4):
        # Checks if the user has run the application before
        # State simply makes it so that the previous selections don't appear everytime if the case the user 
        # puts invalid inputs and just presents on launch
        if path.exists('showroomInfo.txt') and beenHereBefore() and state == 0:
                state = 1

        menuDelimeter()
        print('Welcome to our showroom! ')
        menuList(['BMW', 'Chevy', 'Audi', 'Exit Program'])

        # Input validation
        try:
            userResponse = int(input("Please select the make you desire: "))
        except ValueError as e:
            print(e)
        if (userResponse > 4 or userResponse < 1):
            print('\nThat is not a valid option. Select between 1-4 only.')
        elif userResponse != 4:
            menuDelimeter()
            print('Model: ')
            # Get a list of the desired make and its model
            # Contains model selection subcomponent
            baseList = makeChosen(userResponse)

            menuDelimeter()
            addOnList = selectAccessories();
            allInOne = baseList + addOnList
            menuDelimeter()

            print('List of your choices:')
            printAll(allInOne)

            # Checking if user has selected everything they've wanted
            done = False
            while not done:
                done = input('Are you sure this is what you want? (y/n)? ')
                if not re.match("^n|y$", done):
                    print("\nNot valid option")
                else:
                    if re.match("^y$", done):
                        if path.exists('showroomInfo.txt') and beenHereBefore():
                            removeExisting()
                        # We want this at the very end in case the user manual turns off the program
                        # preventing uncompleted data from entering out table
                        addToFile(allInOne)
                        userResponse = 4
                    done = True;

def menuDelimeter():
    print('*'*50)

def beenHereBefore():
    # This, removeExisting and addToFile methods utilises "with open('file.txt', 'r') as"
    # Allows us to represent the text file as an accessible object and allows
    # us the usage of the "in" key word, and doesn't require the potential side effect of
    # forgetting to close a file
    with open('showroomInfo.txt', 'r') as showroomInfo:
        for line in showroomInfo:
            splitInfo = line.split()
            if userName == splitInfo[0]:
                menuDelimeter()
                print('Welcome back ' + userName + '! Here are your previous selection:')
                printAll(splitInfo[1:])
                return True
    return False

def removeExisting():
    with open("showroomInfo.txt", "r") as showroomInfo:
        lines = showroomInfo.readlines()
    with open("showroomInfo.txt", "w") as showroomInfo:
        for line in lines:
            splitLine = line.split()
            if splitLine[0] != userName:
                showroomInfo.write(line)

def addToFile(allInOne):
    # Adding a row to the file
    with open('showroomInfo.txt', 'a+') as showroomInfo:
        showroomInfo.write(userName + ' ')
        for i in range(len(allInOne)):
            showroomInfo.write(str(allInOne[i]) + ' ')
        showroomInfo.write('\n')    
         
def printAll(infoList):
    #Print the list of all the selections
    print('Car Make: ' + infoList[0] +
          '\nModel: ' + infoList[1] +
          '\nSun Roof: ' + ('Yes' if 'SunRoof' in infoList else 'No') +
          '\nBackup Camera: ' + ('Yes' if 'BackupCamera' in infoList else 'No') +
          '\nBlind Spot Monitor : ' + ('Yes' if 'BlindSpotMonitor' in infoList else 'No') +
          '\nTotal Accessories Cost: ' + str(infoList[5]) +
          '\nTotal Cost: ' + str(infoList))

def selectAccessories():
    addOnPrice = 0;
    validFormat = False;
    while not validFormat:
        print('Add Ons: ')
        menuList(['Sun Roof', 'Backup Camera', 'Blind Spot Monitor'])
        print('Please enter input as integers seperated by commas e.g: "int,int"')
        addOnSelected = input("Please put in desired add-ons: ")
        # As this is more complicated than length 1 strings, RegEx string validation allows us enforce matching components of
        # a string rather than making disgustingly big if else chains.
        # In addition, this allows the user to select multiple options and be prompted a single time rather than only 
        # being allowed to pick on option at a time and be asked if they'd like to continue choosing
        validFormat = re.match("^[1-3]$|^[1-3],[1-3]$|^[1-3],[1-3],[1-3]$", addOnSelected)
        if not validFormat:
            print('Incorrect formating. Please try again!')
    addOnList = addOnSelected.split(',')

    addOn1 = 'null'
    addOn2 = 'null'
    addOn3 = 'null'

    # Since we don't want users to buy multiple of the same option, we are just looking for if our array contains the desired 
    # add on. Key word 'in' only cares about the value existing in the container, not how many times it occurs in the container
    # Note, it can be easily modified to if we wanted the user to select multiples of the same option
    # Count occurence of choice in container and append the occurence to the string
    if '1' in addOnList:
        addOnPrice += 1000;
        addOn1 = 'SunRoof'

    if '2' in addOnList:
        addOnPrice += 2000;
        addOn2 = 'BackupCamera'

    if '3' in addOnList:
        addOnPrice += 3000;
        addOn3 = 'BlindSpotMonitor'
    price = 50000 + addOnPrice
    return [addOn1, addOn2, addOn3, addOnPrice, price];

def makeChosen(make):
    model = False
    # While loop makes sure user stays in the menu in case of invalid input
    # Here we are abusing Python's dynamic typing
    # The idea is that in the case of invalid input we break out of the selectModeOf methods immediately model as a boolean value,
    # if proper input, model is then a string. Kind of hacky, but works
    # Returns container because it will allow us to send multiple values in one method. Additionally, its ordering is structured
    # such that it is one-to-one with how we want our table to look like in our file
    while not model:
        if make == 1:
            menuList(['M3', 'X5', 'I8'])
            model = selectModelOf('BMW')
            if model:
                baseList = ['BMW', model]
        elif make == 2:
            menuList(['Silverado', 'Malibu', 'Tahoe'])
            model = selectModelOf('Chevy')
            if model:
                baseList = ['Chevy', model]
        else:
            menuList(['A6', 'Q3', 'S3'])
            model = selectModelOf('Audi')
            if model:
                baseList = ['Audi', model]
    return baseList

def selectModelOf(make):
    # Simple hard coded return values based on input
    # Could be a switch case instead of else if chain
    try:
        selected = int(input("Please select the model you desire: "))
    except ValueError as e:
        print(e)
        return False
    model = False;
    if (selected > 3 or selected < 1):
        print('\nThat is not a valid option. Select between 1-3 only.')
    
    else:
        model = ''
        if (make == 'BMW'):
            if (selected == 1):
                model = 'M3'
            elif (selected == 2):
                model = 'X5'
            elif (selected == 3):
                model = 'i8'

        elif (make == 'Chevy'):
            if (selected == 1):
                model = 'Silverado'
            elif (selected == 2):
                model = 'Malibu'
            elif (selected == 3):
                model = 'Tahoe'

        elif (make == 'Audi'):
            if (selected == 1):
                model = 'A6'
            elif (selected == 2):
                model = 'Q5'
            elif (selected == 3):
                model = 'S3'
    return model

def menuList(optList):
    # General menu building method
    # Special case toString truth be told
    for i in range(len(optList)):
        print('\t' + str(i+1) +') ' + optList[i])

main()
