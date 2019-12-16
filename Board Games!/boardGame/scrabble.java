package boardGame;

public interface scrabble {
    // After a tile placement, someone as just made a successful word
    public void wordMade();
    // Update board
    public void placeTile(int x, int y, char tile);
}
