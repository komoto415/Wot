class Scrabble:
    def __init__(self):
        noLetterYet = ' '
        self.boardSize = 10
        self.board = [[noLetterYet for i in range(self.boardSize)] for j in range(self.boardSize)]
        # Where (0,0) is the top left and (self.boardSize-1, self.boardSize-1) is the bottom right
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

    def placeTile(self, x, y, tile):
        assert tile in self.tileSet.keys()
        assert 0 <= x < self.boardSize, "Not a valid x position on the board"
        assert 0 <= y < self.boardSize, "Not a valid y position on the board"
        assert self.board[y][x] == ' ', "Can't place a tile here!"

        self.board[y][x] = tile
        print('Tile ' + tile + ' has been added to the board!')
        # self.hasWordBeenMade()

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

def main():
    board = Scrabble()
    b = board.board

    print()
    board.placeTile(1,0,'B')
    board.placeTile(1,2,'L')

    print()
    for rows in b:
        print(rows)

    print()
    print(board.hasWordBeenMade())
main()
