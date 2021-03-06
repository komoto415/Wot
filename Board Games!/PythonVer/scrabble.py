from functools import reduce

class Scrabble:
    def __init__(self):
        self.startPos = '@'
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

    def placeTiles(self, x, y, tile):
        assert tile in self.tileSet.keys()
        assert 0 <= x < self.boardSize, "Not a valid x position on the board"
        assert 0 <= y < self.boardSize, "Not a valid y position on the board"
        assert self.board[y][x] == noLetterYet if self.points != 0 else self.board[y][x] == startPos

        board[y][x] = tile
        points = tileSet[tile];
        self.printPoints(points)

        getBoard()

    def placeTiles(self, x, y, direction, tiles):
        assert set(tiles).issubset(set(self.tileSet.keys())), "Not a list of valid tiles"
        assert direction in ['x+', 'x-', 'y+', 'y-'], "Not a valid direction"
        assert 0 <= x < self.boardSize, "Not a valid x position on the board"
        assert 0 <= y < self.boardSize, "Not a valid y position on the board"
        assert self.checkStepping(x,y,direction,tiles) if self.points == 0 else True, "First placement of tiles must step over the starting position"
        assert self.checkOffBoard(x, direction, len(tiles)) if 'x' in direction else True, "Cannot place off the board in the x direction"
        assert self.checkOffBoard(y, direction, len(tiles)) if 'y' in direction else True, "Cannot place off the board in the y direction"
        assert self.checkStepping(x,y,direction,tiles), "Cannot place a tile where there already is one"
        assert self.checkAdjacency(x,y,direction,tiles) if self.points != 0 else True, "Must place next to an exisiting tile"

        coor = self.adjust(x, y, direction, tiles)
        # Can this be made functional or using list comprehension?
        for letter,_ in enumerate(tiles):
            if 'x' in direction:
                self.board[y][coor+letter] = tiles[letter]
            elif 'y' in direction:
                self.board[coor+letter][x] = tiles[letter]

        points = reduce((lambda x,y: x+y), list(map(lambda x: self.tileSet[x], tiles)))
        self.printPoints(points)

        self.getBoard()

    def printPoints(self, points):
        self.points += points
        print("Points aquired from this placement", points)
        print("Current points:", self.points)

    def adjust(self, coor, len):
        return coor - len + 1

    def adjust(self, x, y, direction, tiles):
        return x if 'x' in direction else y if '-' not in list(direction) else self.adjust(x, len(tiles)) if 'x' in direction else self.adjust(y, len(tiles))

    def checkOffBoard(self, coor, direction, len):
        valid = True
        if '-' in direction:
            valid = adjust(coor, len) >= 0
        elif '+' in direction:
            valid = len + coor < self.boardSize
        return valid

    def checkStepping(self, x, y, direction, tiles):
        valid = True if self.points != 0 else False
        index = 0
        coor = self.adjust(x, y, direction, tiles)
        while index < len(tiles) and (valid if self.points != 0 else not valid):
            tile = self.board[y][coor+index] if 'x' in direction else self.board[coor+index][x]
            if self.points != 0:
                if tile != self.noLetterYet:
                    valid = False
            elif self.points == 0:
                if tile == self.startPos:
                    valid = True
            index += 1
        return valid

    def checkAdjacency(self, x, y, direction, tiles):
        valid = False
        adjacent = []
        index = 0
        coor = self.adjust(x, y, direction, tiles)
        while index < len(tiles):
            adj1 = self.board[y+1][coor+index] if 'x' in direction else self.board[coor+index][x+1]
            adj2 = self.board[y-1][coor+index] if 'x' in direction else self.board[coor+index][x-1]
            adjacent.append(adj1)
            adjacent.append(adj2)
            if index == 0:
                adj3 = self.board[y][coor+index-1] if 'x' in direction else self.board[coor+index-1][x]
                adjacent.append(adj3)
            elif index == len(tiles) - 1:
                adj4 = self.board[y][coor+index+1] if 'x' in direction else self.board[coor+index+1][x]
                adjacent.append(adj4)
            index += 1
        if len(set(adjacent)) > 1:
            valid = True
        return valid

    def getBoard(self):
        space = '  '
        print('Board Status:')
        for rows in range(self.boardSize):
            if rows == 0:
                print(space,space.join(list(map(str,(list(range(0,10)))))),space[0:1].join(list(map(str,(list(range(10,self.boardSize)))))))
            printThis = space[0:1] + str(rows) if rows < 10 else str(rows) + space[0:1]
            printThis += space.join(self.board[rows]) if rows > 9 else space[0:1] + space.join(self.board[rows])
            printThis += space[0:1] +str(rows)
            print(printThis)
            if rows == self.boardSize-1:
                print(space,space.join(list(map(str,(list(range(0,10)))))),space[0:1].join(list(map(str,(list(range(10,self.boardSize)))))))
        print()

def main():
    board = Scrabble()
    word1 = ['L','E','E','T']
    board.placeTiles(7,4,'y+',word1)
    board.placeTiles(3,6,'x+',word1)
    # Suppose to fail
    # board.placeTile(14,14,'y+',word1)

main()
