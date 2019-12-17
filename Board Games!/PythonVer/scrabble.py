from functools import reduce

class Scrabble:
    def __init__(self):
        self.startPos = 'X'
        self.noLetterYet = '-'
        self.points = 0
        self.boardSize = 15
        self.board = [[self.noLetterYet for i in range(self.boardSize)] for j in range(self.boardSize)]
        # Where (0,0) is the top left and (14,14) is the bottom right
        # board[COLOUMNS][ROWS] unfortunately no way around this. I think
        # Positive x and y are right and down
        # The matrix will be indexed by 0
        self.board[7][7] = self.startPos
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

    # IDEA:
    #   Should you be able to place in the negative direction?
    #   If yes, then place in reversed order or shift starting coordinate and place in standing order
    #   BUT IT MAKES THINGS SO STUPIDLY AND UNNECESSARILY COMPLICATED. So many extra freaking checks just for direction
    #   eg: placeTile(0, 3, x-, [L,O,S])
    #       case 1:
    #           -  S  O  L  -  -
    #           -  -  -  -  -  -
    #           -  -  -  -  -  -
    #           -  -  -  -  -  -
    #       case 2:
    #           -  L  O  S  -  -
    #           -  -  -  -  -  -
    #           -  -  -  -  -  -
    #           -  -  -  -  -  -

    # Need to check if the tiles placed is at some point to adjacent to an already placed tile
    def placeTile(self, x, y, direction, tiles):
        assert set(tiles).issubset(set(self.tileSet.keys())), "Not a list of valid tiles"
        assert direction in ['x+', 'x-', 'y+', 'y-'], "Not a valid direction"
        assert 0 <= x < self.boardSize, "Not a valid x position on the board"
        assert 0 <= y < self.boardSize, "Not a valid y position on the board"
        assert self.checkStepping(x,y,direction,tiles, 0) == "Start" if self.points == 0 else True, "First placement of tiles must step over the starting position"
        assert self.checkOffBoard(x, direction, len(tiles)) if 'x' in direction else True, "Cannot place off the board in the x direction"
        assert self.checkOffBoard(y, direction, len(tiles)) if 'y' in direction else True, "Cannot place off the board in the y direction"
        assert self.checkStepping(x,y,direction,tiles, self.points) != "Exists", "Cannot place a tile where there already is one"

        # Is there a way to insert directly with a range
        coor = x if 'x' in direction else y
        if '-' in list(direction):
            coor = self.adjust(x, len(tiles)) if 'x' in direction else self.adjust(y, len(tiles))
        # Can this be made functional?
        for letter,_ in enumerate(tiles):
            if 'x' in direction:
                self.board[y][coor+letter] = tiles[letter]
            elif 'y' in direction:
                self.board[coor+letter][x] = tiles[letter]

        points = reduce((lambda x,y: x+y), list(map(lambda x: self.tileSet[x], tiles)))
        self.points += points

        self.getBoard()
        print("Points aquired from this placement", points)
        print("Current points:", self.points,'\n')

    def adjust(self, coor, len):
        return coor - len + 1

    def checkOffBoard(self, coor, direction, len):
        valid = True
        if '-' in direction:
            valid = coor - len >= 0
        elif '+' in direction:
            valid = len + coor < self.boardSize
        return valid

    def checkStepping(self, x, y, direction, tiles, points):
        valid = True if points != 0 else False
        index = 0
        coor = x if 'x' in direction else y
        if '-' in list(direction):
            coor = self.adjust(x, len(tiles)) if 'x' in direction else self.adjust(y, len(tiles))
        while index < len(tiles) and (valid if points != 0 else not valid):
            tile = self.board[y][coor+index] if 'x' in direction else self.board[coor+index][x]
            if points != 0:
                if tile != self.noLetterYet:
                    valid = "Exists"
            elif points == 0:
                if tile == self.startPos:
                    valid = "Start"
            index += 1
        return valid

    def checkAdjacency(self, x, y, direction, tiles):
        print()
        
    def getBoard(self):
        s = '  '
        for rows in range(self.boardSize):
            if rows == 0:
                print(s,s.join(list(map(str,(list(range(0,10)))))),s[0:1].join(list(map(str,(list(range(10,self.boardSize)))))))
            printThis = s[0:1] + str(rows) if rows < 10 else str(rows) + s[0:1]
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
    board.placeTile(7,4,'y+',word1)
    # board.placeTile(6,7,'x-',word1)

    board.placeTile(11,6,'x-',word1)

    # Suppose to fail
    # board.placeTile(14,14,'y+',word1)

main()
