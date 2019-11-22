def main():
    textFile = 'rotor1.txt'
    with open(textFile, 'r') as subFile:
        line = subFile.readline()
        subs = line.split(" ")
        print(line)
        print(subs)
main()
