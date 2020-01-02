package boardGame;

public interface Scrabble {
    // After a tile placement, someone as just made a successful word
    // Update board
    public void placeTile(int x, int y, char tile);

    public void placeTiles(int x, int y, char direction, Character[] tiles);

    public void getBoard();
	
	public int getPoints();
}
