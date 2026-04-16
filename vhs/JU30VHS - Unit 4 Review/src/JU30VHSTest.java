
// Do not change these imports.
import static org.junit.Assert.assertEquals;

import org.junit.FixMethodOrder;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.Timeout;
import org.junit.runners.MethodSorters;

/**
 * Do not turn this particular file to the dropbox
 * grading system.
 * 
 * @version 6.0
 */

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class JU30VHSTest
{

  @Rule
  public Timeout globalTimeout = Timeout.seconds(4);

  @Test
  public void test01GetValueAt1()
  {
    LowMemory2DArray oceanGrid = new LowMemory2DArray(3, 3);
    oceanGrid.setValueAt(1, 2, 4);
    assertEquals("4", oceanGrid.getValueAt(1, 2) + "");
    assertEquals("0", oceanGrid.getValueAt(0, 0) + "");
  }

  @Test
  public void test01GetValueAt2()
  {
    LowMemory2DArray oceanGrid = new LowMemory2DArray(2, 4);
    oceanGrid.setValueAt(1, 0, 67);
    assertEquals("67", oceanGrid.getValueAt(1, 0) + "");
    assertEquals("0", oceanGrid.getValueAt(1, 3) + "");
  }

  @Test
  public void test01GetValueAt3()
  {
    LowMemory2DArray oceanGrid = new LowMemory2DArray(5, 2);
    oceanGrid.setValueAt(4, 1, 42);
    assertEquals("42", oceanGrid.getValueAt(4, 1) + "");
    assertEquals("0", oceanGrid.getValueAt(3, 0) + "");
  }

  @Test
  public void test01GetValueAt4()
  {
    LowMemory2DArray oceanGrid = new LowMemory2DArray(5, 2);
    oceanGrid.setValueAt(4, 1, 42);
    oceanGrid.setValueAt(0, 0, 67);

    // @formatter:off
    assertEquals(
            "    0  1\n"
          + "    -  -\n"
          + "0| 67  0\n"
          + "1|  0  0\n"
          + "2|  0  0\n"
          + "3|  0  0\n"
          + "4|  0 42\n"
          + "", oceanGrid.toString());
    // @formatter:on
  }

  @Test
  public void test01GetValueAt5()
  {
    LowMemory2DArray oceanGrid = new LowMemory2DArray(6, 5);
    oceanGrid.setValueAt(1, 4, 4);
    oceanGrid.setValueAt(2, 0, 1);
    oceanGrid.setValueAt(3, 1, -9);
    oceanGrid.setValueAt(1, 1, 5);

    // @formatter:off
    assertEquals(
          "    0  1  2  3  4\n"
        + "    -  -  -  -  -\n"
        + "0|  0  0  0  0  0\n"
        + "1|  0  5  0  0  4\n"
        + "2|  1  0  0  0  0\n"
        + "3|  0 -9  0  0  0\n"
        + "4|  0  0  0  0  0\n"
        + "5|  0  0  0  0  0\n"
        + "", oceanGrid.toString());
    // @formatter:on
  }

  @Test
  public void test02DeleteGridColumn1()
  {
    LowMemory2DArray oceanGrid = new LowMemory2DArray(2, 6);
    oceanGrid.setValueAt(1, 4, -7);
    oceanGrid.setValueAt(0, 5, -6);
    // @formatter:off
    assertEquals(
              "    0  1  2  3  4  5\n"
            + "    -  -  -  -  -  -\n"
            + "0|  0  0  0  0  0 -6\n"
            + "1|  0  0  0  0 -7  0\n"
            + "", oceanGrid.toString());
    // @formatter:on
    oceanGrid.deleteGridColumnAt(0);

    // @formatter:off
    assertEquals(
            "    0  1  2  3  4\n"
          + "    -  -  -  -  -\n"
          + "0|  0  0  0  0 -6\n"
          + "1|  0  0  0 -7  0\n"
          + "", oceanGrid.toString());
    // @formatter:on
  }

  @Test
  public void test02DeleteGridColumn2()
  {
    LowMemory2DArray oceanGrid = new LowMemory2DArray(2, 6);
    oceanGrid.setValueAt(1, 4, -7);
    oceanGrid.setValueAt(0, 5, -6);
    // @formatter:off
    assertEquals(
              "    0  1  2  3  4  5\n"
            + "    -  -  -  -  -  -\n"
            + "0|  0  0  0  0  0 -6\n"
            + "1|  0  0  0  0 -7  0\n"
            + "", oceanGrid.toString());
    // @formatter:on
    oceanGrid.deleteGridColumnAt(4);

    // @formatter:off
    assertEquals(
              "    0  1  2  3  4\n"
            + "    -  -  -  -  -\n"
            + "0|  0  0  0  0 -6\n"
            + "1|  0  0  0  0  0\n"
            + "", oceanGrid.toString());
    // @formatter:on
  }

  @Test
  public void test02DeleteGridColumn3()
  {
    LowMemory2DArray oceanGrid = new LowMemory2DArray(5, 4);
    oceanGrid.setValueAt(4, 3, -7);
    oceanGrid.setValueAt(1, 0, -6);
    oceanGrid.setValueAt(3, 1, 13);
    // @formatter:off
    assertEquals(
                "    0  1  2  3\n"
              + "    -  -  -  -\n"
              + "0|  0  0  0  0\n"
              + "1| -6  0  0  0\n"
              + "2|  0  0  0  0\n"
              + "3|  0 13  0  0\n"
              + "4|  0  0  0 -7\n"
              + "", oceanGrid.toString());
    // @formatter:on
    oceanGrid.deleteGridColumnAt(2);

    // @formatter:off
    assertEquals(
                  "    0  1  2\n"
                + "    -  -  -\n"
                + "0|  0  0  0\n"
                + "1| -6  0  0\n"
                + "2|  0  0  0\n"
                + "3|  0 13  0\n"
                + "4|  0  0 -7\n"
                + "", oceanGrid.toString());
    // @formatter:on
  }

  @Test
  public void test02DeleteGridColumn4()
  {
    LowMemory2DArray oceanGrid = new LowMemory2DArray(6, 7);
    oceanGrid.setValueAt(0, 2, -7);
    oceanGrid.setValueAt(1, 4, -6);
    oceanGrid.setValueAt(3, 0, 13);
    oceanGrid.setValueAt(4, 0, -8);
    oceanGrid.setValueAt(1, 6, -2);
    oceanGrid.setValueAt(5, 5, 11);
    // @formatter:off
    assertEquals(
                    "    0  1  2  3  4  5  6\n"
                  + "    -  -  -  -  -  -  -\n"
                  + "0|  0  0 -7  0  0  0  0\n"
                  + "1|  0  0  0  0 -6  0 -2\n"
                  + "2|  0  0  0  0  0  0  0\n"
                  + "3| 13  0  0  0  0  0  0\n"
                  + "4| -8  0  0  0  0  0  0\n"
                  + "5|  0  0  0  0  0 11  0\n"
                  + "", oceanGrid.toString());
    // @formatter:on
    oceanGrid.deleteGridColumnAt(2);

    // @formatter:off
    assertEquals(
                    "    0  1  2  3  4  5\n"
                  + "    -  -  -  -  -  -\n"
                  + "0|  0  0  0  0  0  0\n"
                  + "1|  0  0  0 -6  0 -2\n"
                  + "2|  0  0  0  0  0  0\n"
                  + "3| 13  0  0  0  0  0\n"
                  + "4| -8  0  0  0  0  0\n"
                  + "5|  0  0  0  0 11  0\n"
                  + "", oceanGrid.toString());
    // @formatter:on
  }

  @Test
  public void test02DeleteGridColumn5()
  {
    LowMemory2DArray oceanGrid = new LowMemory2DArray(6, 5);
    oceanGrid.setValueAt(1, 4, 4);
    oceanGrid.setValueAt(2, 0, 1);
    oceanGrid.setValueAt(3, 1, -9);
    oceanGrid.setValueAt(1, 1, 5);
    oceanGrid.deleteGridColumnAt(1);

    // @formatter:off
    assertEquals(
            "    0  1  2  3\n"
          + "    -  -  -  -\n"
          + "0|  0  0  0  0\n"
          + "1|  0  0  0  4\n"
          + "2|  1  0  0  0\n"
          + "3|  0  0  0  0\n"
          + "4|  0  0  0  0\n"
          + "5|  0  0  0  0\n"
          + "", oceanGrid.toString());
    // @formatter:on

    oceanGrid.deleteGridColumnAt(2);
    oceanGrid.deleteGridColumnAt(2);

    // @formatter:off
    assertEquals(
              "    0  1\n"
            + "    -  -\n"
            + "0|  0  0\n"
            + "1|  0  0\n"
            + "2|  1  0\n"
            + "3|  0  0\n"
            + "4|  0  0\n"
            + "5|  0  0\n"
            + "", oceanGrid.toString());
    // @formatter:on
  }

}