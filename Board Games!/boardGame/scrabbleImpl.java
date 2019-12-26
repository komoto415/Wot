package boardGame;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class ScrabbleImpl implements Scrabble {
	private static int boardSize = 15;
	private static char[][] board = new char[boardSize][boardSize];
	private static HashMap<Character, Integer> alphabetConversion = new HashMap<>();
	private static int points = 0;

	private final char EMPTY_SPACE = '-';
	private final List<Character> LETTERS_LIST = new ArrayList<>(Arrays.asList(
			'O','L','Z','E','A','S','G','T','B','P')
			);

	// Where (0,0) is the top left and (14,14) is the bottom right
	// board[COLOUMNS][ROWS] unfortunately no way around this. I think
	// Positive x and y are right and down
	// The matrix will be indexed by 0
	
	/*
        Precondition(s):
                            None
        Postcondition(s):
                            Instantiate a scrabble game C:
	 */
	private final char STARTING_POSITION = 'X';
	public ScrabbleImpl() {
		for (int i = 0; i < boardSize; i++) {
			for (int j = 0; j < boardSize; j++) {
				board[i][j] = EMPTY_SPACE;
				// Replace magic number with constant
				if (i == 7 && j == 7) {
					board[i][j] = STARTING_POSITION;
				}
			}
		}
		
		for (int i = 0; i < LETTERS_LIST.size(); i++){
			alphabetConversion.put(LETTERS_LIST.get(i), i);
		}
	}

	// This implies you can only place one letter at a time, should you be able to place multiple sequential letters?
	public void placeTile(int x, int y, char tile) {
		assert LETTERS_LIST.contains(tile);
		assert 0 <= x && x < board.length-1;
		assert 0 <= y && y < board.length-1;
		assert points != 0 ? board[y][x] == EMPTY_SPACE : board[y][x] == STARTING_POSITION;
		assert points != 0 ? checkAdjacency(x,y) : true;

		board[y][x] = tile;

		int pointsGained = alphabetConversion.get(tile);
		
		printPoints(pointsGained);
		getBoard();
	}

	private final char X_DIRECTION = 'x';
	private final char Y_DIRECTION = 'y';
	// For this, direction expecting positive direction
	public void placeTiles(int x, int y, char direction, char[] tiles) {
		assert isValidTileList(tiles);
		assert direction == X_DIRECTION || direction == Y_DIRECTION;
		assert 0 <= x && x < board.length-1;
		assert 0 <= y && y < board.length-1;
		assert points == 0 ? checkSteps(x, y, direction, tiles) : true;
		assert direction == X_DIRECTION ? x + tiles.length < board.length : true;
		assert direction == Y_DIRECTION ? y + tiles.length < board.length : true;
		assert checkSteps(x, y, direction, tiles);
		assert points != 0 ? checkAdjacency(x, y, direction, tiles.length) : true;

		for (int i = 0; i < tiles.length; i++) {
			if (direction == X_DIRECTION) {
				board[y][x+i] = tiles[i];
			}
			else if (direction == Y_DIRECTION) {
				board[y+i][x] = tiles[i];
			}
		}
		
		int pointsGained = 0;
		for (char curVal : tiles) {
			pointsGained += alphabetConversion.get(curVal);
		}
		
		printPoints(pointsGained);
		getBoard();
	}

	private boolean checkAdjacency(int x, int y) {
		boolean valid = false;
		Set<Character> adjacentSpaces = new HashSet<>();
		adjacentSpaces.addAll(new ArrayList<>(Arrays.asList(
				board[y][x+1], board[y][x-1], board[y+1][x], board[y-1][x])));
		if (adjacentSpaces.size() > 1) {
			valid = true;
		}
		return valid;
	}
	
	private boolean checkAdjacency(int x, int y, char direction, int tilesLength) {
		boolean valid = false;
		char adj1Body = EMPTY_SPACE;
		char adj2Body = EMPTY_SPACE;
		char adjHead = EMPTY_SPACE;
		char adjTail = EMPTY_SPACE;

		Set<Character> adjacentSpaces = new HashSet<>();
		int index = 0;
		while (index < tilesLength) {
			adj1Body = direction == X_DIRECTION ? board[y+1][x+index] : board[y+index][x+1];
			adj2Body = direction == X_DIRECTION ? board[y-1][x+index] : board[y+index][x-1];
			if (index == 0) {
				adjHead = direction == X_DIRECTION ? board[y][x+index-1] : board[y+index-1][x];
			}
			else if (index == tilesLength - 1) {
				adjTail = direction == X_DIRECTION ? board[y][x+index+1] : board[y+index+1][x];
			}
			index++;
		}
		adjacentSpaces.addAll(new ArrayList<>(Arrays.asList(
				adj1Body, adj2Body, adjHead, adjTail)));
		if (adjacentSpaces.size() > 1) {
			valid = true;
		}
		return valid;
	}
	
	private boolean checkSteps(int x, int y, char direction, char[] tiles) {
		boolean valid = points != 0 ? true : false;
		int index = 0;
		while (index < tiles.length && (points != 0 ? valid : !valid)) {
			char tile = direction == X_DIRECTION ? board[y][x+index] : board[y+index][x];
			if (points != 0) {
				if (tile != EMPTY_SPACE) {
					valid = false;
				}
			}
			else if (points == 0) {
				if (tile == STARTING_POSITION) {
					valid = true;
				}
			}
			index++;
		}
		return valid;
	}
	
	private void printPoints(int pointsGained) {
		points += pointsGained;
		System.out.printf("Points gained from this placement: %d\n", pointsGained);
		System.out.printf("Total Points: %d\n", points);
	}

	private boolean isValidTileList(char[] tiles) {
		Set<Character> incomingAsSet = new HashSet<Character>();
		for (Character curVal : tiles) {
			incomingAsSet.add(curVal);
		}
		Set<Character> lettersAsSet = new HashSet<>();
		lettersAsSet.addAll(LETTERS_LIST);

		return lettersAsSet.containsAll(incomingAsSet);
	}

	public int getPoints() {
		return points;
	}

	public void getBoard() {
		System.out.println("   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14");
		for (int i = 0; i < boardSize; i++) {
			String rowNum = i + " ";
			System.out.print(i > 9  ? rowNum : " " + rowNum);
			for (int j = 0; j < boardSize; j++) {
				if (j != 0) {
					System.out.print(" "); 
				}
				System.out.print(board[i][j]);
				System.out.print(" ");
			}
			System.out.println();
		}
	}

	public static void main(String[]args) {
		Scrabble test = new ScrabbleImpl();
		test.placeTiles(5, 7, 'x', new char[] {'A', 'B', 'B'});
		test.placeTiles(7, 4, 'y', new char[] {'A', 'B', 'B'});
	}
}
