import java.util.ArrayList;

/**
 * @author: Your First and Last name goes here!
 *          VHS Learning
 *          Submit this file to the Dropbox.
 */

public class LowMemory2DArray
{
  private int numRows;
  private int numCols;

  private ArrayList<GridPoint> entries;

  public LowMemory2DArray(int maxRows, int maxCols)
  {
    entries = new ArrayList<>();
    numRows = maxRows;
    numCols = maxCols;
  }

  public int getNumRows()
  {
    return numRows;
  }

  public int getNumCols()
  {
    return numCols;
  }

  public int getValueAt(int row, int col)
  {
    if (row >= numRows)
    {
      throw new ArrayIndexOutOfBoundsException(row);
    }
    if (col >= numCols)
    {
      throw new ArrayIndexOutOfBoundsException(col);
    }

    for (GridPoint entry : entries)
    {
      if (entry.getRow() == row && entry.getCol() == col)
      {
        return entry.getValue();
      }
    }
    return 0;
  }

  public void deleteGridColumnAt(int col)
  {
    if (col >= numCols)
    {
      throw new ArrayIndexOutOfBoundsException(col);
    }

    ArrayList<GridPoint> updated = new ArrayList<>();

    for (GridPoint entry : entries)
    {
      int entryRow = entry.getRow();
      int entryCol = entry.getCol();
      int entryValue = entry.getValue();

      if (entryCol == col)
      {
        continue;
      }
      if (entryCol > col)
      {
        updated.add(new GridPoint(entryRow, entryCol - 1, entryValue));
      }
      else
      {
        updated.add(entry);
      }
    }

    entries = updated;
    numCols--;
  }

  public void setValueAt(int aRow, int aColumn, int value)
  {
    if (aRow >= numRows)
    {
      throw new ArrayIndexOutOfBoundsException(aRow);
    }
    if (aColumn >= numCols)
    {
      throw new ArrayIndexOutOfBoundsException(aColumn);
    }
    GridPoint item = new GridPoint(aRow, aColumn, value);
    entries.add(item);
  }

  public String toString()
  {
    String response = "  ";

    for (int c = 0; c < this.getNumCols(); c++)
    {
      response += String.format("%3d", c);
    }
    response += "\n  ";

    for (int c = 0; c < this.getNumCols(); c++)
    {
      response += String.format("%3s", "-");
    }
    response += "\n";

    for (int r = 0; r < this.getNumRows(); r++)
    {
      response += r + "|";
      for (int c = 0; c < this.getNumCols(); c++)
      {
        response += String.format("%3d", getValueAt(r, c));
      }
      response += "\n";
    }
    return response;
  }
}