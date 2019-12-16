package boardGame;

import java.util.HashMap;

class scrabbleImpl implements scrabble {
    private static char[][] board = new char[10][10];
    private static String[] dictionary;
    private static HashMap<Character, Integer> alphabetConversion = new HashMap<>();

    private final char noLetterYet = ' ';
    private final List<Character> letters = new ArrayList<>(Arrays.asList(
            'O','L','Z','E','A','S','G','T','B','P')
        );

    public scrabbleImpl() {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                board[i][j] = noLetterYet;
            }
        }
        for (int i = 0; i < letters.size(); i++){
            alphabetConversion.put(letters.get(i), i);
        }
        // alphabetConversion.put('O', 0); alphabetConversion.put('L', 1);
        // alphabetConversion.put('Z', 2); alphabetConversion.put('E', 3);
        // alphabetConversion.put('A', 4); alphabetConversion.put('S', 5);
        // alphabetConversion.put('G', 6); alphabetConversion.put('T', 7);
        // alphabetConversion.put('B', 8); alphabetConversion.put('P', 9);
    }

    public void placeTile(int x, int y, char tile) {
        assert letters.contains(tile);
        assert 0 <= x || x < board.length-1;
        assert 0 <= y || y < board.length-1;
        assert board[y][x] == ' ';

        board[i][j] = tile;

    }
}
