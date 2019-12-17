from functools import reduce

class Scrabble:
    def __init__(self):
        self.startPos = 'X'
        self.noLetterYet = '-'
        self.points = 0
        self.boardSize = 15
        self.board = [[self.noLetterYet for i in range(self.boardSize)] for j in range(self.boardSize)]
        self.board[7][7] = self.startPos
        # Where (0,0) is the top left and (14,14) is the bottom right
        # board[COLOUMNS][ROWS] unfortunately no way around this. I think
        # Positive x and y are right and down
        # The matrix will be indexed by 0
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
        assert direction in ['x+', 'x-', 'y+', 'y-'], "Not a valid direction"
        assert 0 <= x < self.boardSize, "Not a valid x position on the board"
        assert 0 <= y < self.boardSize, "Not a valid y position on the board"
        assert x == y and x == 7 if points == 0 else True, "The first set of tiles have to go over the starting position"
        assert self.check(x, direction, len(tiles)) if 'x' in direction else True, "Cannot place off the board in the x direction"
        assert self.check(y, direction, len(tiles)) if 'y' in direction else True, "Cannot place off the board in the y direction"
        assert self.allEmpty(x,y,direction,tiles), "Cannot place a tile where there already is one"

        # Is there a way to insert directly with a range
        if 'x' in list(direction):
            # Can these be made functional?
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

    def validStart(self):
        print()

    def check(self, coor, direction, len):
        valid = True
        if '-' in direction:
            valid = coor - len >= 0
        elif '+' in direction:
            valid = len + coor < self.boardSize
        return valid

    def allEmpty(self, x, y, direction, tiles):
        valid = True
        index = 0
        coor = x if 'x' in direction else y
        if '-' in list(direction):
            coor = x - len(tiles) + 1 if 'x' in direction else y - len(tiles) + 1
        while index < len(tiles) and valid:
            tile = self.board[y][coor+index] if 'x' in direction else self.board[coor+index][x]
            if tile != self.noLetterYet and tile != self.startPos:
                valid = False
            index += 1
        return valid

    def getBoard(self):
        s = '  '
        for rows in range(self.boardSize):
            if rows == 0:
                print(s,s.join(list(map(str,(list(range(0,10)))))),s[0:1].join(list(map(str,(list(range(10,self.boardSize)))))))
            printThis = str(rows) + s[0:1]
            printThis += s.join(self.board[rows]) if rows > 9 else s[0:1] + s.join(self.board[rows])
            printThis += s[0:1] +str(rows)
            print(printThis)
            if rows == self.boardSize-1:
                print(s,s.join(list(map(str,(list(range(0,10)))))),s[0:1].join(list(map(str,(list(range(10,self.boardSize)))))))


    def reset(self):
        self.__init__()

    # def getBoardPretty(self):
def main():
    board = Scrabble()
    word1 = ['L','E','E','T']
    board.placeTile(9,3,'y+',word1)

    # Suppose to fail
    # board.placeTile(9,6,'y+',word1)

    # Suppose to fail
    # board.placeTile(14,14,'y+',word1)

    board.getBoard()
    print("Current points:", board.points)
main()
