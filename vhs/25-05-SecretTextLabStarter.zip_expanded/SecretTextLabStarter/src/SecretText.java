
/**
 * You will eventually complete all of these methods after you finish all
 * four activities in the labs.
 * 
 * @author: VHS
 * @version 1.1
 */

import java.awt.Color;
import java.util.ArrayList;

import picturelib.*;

public class SecretText
{

  public static void main(String[] args)
  {
    /**
     * You'll be constantly editing the main method through all of the problems
     * and activities. You can also open SecretTextTest.java and press play
     * on it to verify that your methods are working correctly.
     */

    Picture beach = new Picture("beach.png");
    beach.explore(); // explore is a method that just shows the image.
    Pixel[][] pixels = beach.getPixels2D();
    Pixel aPixel = pixels[5][10];
    System.out.println(aPixel.toString());
    aPixel.setRed(200);
    aPixel.setBlue(255);
    beach.explore();

    /**
     * Once you get testSetLow working, you can uncomment the code below and
     * press PLAY. Visually, you won't see much after clearLow runs on an image.
     * It just zeros out the last two bits of each 8bit red, green, and blue
     * value. However, you should examine the same pixel from each picture and
     * see that the pixel is a tad slightly different.
     */

    // Picture copy = testClearLow(beach);
    // copy.explore();

    // Test hideText and revealText
    String secretMessage = "HELLO WORLD";
    Picture hiddenPic = hideText(beach, secretMessage);
    hiddenPic.explore(); // Should look almost the same as beach
    String revealedMessage = revealText(hiddenPic);
    System.out.println("Original message: " + secretMessage);
    System.out.println("Revealed message: " + revealedMessage);

  }

  /**
   * Clear the lower (rightmost) two bits in a pixel.
   */
  public static void clearLow(Pixel aSinglePixel)
  {
    aSinglePixel.setRed(aSinglePixel.getRed() / 4 * 4);
    aSinglePixel.setBlue(aSinglePixel.getBlue() / 4 * 4);
    aSinglePixel.setGreen(aSinglePixel.getGreen() / 4 * 4);

    // TODO: Activity 1 Question 7
    /**
     * @formatter:off
     * HINTS:
     * Extract the red, green, and blue integer values from aSinglePixel. 
     * Divide each color value by 4 using integer division, and then
     * multiply the result by 4. 
     * Set the pixel’s color to the new color represented by these updated values.
     * @formatter:on
     */
    /* watch the video in the lesson on how to do this */
  }

  /**
   * Method to test clearLow on all pixels in a Picture
   * 
   * @params pic - not null
   * @return a new picture with the lowest two bits zeroed out on every pixel.
   */
  public static Picture testClearLow(Picture pic)
  {
    // Activity 1 Question 8
    /**
     * Hints: Clone the picture into a new picture variable clonePic. (We don't
     * want to mutate the pic parameter.)
     * 
     * Get the 2D array of pixels from clonePic. Nested loop through all of the
     * pixels and invoke clearLow method on each. Finally return the clonedPic
     */
    Picture copyOfPic = new Picture(pic);
    // Gets all of the pixels of the image. They are mutable as well.
    Pixel[][] pixels = copyOfPic.getPixels2D();
    // TODO: code here
    for (int row = 0; row < pixels.length; row++)
    {
      for (int col = 0; col < pixels[0].length; col++)
      {
        clearLow(pixels[row][col]);
      }
    }

    return copyOfPic;
  }

  /**
   * Set the lower 2 bits in a pixel to the highest 2 bits in anRGBColor.
   * This probably the most important method in this lab. You will
   * be constantly sending one color of the secret picture, and it will
   * mutate aSinglePixel to hide that color in the least significant bits.
   */
  public static void setLow(Pixel aSinglePixel, Color anRGBColor)
  {

    // TODO: For Activity 1 Question 11
    /**
     * HINT: You are actually mutating the parameter p - you'll use setColor on
     * it. Divide c RGB by 64, then add those to the RGB of p's color RGBs,
     * create a new color with that, and then set p's color to that.
     */
    clearLow(aSinglePixel); // leave this here, it zero's out the last two bits
    // of the color
    // TODO: Complete the code here.
    int red = anRGBColor.getRed();
    int green = anRGBColor.getGreen();
    int blue = anRGBColor.getBlue();

    int highRed = red / 64;
    int highGreen = green / 64;
    int highBlue = blue / 64;

    aSinglePixel.setRed(aSinglePixel.getRed() + highRed);
    aSinglePixel.setGreen(aSinglePixel.getGreen() + highGreen);
    aSinglePixel.setBlue(aSinglePixel.getBlue() + highBlue);

  }

  /**
   * Method to test setLow on all pixels in a Picture
   */
  public static Picture testSetLow(Picture originalPNG, Color anRGBColor)
  {
    /**
     * Activity 1 Question 12 Hints: Very similar to testClearLow. You are
     * basically taking the most significant bits of the color and setting them
     * to the least significant bits of the RGB. It's basically hiding a single
     * color image in pic. Make sure you clone pic, setLow on all of it's
     * pixels, then return the cloned pic.
     */

    // This command clones the original picture, so we don't mutate the
    // original.
    Picture clonePNG = new Picture(originalPNG);
    // TODO: Complete the code here.
    Pixel[][] pixels = clonePNG.getPixels2D();
    for (int row = 0; row < pixels.length; row++)
    {
      for (int col = 0; col < pixels[0].length; col++)
      {
        setLow(pixels[row][col], anRGBColor);
      }
    }

    return clonePNG;
  }

  /**
   * Sets the highest two bits of each pixel’s colors * to the lowest two bits
   * of each pixel’s colors. This will send the secret picture back that was
   * hidden in the picture named "hidden".
   */
  public static Picture revealPicture(Picture hidden)
  {
    /**
     * Activity 1 Question 14
     */
    Picture copy = new Picture(hidden);
    Pixel[][] pixels = copy.getPixels2D();
    Pixel[][] source = hidden.getPixels2D();
    for (int r = 0; r < pixels.length; r++)
    {
      for (int c = 0; c < pixels[0].length; c++)
      {
        Color col = source[r][c].getColor();
        int rightDigRed = col.getRed() % 4;
        int rightDigGreen = col.getGreen() % 4;
        int rightDigBlue = col.getBlue() % 4;

        pixels[r][c].setRed(rightDigRed * 64);
        pixels[r][c].setGreen(rightDigGreen * 64);
        pixels[r][c].setBlue(rightDigBlue * 64);
        /* TODO: To be Implemented Activity 1: Question 14 */
        /**
         * @formatter:off
         * HINTS:
         * To isolate the rightmost 2 values, instead of dividing by 4 like before 
         * when clearing the bits, we want to use % (modulus) to preserve 
         * only the rightmost two bits.
         * Finally, this value needs to be multiplied by 64 to move 
         * the bits into the appropriate, leftmost position.
         * 
         * Get the pixel from the copy.
         * Then set it's red to color MOD 4 times 64. 
         * Do the same for green and blue
         * @formatter:on
         */

        // TODO: Complete the code here.
      }
    }
    return copy;
  }

  /**
   * Determines whether secret can be hidden in source, which is true if (FOR
   * ACTIVITY 2 QUESTION 8) source and secret are the same dimensions, OR (FOR
   * ACTIVITY 3 QUESTION 1) both the width and height are smaller than source.
   * 
   * @param source
   *          is not null
   * @param secret
   *          is not null
   * 
   * @return true if secret can be hidden in source, false otherwise. * true if
   *         source and secret are the same (OR less) dimensions.
   */
  public static boolean canHide(Picture source, Picture secret)
  {
    // TODO: Activity 2 Question 8
    // TODO: Will also be modified in Activity 3 Question 1

    // uncomment if you want to debug.
    int sourceW = source.getWidth();
    int sourceH = source.getHeight();
    int secretW = secret.getWidth();
    int secretH = secret.getHeight();

    // System.out.println(source.getWidth() + " " + secret.getWidth());
    // System.out.println(source.getHeight() + " " + secret.getHeight());

    if (sourceW == secretW && sourceH == secretH)
    {
      return true;
    }
    return false;
  }

  /**
   * Creates a new Picture with data from secret hidden in data from source
   * precondition: source is same width and height as secret
   * 
   * @param source
   *          is not null
   * @param secret
   *          is not null
   * @return combined Picture with secret hidden in source
   */
  public static Picture hidePicture(Picture source, Picture secret)
  {
    // TODO: Activity 2 Question 9

    /** HINTS:
     * @formatter:off
     * Create a new image from source
     * Get the 2D array of pixels from the new image
     * Get the 2D array of pixels from the secret image
     * NESTED LOOP For each pixel in the 2D array from secret image
     *   get the color of the secret pixel
     *   use setLow to set the lowest bits of the matching pixel.
     * Don't forget to return the picture.
     * @formatter:on
     */
    Picture combined = new Picture(source);
    Pixel[][] sourceArray = source.getPixels2D();
    Pixel[][] secretArray = secret.getPixels2D();

    Pixel[][] combinedArray = combined.getPixels2D();
    
    for (int row = 0; row < secretArray.length; row++)
    {
      for (int col = 0; col < secretArray[0].length; col++)
      {
        Color secretColor = secretArray[row][col].getColor();
        setLow(combinedArray[row][col], secretColor);
      }
    }

    return combined;
  }

  /**
   * Hides secret in picture, starting at a given point in picture
   * precondition: source is same or greater width and height as secret, AND
   * startRow and startColumn don't make the secret picture exceed the edges
   * of the source picture.
   * 
   * @param source
   *          is not null
   * @param secret
   *          is not null
   * @param startRow
   *          row in source where hidden pic will start
   * @param startColumn
   *          column in source where hidden pic will start
   * @return combined Picture with secret hidden in source
   */
  public static Picture hidePicture(Picture source, Picture secret,
                                    int startRow, int startColumn)
  {
    // TODO: Activity 3 Question 1
    /**
     * HINT: Instead of starting at zero for the row and col start at startRow
     * and startColumn, then end at width and height.
     */
    Picture combined = new Picture(source);
    Pixel[][] hPixels = combined.getPixels2D();
    // TODO: Complete the code here.

    return combined;
  }

  /**
   * Checks to see if pic1 and pic2 match
   * 
   * @param pic1
   *          first picture
   * @param pic2
   *          second picture
   * @return true if pics match; false otherwise
   */
  public static boolean isSame(Picture pic1, Picture pic2)
  {
    // TODO: Activity 3 Question 2
    /**
     * HINT: Get the pixel 2D arrays from both pictures, then return false if
     * they aren't the same dimensions. Then iterate through typical nested
     * loops and compare the red,green,blue colors values. If they aren't equal,
     * immediately return false.
     */
    Pixel[][] pixels = pic1.getPixels2D();
    Pixel[][] otherPixels = pic2.getPixels2D();
    // TODO: Complete the code here.
    return true;
  }

  /**
   * Returns arraylist of points where pictures differ
   * 
   * @param pic1
   *          first picture
   * @param pic2
   *          second picture
   * @return list of points where pic1 and pic2 differ or * returns empty list
   *         if they are not the same size
   */
  public static ArrayList<Point> findDifferences(Picture pic1, Picture pic2)
  {
    // TODO: Activity 3 Question 3
    /**
     * HINT: Similar to the isSame. Create a list of Points. When you find a
     * difference in RGB for a point, then add that Point to the arraylist.
     * Return an empty arraylist if the dimensions are different. The Point
     * class has been already created in this project.
     */
    ArrayList<Point> list = new ArrayList<>();
    // TODO: Complete the code here.
    return list;
  }

  /**
   * Draws red rectangle around area containing points
   * 
   * @param pic
   *          source picture
   * @param points
   *          list of points
   * @return pic with rectangle drawn pre-condition all of points are on the
   *         Picture pic * pre-condition - points contains at least two points
   */
  public static Picture showDifferentArea(Picture pic, ArrayList<Point> points)
  {
    // TODO: Activity 3 Question 4
    /**
     * Hints:
     * @formatter:off
     * Clone the pic into a new Picture object called result.
     * Get the pixel row and pixel width value (don't forget to subtract 1)
     * You'll write a loop that determines the coordinates
     * of the upper left and lower corner of pic. Loop through
     * the arraylist and find these points.
     * @formatter:on
     */

    Picture result = new Picture(pic);
    Pixel[][] pixels = result.getPixels2D();
    
    // Find min and max row and col
    int minRow = Integer.MAX_VALUE;
    int maxRow = Integer.MIN_VALUE;
    int minCol = Integer.MAX_VALUE;
    int maxCol = Integer.MIN_VALUE;
    
    for (Point p : points) {
      if (p.getRow() < minRow) minRow = p.getRow();
      if (p.getRow() > maxRow) maxRow = p.getRow();
      if (p.getCol() < minCol) minCol = p.getCol();
      if (p.getCol() > maxCol) maxCol = p.getCol();
    }
    
    // Draw top and bottom lines
    for (int col = minCol; col <= maxCol; col++) {
      pixels[minRow][col].setColor(Color.RED);
      pixels[maxRow][col].setColor(Color.RED);
    }
    
    // Draw left and right lines
    for (int row = minRow; row <= maxRow; row++) {
      pixels[row][minCol].setColor(Color.RED);
      pixels[row][maxCol].setColor(Color.RED);
    }
    
    return result;
  }

  /**
   * Takes a string consisting of letters and spaces and encodes the string into
   * an arraylist of integers. The integers are 1-26 for A-Z, 27 for space, and
   * 0 for end of string. The arraylist of integers is returned. Call this
   * method in hideText
   * 
   * @param s
   *          string consisting of letters and spaces
   * @return ArrayList containing integer encoding of uppercase
   *
   *         version of s
   */
  public static ArrayList<Integer> encodeString(String topSecretTextMessage)
  {
    // For Activity 4 Question 1 -
    // CODE IS ALREADY COMPLETE - LEAVE THIS METHOD ALONE!
    String upperCaseTopSecretTextMessage = topSecretTextMessage.toUpperCase();
    String alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    ArrayList<Integer> result = new ArrayList<Integer>();
    for (int i = 0; i < upperCaseTopSecretTextMessage.length(); i++)
    {
      String aLetter = upperCaseTopSecretTextMessage.substring(i, i + 1);
      if (aLetter.equals(" "))
      {
        result.add(27);
      }
      else
      {
        // Add one since A is 1 not zero.
        int letterLocation = alpha.indexOf(aLetter) + 1;
        result.add(letterLocation);
      }
    }
    result.add(0);
    return result;
  }

  /**
   * Returns the string represented by the codes arraylist. * 1-26 = A-Z, 27 =
   * space
   * 
   * @param codes
   *          encoded string
   * @return decoded string
   */
  public static String decodeString(ArrayList<Integer> codes)
  {
    // For Activity 4 Question 1
    // CODE IS ALREADY COMPLETE - LEAVE THIS METHOD ALONE!
    String result = "";
    String alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (int i = 0; i < codes.size(); i++)
    {
      if (codes.get(i) == 27)
      {
        result += " ";
      }
      else
      {
        int letterLocation = codes.get(i);

        result += alpha.substring(letterLocation - 1, letterLocation);
      }
    }
    return result;
  }

  /**
   * Given a number from 0 to 63, creates and returns a 3-element * int array
   * consisting of the integers representing the pairs of bits in the number
   * from right to left.
   * (100, 2, 255)
   * (10011100, 00000001, 11111110)
   * (99, 4, 254)
   * 
   * E = 6
   * 110
   * 00 01 10
   * 110 = 6 = E
   * 
   * @param num
   *          number to be broken up
   * @return bit pairs in number
   */
  private static int[] getBitPairs(int num)
  {
    // For Activity 4 Question 1
    // CODE IS ALREADY COMPLETE - LEAVE THIS METHOD ALONE!
    int[] bits = new int[3];
    int code = num;
    for (int i = 0; i < 3; i++)
    {
      bits[i] = code % 4;
      code = code / 4;
    }
    return bits;
  }

  /**
   * Hide a string (must be only capital letters and spaces) in a * picture. The
   * string always starts in the upper left corner.
   * 
   * @param source
   *          picture to hide string in
   * @param s
   *          string to hide
   * @return picture with hidden string
   */
  public static Picture hideText(Picture source, String topSecretTextMessage)
  {
    // TODO: Activity 4 Question 2
    /**
     * Hints:
     * @formatter:off
     * Create a clone of source and store it into newPic
     * Get the 2D array of the pixels from it.
     * Use encodeString to create ArrayList eCode of integers from topSecretTextMessage.
     *   that converts each letter into a number
     * 
     * Create your typical nested loop but stop when you
     *   are done with every letter in the message.
     *   
     *   get the RGB values from each pixel
     *   clear the Low bits from the pixel to make space for the encoded letter
     *   get the color from it.
     *   Get a value from the eCode to convert the letter into
     *     an int array - [0] will have red, [1] green and [2] blue.
     *   Create a new color and add bits[0] to red, bits[1] to gree
     *     and bits[2] to blue.
     *   bump up the counter 
     * 
     * @formatter:on
     */
    Pixel leftPixel = null;
    Picture newPic = new Picture(source);
    Pixel[][] pixels = newPic.getPixels2D();
    Color leftColor = null;
    // TODO: Complete the code here.
    ArrayList<Integer> eCode = encodeString(topSecretTextMessage);
    int counter = 0;
    for (int row = 0; row < pixels.length && counter < eCode.size(); row++)
    {
      for (int col = 0; col < pixels[0].length && counter < eCode.size(); col++)
      {
        int code = eCode.get(counter);
        int[] bits = getBitPairs(code);
        Color hideColor = new Color(bits[0] * 64, bits[1] * 64, bits[2] * 64);
        setLow(pixels[row][col], hideColor);
        counter++;
      }
    }
    
    return newPic;
  }

  /**
   * Returns a string hidden in the picture
   * 
   * @param source
   *          picture with hidden string * @return revealed string
   */
  public static String revealText(Picture source)
  {
    // TODO: Activity 4 Question 3
    /**
     * Hints:
     * @formatter:off
     * Create a clone of source and store it into newPic
     * Get the 2D array of the pixels from it.
     * Create a new Integer arraylist called codes
     * Visit each pixel in the image. (Nested for loops)
     *   get the color of the pixel
     *   get the rgb values
     *   To get the code compute the sum
     *              (MOD the red by 4) + 
     *              (MOD the green by 4, then multiply by 4) +
     *              (MOD the blue by 4, the multiply by 16)
     *   If the code is zero, then there's no more encoded message
     *   Add the code to the ArrayList codes
     *   
     * After the loop is done, decode the codes ArrayList
     * return the message.
     *   
     * @formatter:on
     */
    Pixel leftPixel = null;
    Pixel[][] pixels = source.getPixels2D();
    Color leftColor = null;
    ArrayList<Integer> codes = new ArrayList<Integer>();
    // TODO: Complete the code here.
    for (int row = 0; row < pixels.length; row++)
    {
      for (int col = 0; col < pixels[0].length; col++)
      {
        Color color = pixels[row][col].getColor();
        int code = (color.getRed() % 4) + ((color.getGreen() % 4) * 4) + ((color.getBlue() % 4) * 16);
        if (code == 0)
        {
          return decodeString(codes);
        }
        codes.add(code);
      }
    }
    return decodeString(codes);
  }

}
