import re;

def main():
    #                   Rotor Wiring Table
    #                   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    # Rotor 1 wiring:   J G D Q O X U S C A M I F R V T P N E W K B L Z Y H
    # Rotor 2 wiring:   N T Z P S F B O K M W R C J D I V L A E Y U X H G Q
    # Rotor 3 wiring:   J V I U B H T C D Y A K E Q Z P O S G X N R M W F L
    # Reflector 1:      E J M Z A L Y X V B W F C R Q U O N T S P I K H G D
    # Reflector 2:      F V P J I A O Y E D R Z X W G C T K U Q S B N M H L
    # global rotorBeta;
    # rotorBeta = {
    # "A":"N", "B":"T", "C":"C", "D":"Q", "E":"O", "F":"X", "G":"U", "H":"S", "I":"C", "J":"A",
    # "K":"M", "L":"I", "M":"F", "N":"R", "O":"V", "P":"T", "Q":"P", "R":"N", "S":"E", "T":"W",
    # "U":"K", "V":"B", "W":"L", "X":"Z", "Y":"Y", "Z":"H"
    # }
    global rotorAlpha;
    rotorAlpha = [
    ["A","J"], ["B","G"], ["C","D"], ["D","Q"], ["E","O"],
    ["F","X"], ["G","U"], ["H","S"], ["I","C"], ["J","A"],
    ["K","M"], ["L","I"], ["M","F"], ["N","R"], ["O","V"],
    ["P","T"], ["Q","P"], ["R","N"], ["S","E"], ["T","W"],
    ["U","K"], ["V","B"], ["W","L"], ["X","Z"], ["Y","Y"],
    ["Z","H"]
    ]


    # Turnover notches
    #   I             Q	      If rotor steps from Q to R, the next rotor is advanced
    #   II	          E    	  If rotor steps from E to F, the next rotor is advanced
    #   III	          V	      If rotor steps from V to W, the next rotor is advanced
    #   IV	          J	      If rotor steps from J to K, the next rotor is advanced
    #   V	          Z       If rotor steps from Z to A, the next rotor is advanced
    #   VI,VII,VIII	  Z+M	  If rotor steps from Z to A, or from M to N the next rotor is advanced

    # Rotor 1, 2 , 3 left to right, reflector 1 starting AAA, assume no increments
    # Input                 P
    # Step 1 (R3):          P -> P
    # Step 2 (R2):          P -> I
    # Step 3 (R1):          I -> C
    # Step 4 (Reflector):   C -> M
    # Step 5 (IvR1):        M -> F
    # Step 6 (IvR2):        F -> F
    # Step 7 (IvR3):        F -> H
    # Outcome               H

    print('Enigma Machine :)')
    validInput = False
    while not validInput:
        char = input("Give me a letter to encipher: ")
        if re.match("^[A-Z]$", char):
            nonIncrement(char.upper())
        else:
            print("Try again")
def nonIncrement():
    # print(rotorAlpha)
    # for i in range(len(rotorAlpha)):
    #     print(rotorAlpha[i][0] + ' --> ' + rotorAlpha[i][1])
    print(ord('A'))

main()
