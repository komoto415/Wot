import re
import Enigma


def main():
    print('Rotor Placements')
    print(' _____________________________ ')
    print('|   __     __     __     __   |')
    print('|  |  | < |  | < |  | < |  |  |')
    print('|  |rf|   |r1|   |r2|   |r3|  |')
    print('|  |__| > |__| > |__| > |__|  |')
    print('|  q w e r t y u i o p    bck |')
    print('|   a s d f g h j k l    entr |')
    print('|    z x c v b n m        suh |')
    print('|_____________________________|')

    #               Rotor Wiring Table
    #                           A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

    # Rotor Alpha wiring:       J G D Q O X U S C A M I F R V T P N E W K B L Z Y H
    # Rotor Beta wiring:        N T Z P S F B O K M W R C J D I V L A E Y U X H G Q
    # Rotor Charlie wiring:     J V I U B H T C D Y A K E Q Z P O S G X N R M W F L
    # Reflector Alpha:          E J M Z A L Y X V B W F C R Q U O N T S P I K H G D
    # Reflector Beta:           F V P J I A O Y E D R Z X W G C T K U Q S B N M H L

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

    global alphabet, rotorAlphaList, rotorBetaList, rotorCharlieList, reflectorAlphaList, reflectorBetaList, rotorOrder;

    alphabet = getSubstitutions('alphabet')

    rotorAlphaList = Enigma.Rotor(makeDict([], getSubstitutions('rotorAlpha')))

    rotorBetaList = Enigma.Rotor(makeDict([], getSubstitutions('rotorBeta')))

    rotorCharlieList = Enigma.Rotor(makeDict([], getSubstitutions('rotorCharlie')))

    reflectorAlphaList = Enigma.Rotor(makeDict([], getSubstitutions('reflector1')))

    reflectorBetaList = Enigma.Rotor(makeDict([], getSubstitutions('reflector2')))

#     All Dicts
#     global rotorAlphaDict;
#     rotorAlphaDict = {}
#     reflectorBetaDict = makeDict({},getSubstitutions('rotor1'))
#
#     global rotorBetaDict;
#     rotorBetaDict = {}
#     reflectorBetaDict = makeDict({},getSubstitutions('rotor2'))
#
#     global rotorCharlieDict;
#     rotorCharlieDict = {}
#     reflectorBetaDict = makeDict({},getSubstitutions('rotor3'))
#
#     global reflectorAlphaDict;
#     reflectorBetaDict = makeDict({},getSubstitutions('reflector1'))
#
#     global reflectorBetaDict;
#     reflectorBetaDict = makeDict({},getSubstitutions('reflector2'))

    # Send order is as seen in my pretty picture
    rotorOrder = selectRotorOrder(reflectorAlphaList,rotorAlphaList,rotorBetaList,rotorCharlieList)
    while True:
#         char = input("Give me a letter to encipher: ")
        char = 'A'
        if re.match("^[A-Z]$", char):
            print('Input -->', char)
            # output = 'A'
            output = nonIncrementListRec(char,0)
#             output = nonIncrementListItr(char)
            print('\nOutput -->', output)
            print(char + ' --> ' + output)
            return False
        else:
            print("Try again")

def makeDict(liste, subs):
    for i in range(26):
        liste.append([alphabet[i],subs[i]])
    return liste

def makeDict(dicte, subs):
    for i in range(26):
        dicte[alphabet[i]] = subs[i]
    return dicte

def getSubstitutions(sub):
    textFile = sub + '.txt'
    with open(textFile, 'r') as subFile:
        return (subFile.readline().split(" "))

def selectRotorOrder(r1, r2, r3, rf):
    return [r3,r2,r1,rf,r1,r2,r3]

def nonIncrementListItr(char):
    for i in range(len(rotorOrder)):
        print(char)
        j = ord(char) - 65
        char = rotorOrder[i][j][1]
        print(char)
    return char

def nonIncrementListRec(char, step):
    index = ord(char) - 65
    print(char)
    if (step == len(rotorOrder)):
        return char
    char = rotorOrder[step][index][1]
    print(char)
    return nonIncrementListRec(char, step+1)

# def nonIncrementDict(char):
#     print(rotorAlphaDict)
#     print(rotorAlphaDict[char])
#     return True

main()
