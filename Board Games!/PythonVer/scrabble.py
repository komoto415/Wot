from functools import reduce

class Scrabble:
    def __init__(self):
        noLetterYet = ' '
        self.points = 0
        self.direction = ['x+', 'x-', 'y+', 'y-']
        self.boardSize = 10
        self.board = [[noLetterYet for i in range(self.boardSize)] for j in range(self.boardSize)]
        # Where (0,0) is the top left and (self.boardSize-1, self.boardSize-1) is the bottom right
        # board[COLOUMNS][ROWS]
        # Positive x and y are right and down
        # Indexed by zero
        self.tileSet = {
                'O' : 0,
                'L' : 1,
                'Z' : 2,
                'E' : 3,
                'A' : 4,
                'S' : 5,
                'G' : 6,
                'T' : 7,
                'B' : 8,
                'P' : 9
            }

    def placeTile(self, x, y, direction, tiles):
        assert set(tiles).issubset(set(self.tileSet.keys())), "Not a list of valid tiles"
        assert direction in self.direction, "Not a valid direction"
        assert 0 <= x < self.boardSize, "Not a valid x position on the board"
        assert 0 <= y < self.boardSize, "Not a valid y position on the board"
        assert x - len(tiles) >= 0 or len(tiles) + x < self.boardSize, "Cannot place off the board in the x direction"
        assert y - len(tiles) >= 0 or len(tiles) + y < self.boardSize, "Cannot place off the board in the y direction"
        assert self.allEmpty(x,y,direction,tiles), "Cannot place a tile where there already is one"


        # Need to account for placing tiles over existing tiles.
        # ex:
        #    State 1:
        #    ' ',' ',' ',' '
        #    ' ',' ',' ',' '
        #    'L','E','E','T'
        #    ' '.' ',' ',' '

        #    State 2: placeTile(1,0,'y+',['L','E','E','T'])
        #    ' ','L',' ',' '
        #    ' ','E',' ',' '
        #    'L','E','E','T'
        #    ' '.'T',' ',' '
        # Check that the would be intersected coordinate char is equal to the corresponding iterated incomingArr char
        # Using above example because explaining is hard: (Not proper code)
        # assert ['L','E','E','T'][2] == board[2][1]

        # A player doesn't technically place the intersected tile again, they place the tiles all around it.
        # You would do two 'seperate' placements
        # ex: instead of previous call:
        # placeTile(1,0,'y+',['L','E']) AND placeTile(1,3,'y+',['T'])

        # assert self.board[y][x] == ' ', "Can't place a tile here!"


        # Is there a way to insert directly with a range
        if 'x' in list(direction):
            # Can these be made functional;
            if '-' in list(direction):
                x = self.adjust(x, len(tiles))
            for letter in range(len(tiles)):
                self.board[y][x+letter] = tiles[letter]
        else:
            if '-' in list(direction):
                y = self.adjust(y, len(tiles))
            for letter in range(len(tiles)):
                self.board[y+letter][x] = tiles[letter]

        self.points += reduce((lambda x,y: x+y), list(map(lambda x: self.tileSet[x], tiles)))

    def adjust(self, coor, len):
        return coor - len + 1

    def allEmpty(self, x, y, direction, tiles):
        valid = True
        if 'x' in list(direction):
            # Can these be made functional;
            if '-' in list(direction):
                x = x - len(tiles) + 1
            for letter in range(len(tiles)):
                tile = self.board[y][x+letter]
                if tile != ' ':
                    valid = False
        else:
            if '-' in list(direction):
                y = y - len(tiles) + 1
            for letter in range(len(tiles)):
                tile = self.board[y+letter][x]
                if tile != ' ':
                    valid = False
        return valid

    def getBoard(self):
        board = ''
        [[print("a") for i in range(self.boardSize)] for j in range(self.boardSize)]

    # Don't need this
    def hasWordBeenMade(self):
        wordListR = []
        wordListC = []
        # Doesn't actually check if a word has been made yet, just joins the rows and coloumns to see what
        # strings are built from current state of the board
        for i in range(self.boardSize):
            wordListR.append(''.join(self.board[i]))
            wordListC.append(''.join(row[i] for row in self.board))
        print('Words by row:', wordListR)
        print('Words by coloum:', wordListC)
        wordList = wordListR + wordListC
        print('Combined words found: ')
        for word in range(len(wordList)):
            if (word == len(wordList)/2):
                print()
            print('[' + wordList[word] + ']')

    def getBoard(self):
        for rows in range(self.boardSize):
            if rows == 0:
                print('   ','    '.join(list(map(str,(list(range(0,self.boardSize)))))))
            print(rows,self.board[rows])

def main():
    board = Scrabble()
    b = board.board

    word1 = ['L','E','E','T']
    board.placeTile(9,3,'x-',word1)
    # Suppose to fail
    # board.placeTile(9,0,'y+',word1)
    board.placeTile(9,0,'y+',word1[0:3])
    print()
    board.getBoard()
    print()
    print(board.points)
main()
