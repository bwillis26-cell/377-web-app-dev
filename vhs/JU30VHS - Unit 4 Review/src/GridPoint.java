/**
 * Do not submit this file to the dropbox.
 * It's used to simulate a single element in a 2D array.
 */

public class GridPoint
{
  /** The row index and column index for this entry in the sparse array */
  private int row;
  private int col;
  private int value;

  /**
   * Constructs a GridPoint object that represents a sparse array
   * element
   * with row index r and column index c, containing value v.
   */
  public GridPoint(int r, int c, int v)
  {
    row = r;
    col = c;
    value = v;
  }

  /** Returns the row index of this GridPoint element. */
  public int getRow()
  {
    return row;
  }

  /** Returns the column index of this GridPoint element. */
  public int getCol()
  {
    return col;
  }

  /** Returns the value of this GridPoint element. */
  public int getValue()
  {
    return value;

  }

  public String toString()
  {
    return "" + this.getRow() + this.getCol() + this.getValue();
  }
}
