
/**
 * This is a review of all kinds of concepts.
 * 
 * @author YOURNAME
 */

public class JU31VHS
{

  # 1. Write a method that takes an array of ints and returns a new array where every 4 is followed by a 5. You may assume that every 4 in the original array is followed by a number that is not a 4, and that the array contains the same number of 4s and 5s.
  public static int[] putFivesAfterFours(int[] nums)
  {
    int[] result = new int[nums.length];
    System.arraycopy(nums, 0, result, 0, nums.length);

    for (int i = 0; i < result.length - 1; i++)
    {
      if (result[i] == 4 && result[i + 1] != 5)
      {
        for (int j = i + 1; j < result.length; j++)
        {
          if (result[j] == 5 && (j == 0 || result[j - 1] != 4))
          {
            int temp = result[i + 1];
            result[i + 1] = result[j];
            result[j] = temp;
            break;
          }
        }
      }
    }
    return result;
  }


  public static String centralThree(String letters)
  {
    int len = letters.length();
    if (len <= 3) return letters;
    int start = (len - 3) / 2;
    return letters.substring(start, start + 3);
  }

  public static String chopFront(String str)
  {
    StringBuilder sb = new StringBuilder();
    for (char c : str.toCharArray())
    {
      if ("ablovrxyz".indexOf(c) != -1)
      {
        sb.append(c);
      }
    }
    String kept = sb.toString();
    StringBuilder sb2 = new StringBuilder();
    for (char c : kept.toCharArray())
    {
      sb2.append(c);
      if (c == 'a' && str.contains("w"))
      {
        sb2.append('a');
      }
    }
    kept = sb2.toString();
    int countA = 0;
    for (char c : kept.toCharArray())
    {
      if (c == 'a') countA++;
    }
    if (countA > 1)
    {
      kept = kept.replaceFirst("a", "");
    }
    return kept;
  }

  public static String hateX(String str)
  {
    return str.replace("x", "");
  }

  public static void swapRows(int[][] mat, int rowAIndex, int rowBIndex)
  {
    int[] temp = mat[rowAIndex];
    mat[rowAIndex] = mat[rowBIndex];
    mat[rowBIndex] = temp;
  }

  public static void swapColumns(int[][] mat, int colAIndex, int colBIndex)
  {
    for (int i = 0; i < mat.length; i++)
    {
      int temp = mat[i][colAIndex];
      mat[i][colAIndex] = mat[i][colBIndex];
      mat[i][colBIndex] = temp;
    }
  }

  public static String[][] fill2DWithLetters(String str, int rows, int cols)
  {
    String[][] mat = new String[rows][cols];
    int index = 0;
    for (int i = 0; i < rows; i++)
    {
      for (int j = 0; j < cols; j++)
      {
        if (index < str.length())
        {
          mat[i][j] = str.substring(index, index + 1);
          index++;
        }
        else
        {
          mat[i][j] = null;
        }
      }
    }
    return mat;
  }

  public static int[][] fillDownAndUp(int[] vals, int rows, int cols)
  {
    int[][] mat = new int[rows][cols];
    int index = 0;
    for (int c = 0; c < cols; c++)
    {
      if (c % 2 == 0)
      {
        // down
        for (int r = 0; r < rows; r++)
        {
          mat[r][c] = vals[index++];
        }
      }
      else
      {
        // up
        for (int r = rows - 1; r >= 0; r--)
        {
          mat[r][c] = vals[index++];
        }
      }
    }
    return mat;
  }

  public static int[][] crop2D(int[][] mat, int startRow, int startCol,
                               int endRow, int endCol)
  {
    int newRows = endRow - startRow;
    int newCols = endCol - startCol;
    int[][] newMat = new int[newRows][newCols];
    for (int i = 0; i < newRows; i++)
    {
      for (int j = 0; j < newCols; j++)
      {
        newMat[i][j] = mat[startRow + i][startCol + j];
      }
    }
    return newMat;
  }

}