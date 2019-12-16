package boardGame;

import java.util.HashMap;

class scrabbleImpl implements scrabble {
    private static char[][] board = new char[10][10];
    private static String[] dictionary;
    private static HashMap<Character, Integer> alphabetConversion = new HashMap<>();
    /*
        Tile value (1337 alphabet)
            O --> 0
            L --> 1
            Z --> 2
            E --> 3
            A --> 4
            S --> 5
            G --> 6
            T --> 7
            B --> 8
            P --> 9
    */
    private final char placeholder = ' ';
    public scrabbleImpl() {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                board[i][j] = placeholder;
            }
        }
        alphabetConversion.put('O', 0); alphabetConversion.put('L', 1);
        alphabetConversion.put('Z', 2); alphabetConversion.put('E', 3);
        alphabetConversion.put('A', 4); alphabetConversion.put('S', 5);
        alphabetConversion.put('G', 6); alphabetConversion.put('T', 7);
        alphabetConversion.put('B', 8); alphabetConversion.put('P', 9);
    }

    public void wordMade() {
        
    }

    public void placeTile(int x, int y, char tile) {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (x == j && y == i) {
                    board[i][j] = tile;
                }
            }
        }
    }

    public static String getBoard() {
        StringBuilder rv = new StringBuilder();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                rv.append('['+board[i][j]+']');
            }
            rv.append('\n');
        }
        return rv.toString();
    }
}
