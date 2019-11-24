# Car Shopping Group Project by Professor Sundararajan
# Implemented by Stephanie Lao, Caleb Cramer, and Rhea Loney

from os import path

def main():
    
    userName = input("Please enter your name: ")

    # Check if the file exists and if so, check if the same user has seen a car before.
    # If yes, display previous selections. If not, print first time user welcome message.
    # If the file does not exist, also print first time user welcome message.

    if path.exists("showroomInfo.txt"):
        try:
            fileObj = open("showroomInfo.txt", "r")
        except Exception as err:
            print(err)
        data = fileObj.readline()
        data = data.rstrip("\n")

        if userName.lower() == data.lower():
            print()
            print("Welcome back,", userName, "!")
            print("Here are your previous selections:")
            data = fileObj.readline()
            while data != "":
                data = data.rstrip("\n")
                print(data)
                data = fileObj.readline()
                 
            fileObj.close()
        else:
            print("First time user, welcome to our showroom!")          
    else:
        print("First time user, welcome to our showroom!")  
     
    # Open the file in write mode and write the user's selections into the file 
    # throughout the main function.
     
    fileObj = open("showroomInfo.txt", "w")     
    fileObj.write(userName + "\n")  
    
    # Print the menu of makes. Use input validation to check if the user enters strings,
    # floats, or integers not available on menu. Based on the user input, call the bmw,
    # chevy, or audi functions.
    
    makeInput = 0 
    while makeInput != 4:
        print()
        print("""List of makes:
        1. BMW
        2. Chevy
        3. Audi
        4. Exit the program""")
        try:
            makeInput = int(input("Please select a number of the listed makes:"))
        except ValueError:
            print()
        if makeInput > 4 or makeInput < 1:
            print("Please make a valid selection.")
            print()
        elif makeInput == 1:
            fileObj.write("Make: BMW\n") 
            fileObj.close()
            bmw()
            break
        elif makeInput == 2:
            fileObj.write("Make: Chevy\n") 
            fileObj.close() 
            chevy()
            break
        elif makeInput == 3:
            fileObj.write("Make: Audi\n") 
            fileObj.close() 
            audi()
            break
        elif makeInput == 4:
            print("You have exited the showroom.")
            fileObj.close()
                    
def bmw():
    
    # Open the file in append mode and append the user's selections into the file
    
    try:
        fileObj = open("showroomInfo.txt", "a")
    except Exception as err:
        print(err)
        
    # Print the menu of models. Use input validation to check if the user enters strings,
    # floats, or integers not available on menu. Call the options function once the user
    # inputs what model they want.
        
    bmwInput = 0
    while bmwInput != 4:
        print()
        print("""BMW Models:
        1.M3
        2.X5
        3.i8
        4.Exit the program""")
        try:
            bmwInput = int(input("Please select a number of the listed BMW models:"))
        except ValueError:
            print()
        if bmwInput > 4 or bmwInput < 1:
            print("Please make a valid selection.")
            print()
        elif bmwInput == 1:
            fileObj.write("Model: M3\n")
            fileObj.close()
            options()
            break
        elif bmwInput == 2:
            fileObj.write("Model: X5\n")
            fileObj.close() 
            options()
            break
        elif bmwInput == 3:
            fileObj.write("Model: i8\n")
            fileObj.close()
            options()
            break 
        elif bmwInput == 4:
            print("You have exited the showroom.")

def chevy():
    
    # This follows the same flow as the previous bmw function, except providing a list of
    # available chevy models.
    
    try:
        fileObj = open("showroomInfo.txt", "a")
    except Exception as err:
        print(err)
        
    chevyInput = 0
    while chevyInput != 4:
        print()
        print("""Chevy models:
        1. Silverado
        2. Malibu
        3. Tahoe
        4. Exit the program""")
        try:
            chevyInput = int(input("Please select a number of the listed Chevy models:"))
        except ValueError:
            print()
        if chevyInput > 4 or chevyInput < 1:
            print("Please make a valid selection.")
            print()
        elif chevyInput == 1:
            fileObj.write("Model: Silverado\n")
            fileObj.close()
            options()
            break 
        elif chevyInput == 2:
            fileObj.write("Model: Malibu\n") 
            fileObj.close()
            options()
            break
        elif chevyInput == 3:
            fileObj.write("Model: Tahoe\n") 
            fileObj.close()
            options()
            break
        elif chevyInput == 4:
            print("You have exited the showroom.")
            fileObj.close()

def audi():
    
    # This follows the same flow as the previous bmw and chevy functions, except 
    # providing a list of available audi models.
    
    try:
        fileObj = open("showroomInfo.txt", "a")
    except Exception as err:
        print(err)
    
    audiInput = 0
    while audiInput != 4:
        print()
        print("""Audi models:
        1. A6
        2. Q5
        3. S3
        4. Exit the program""")
        try:
            audiInput = int(input("Please select a number of the listed Audi models:"))
        except ValueError:
            print()
        if audiInput > 4 or audiInput < 1:
            print("Please make a valid selection.")
            print()
        elif audiInput == 1:
            fileObj.write("Model: A6\n") 
            fileObj.close()
            options()
            break
        elif audiInput == 2:
            fileObj.write("Model: Q5\n")
            fileObj.close() 
            options()
            break
        elif audiInput == 3:
            fileObj.write("Model: S3\n") 
            fileObj.close()
            options()
            break
        elif audiInput == 4:
            print("You have exited the showroom.")
            fileObj.close()
        
def options():
    
    try:
        fileObj = open("showroomInfo.txt", "a")
    except Exception as err:
        print(err)
    
    # Use accumulators for the while loop to get the options cost. Append to the dictionary
    # throughout the loop to print the options and corresponding costs. Use input validation
    # like shown previously. Use existList so when a user picks an option more than once,
    # the options cost does not update.
            
    print()
    basePrice = 50000
    sunRoof = 1000
    backupCamera = 2000
    blindSpotMonitor = 3000
    optionsCost = 0
    optionsDict = {}
    existList = []
    optionsInput = 0
    
    while optionsInput != 4:
        optionsInput = 0
        print()
        print("""Options:
        1. Sun roof
        2. Backup Camera
        3. Blindspot Monitor
        4. Exit the options menu""")
        try:
            optionsInput = int(input("Please select a number of the listed options:"))
        except ValueError:
            print()
            print("Please enter an integer 1-4.")
        if optionsInput > 4 or optionsInput < 1:
            print("Please make a valid selection.")
            print()
        elif optionsInput == 1 and not sunRoof in existList:
            optionsCost += sunRoof
            optionsDict["Sun roof"] = sunRoof
            existList.append(sunRoof)
        elif optionsInput == 2 and not backupCamera in existList:
            optionsCost += backupCamera
            optionsDict["Backup Camera"] = backupCamera
            existList.append(backupCamera)
        elif optionsInput == 3 and not blindSpotMonitor in existList:
            optionsCost += blindSpotMonitor
            optionsDict["Blind spot monitor"] = blindSpotMonitor 
            existList.append(blindSpotMonitor)
        elif optionsInput == 4:
            print()
            print("You have exited the options menu.")
            print()
            break
    
    print("Base price: $", basePrice)
    strBasePrice = str(basePrice)
    fileObj.write("Base Price: $" + strBasePrice + "\n")

    for key, value in optionsDict.items():
        print("Option and corresponding price: ", key, ": $", value)
        fileObj.write("Option:" + key + "; Price: $" + str(value) + "\n")
            
    totalCost = basePrice + optionsCost
    print("Total cost: $", totalCost)
    fileObj.write("Total cost: $" + str(totalCost) + "\n")

    fileObj.close()
        
main()