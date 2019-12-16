class Scrabble:
    def __init__(self):
        noLetterYet = ' '
        self.boardSize = 10
        self.board = [[noLetterYet for i in range(self.boardSize)] for j in range(self.boardSize)]
        # Where (0,0) starts at the top left and and (4,4) is the bottom right
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
        for i in range(self.boardSize):
            wordListR.append(''.join(self.board[i]))
            wordListC.append(''.join(row[i] for row in self.board))
        print('Words by row:', wordListR)
        print('Words by coloum:', wordListC)
        wordList = wordListR + wordListC
        print('Combined words found: ')
        for word in range(len(wordList)):
            print('[' + wordList[word] + ']')
            if (word == len(wordList)/2-1):
                print()

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
