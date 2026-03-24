import static org.junit.Assert.assertEquals;

import java.awt.Color;
import java.util.ArrayList;

import org.junit.FixMethodOrder;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.Timeout;
import org.junit.runners.MethodSorters;

import picturelib.*;

/**
 * Do not turn this particular file to the dropbox.
 * 
 * @version 5.1
 */

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class SecretTextTest
{
  @Rule
  public Timeout globalTimeout = Timeout.seconds(4);

  @Test
  public void test01Act1ClearLow1()
  {
    Picture testPicture = new Picture("kitten2.png");
    Pixel tp = new Pixel(testPicture, 10, 10);
    SecretText.clearLow(tp);
    assertEquals("java.awt.Color[r=132,g=128,b=108]", tp.getColor().toString());
  }

  @Test
  public void test02Act1ClearLow2()
  {
    Picture testPicture = new Picture("kitten2.png");
    Pixel tp = new Pixel(testPicture, 42, 45);
    SecretText.clearLow(tp);
    assertEquals("java.awt.Color[r=140,g=140,b=136]", tp.getColor().toString());
  }

  @Test
  public void test03Act1ClearLow3()
  {
    Picture testPicture = new Picture("seagull.png");
    Pixel tp = new Pixel(testPicture, 15, 10);
    SecretText.clearLow(tp);
    assertEquals("java.awt.Color[r=112,g=132,b=152]", tp.getColor().toString());
  }

  @Test
  public void test04Act1TestClearLow1()
  {
    Picture testPicture = new Picture("seagull.png");
    Picture clearedPicture = SecretText.testClearLow(testPicture);
    Pixel[][] pixels = clearedPicture.getPixels2D();

    int maxRow = clearedPicture.getHeight() - 1;
    int maxCol = clearedPicture.getWidth() - 1;

    assertEquals("Pixel row=242 col=161 red=116 green=128 blue=132",
                 pixels[maxRow / 2][maxCol / 4].toString());

    assertEquals("Pixel row=121 col=323 red=104 green=128 blue=132",
                 pixels[maxRow / 4][maxCol / 2].toString());

    assertEquals("Pixel row=121 col=215 red=128 green=152 blue=160",
                 pixels[maxRow / 4][maxCol / 3].toString());

    assertEquals("Pixel row=161 col=161 red=88 green=104 blue=100",
                 pixels[maxRow / 3][maxCol / 4].toString());

  }

  @Test
  public void test05Act1TestClearLow2()
  {
    Picture testPicture = new Picture("butterfly1.png");
    Picture clearedPicture = SecretText.testClearLow(testPicture);
    Pixel[][] pixels = clearedPicture.getPixels2D();

    int maxRow = clearedPicture.getHeight() - 1;
    int maxCol = clearedPicture.getWidth() - 1;

    assertEquals("Pixel row=248 col=105 red=44 green=36 blue=36",
                 pixels[maxRow / 2][maxCol / 4].toString());

    assertEquals("Pixel row=124 col=210 red=68 green=64 blue=48",
                 pixels[maxRow / 4][maxCol / 2].toString());

    assertEquals("Pixel row=124 col=140 red=176 green=204 blue=208",
                 pixels[maxRow / 4][maxCol / 3].toString());

    assertEquals("Pixel row=165 col=105 red=48 green=16 blue=8",
                 pixels[maxRow / 3][maxCol / 4].toString());
  }

  @Test
  public void test06Act1SetLow1()
  {
    Picture testPicture = new Picture("kitten2.png");
    Pixel tp = new Pixel(testPicture, 10, 10);
    SecretText.setLow(tp, new Color(123, 42, 200));
    assertEquals("java.awt.Color[r=133,g=128,b=111]", tp.getColor().toString());
  }

  @Test
  public void test07Act1SetLow2()
  {
    Picture testPicture = new Picture("kitten2.png");
    Pixel tp = new Pixel(testPicture, 15, 30);
    SecretText.setLow(tp, new Color(123, 42, 200));
    assertEquals("java.awt.Color[r=117,g=116,b=115]", tp.getColor().toString());
  }

  @Test
  public void test08Act1SetLow3()
  {
    Picture testPicture = new Picture("kitten2.png");
    Pixel tp = new Pixel(testPicture, 50, 24);
    SecretText.setLow(tp, new Color(123, 42, 200));
    assertEquals("java.awt.Color[r=129,g=124,b=107]", tp.getColor().toString());
  }

  @Test
  public void test09Act1TestSetLow1()
  {
    Picture testPicture = new Picture("koala.png");
    Picture settedPicture =
      SecretText.testSetLow(testPicture, new Color(255, 250, 253));
    Pixel[][] pixels = settedPicture.getPixels2D();

    int maxRow = settedPicture.getHeight() - 1;
    int maxCol = settedPicture.getWidth() - 1;

    assertEquals("Pixel row=4 col=9 red=119 green=135 blue=91",
                 pixels[4][9].toString());

    assertEquals("Pixel row=121 col=242 red=95 green=95 blue=79",
                 pixels[maxRow / 4][maxCol / 2].toString());

    assertEquals("Pixel row=121 col=161 red=103 green=91 blue=75",
                 pixels[maxRow / 4][maxCol / 3].toString());

    assertEquals("Pixel row=161 col=121 red=167 green=147 blue=119",
                 pixels[maxRow / 3][maxCol / 4].toString());

  }

  @Test
  public void test10Act1TestSetLow2()
  {
    Picture testPicture = new Picture("butterfly1.png");
    Picture settedPicture =
      SecretText.testSetLow(testPicture, new Color(243, 231, 154));
    Pixel[][] pixels = settedPicture.getPixels2D();

    int maxRow = settedPicture.getHeight() - 1;
    int maxCol = settedPicture.getWidth() - 1;

    assertEquals("Pixel row=248 col=105 red=47 green=39 blue=38",
                 pixels[maxRow / 2][maxCol / 4].toString());

    assertEquals("Pixel row=124 col=210 red=71 green=67 blue=50",
                 pixels[maxRow / 4][maxCol / 2].toString());

    assertEquals("Pixel row=124 col=140 red=179 green=207 blue=210",
                 pixels[maxRow / 4][maxCol / 3].toString());

    assertEquals("Pixel row=165 col=105 red=51 green=19 blue=10",
                 pixels[maxRow / 3][maxCol / 4].toString());
  }

  @Test
  public void test11Act1TestRevealPictureWithSimpleColor1()
  {
    Picture testPicture = new Picture("beachhiddenpink.png");
    Picture secretPicture = SecretText.revealPicture(testPicture);
    Pixel[][] pixels = secretPicture.getPixels2D();

    int maxRow = secretPicture.getHeight() - 1;
    int maxCol = secretPicture.getWidth() - 1;

    assertEquals("Pixel row=239 col=159 red=192 green=128 blue=128",
                 pixels[maxRow / 2][maxCol / 4].toString());

    assertEquals("Pixel row=119 col=319 red=192 green=128 blue=128",
                 pixels[maxRow / 4][maxCol / 2].toString());

    assertEquals("Pixel row=119 col=213 red=192 green=128 blue=128",
                 pixels[maxRow / 4][maxCol / 3].toString());

    assertEquals("Pixel row=159 col=159 red=192 green=128 blue=128",
                 pixels[maxRow / 3][maxCol / 4].toString());
  }

  @Test
  public void test12Act1TestRevealPictureWithSimpleColor2()
  {
    Picture testPicture = new Picture("jenny-redhidden.png");
    Picture secretPicture = SecretText.revealPicture(testPicture);
    Pixel[][] pixels = secretPicture.getPixels2D();

    int maxRow = secretPicture.getHeight() - 1;
    int maxCol = secretPicture.getWidth() - 1;

    assertEquals("Pixel row=132 col=74 red=0 green=0 blue=192",
                 pixels[maxRow / 2][maxCol / 4].toString());

    assertEquals("Pixel row=66 col=149 red=0 green=0 blue=192",
                 pixels[maxRow / 4][maxCol / 2].toString());

    assertEquals("Pixel row=66 col=99 red=0 green=0 blue=192",
                 pixels[maxRow / 4][maxCol / 3].toString());

    assertEquals("Pixel row=88 col=74 red=0 green=0 blue=192",
                 pixels[maxRow / 3][maxCol / 4].toString());
  }

  @Test
  public void test13Act2CanHide1()
  {
    Picture arch = new Picture("arch.png");
    Picture beach = new Picture("beach.png");
    assertEquals("false", SecretText.canHide(arch, beach) + "");

    // Commented out to stop equal height issue.
    // assertEquals("false", SecretText.canHide(beach, arch) + "");

    Picture swan = new Picture("swan.png");
    Picture gorge = new Picture("gorge.png");
    assertEquals("true", SecretText.canHide(swan, gorge) + "");
    assertEquals("true", SecretText.canHide(gorge, swan) + "");
  }

  @Test
  public void test14Act2HidePicture1()
  {
    Picture swan = new Picture("swan.png");
    Picture gorge = new Picture("gorge.png");
    Picture combinedPic = SecretText.hidePicture(swan, gorge);
    Pixel[][] pixels = combinedPic.getPixels2D();

    int maxRow = combinedPic.getHeight() - 1;
    int maxCol = combinedPic.getWidth() - 1;

    assertEquals("Pixel row=179 col=119 red=58 green=53 blue=48",
                 pixels[maxRow / 2][maxCol / 4].toString());

    assertEquals("Pixel row=89 col=239 red=53 green=53 blue=45",
                 pixels[maxRow / 4][maxCol / 2].toString());

    assertEquals("Pixel row=89 col=159 red=49 green=48 blue=44",
                 pixels[maxRow / 4][maxCol / 3].toString());

    assertEquals("Pixel row=119 col=119 red=61 green=61 blue=56",
                 pixels[maxRow / 3][maxCol / 4].toString());

  }

  @Test
  public void test15Act2HidePicture2()
  {
    Picture swan = new Picture("blueMotorcycle.png");
    Picture gorge = new Picture("blue-mark.png");
    Picture combinedPic = SecretText.hidePicture(swan, gorge);
    Pixel[][] pixels = combinedPic.getPixels2D();

    int maxRow = combinedPic.getHeight() - 1;
    int maxCol = combinedPic.getWidth() - 1;

    assertEquals("Pixel row=239 col=159 red=224 green=220 blue=245",
                 pixels[maxRow / 2][maxCol / 4].toString());

    assertEquals("Pixel row=119 col=319 red=132 green=128 blue=117",
                 pixels[maxRow / 4][maxCol / 2].toString());

    assertEquals("Pixel row=119 col=213 red=184 green=168 blue=153",
                 pixels[maxRow / 4][maxCol / 3].toString());

    assertEquals("Pixel row=159 col=159 red=116 green=120 blue=153",
                 pixels[maxRow / 3][maxCol / 4].toString());

  }

  @Test
  public void test16Act2RevealPictureWithComplexPhoto1()
  {
    Picture combinedPic = new Picture("swanhidden.png");
    Picture revealedPic = SecretText.revealPicture(combinedPic);
    Pixel[][] pixels = revealedPic.getPixels2D();

    int maxRow = combinedPic.getHeight() - 1;
    int maxCol = combinedPic.getWidth() - 1;

    assertEquals("Pixel row=179 col=119 red=128 green=64 blue=0",
                 pixels[maxRow / 2][maxCol / 4].toString());

    assertEquals("Pixel row=89 col=239 red=64 green=64 blue=64",
                 pixels[maxRow / 4][maxCol / 2].toString());

    assertEquals("Pixel row=89 col=159 red=64 green=0 blue=0",
                 pixels[maxRow / 4][maxCol / 3].toString());

    assertEquals("Pixel row=119 col=119 red=64 green=64 blue=0",
                 pixels[maxRow / 3][maxCol / 4].toString());

  }

  @Test
  public void test17Act2RevealPictureWithComplexPhoto2()
  {
    Picture combinedPic = new Picture("blueMotorcyclehidden.png");
    Picture revealedPic = SecretText.revealPicture(combinedPic);
    Pixel[][] pixels = revealedPic.getPixels2D();

    int maxRow = combinedPic.getHeight() - 1;
    int maxCol = combinedPic.getWidth() - 1;

    assertEquals("Pixel row=239 col=159 red=0 green=0 blue=64",
                 pixels[maxRow / 2][maxCol / 4].toString());

    assertEquals("Pixel row=16 col=632 red=64 green=64 blue=0",
                 pixels[16][632].toString());

    assertEquals("Pixel row=331 col=234 red=128 green=128 blue=128",
                 pixels[331][234].toString());

    assertEquals("Pixel row=210 col=340 red=128 green=64 blue=64",
                 pixels[210][340].toString());

  }

  @Test
  public void test18Act3CanHideSmallInsideBig1()
  {
    Picture smallPic = new Picture("KatieFancy.png");
    Picture bigPic = new Picture("koala.png");
    assertEquals("false", SecretText.canHide(smallPic, bigPic) + "");
    assertEquals("true", SecretText.canHide(bigPic, smallPic) + "");

    Picture arch = new Picture("arch.png");
    Picture beach = new Picture("beach.png");

    assertEquals("true", SecretText.canHide(beach, arch) + "");
  }

  @Test
  public void test19Act3HidePictureAtSpecificLocation1()
  {
    Picture smallPic = new Picture("KatieFancy.png");
    Picture bigPic = new Picture("koala.png");

    Picture combinedPic = SecretText.hidePicture(bigPic, smallPic, 50, 200);

    Pixel[][] pixels = combinedPic.getPixels2D();

    assertEquals("Pixel row=70 col=177 red=112 green=91 blue=70",
                 pixels[70][177].toString());

    assertEquals("Pixel row=409 col=344 red=121 green=130 blue=113",
                 pixels[409][344].toString());

    assertEquals("Pixel row=198 col=297 red=55 green=63 blue=55",
                 pixels[198][297].toString());

    assertEquals("Pixel row=60 col=389 red=98 green=94 blue=62",
                 pixels[60][389].toString());

  }

  @Test
  public void test20Act3HidePictureAtSpecificLocation2()
  {
    Picture smallPic = new Picture("KatieFancy.png");
    Picture bigPic = new Picture("koala.png");

    Picture combinedPic = SecretText.hidePicture(bigPic, smallPic, 75, 25);

    Pixel[][] pixels = combinedPic.getPixels2D();

    assertEquals("Pixel row=84 col=34 red=106 green=134 blue=89",
                 pixels[84][34].toString());

    assertEquals("Pixel row=418 col=220 red=57 green=53 blue=49",
                 pixels[418][220].toString());

    assertEquals("Pixel row=403 col=231 red=69 green=74 blue=67",
                 pixels[403][231].toString());

    assertEquals("Pixel row=74 col=228 red=107 green=119 blue=71",
                 pixels[74][228].toString());

  }

  @Test
  public void test21Act3IsSame1()
  {
    Picture pict1 = new Picture("swan.png");
    Picture pict2 = new Picture("swan.png");
    assertEquals("true", SecretText.isSame(pict1, pict2) + "");
    assertEquals("true", SecretText.isSame(pict2, pict1) + "");

    Picture pict3 = new Picture("swanlowcleared.png");
    assertEquals("false", SecretText.isSame(pict1, pict3) + "");
    assertEquals("false", SecretText.isSame(pict3, pict1) + "");
  }

  @Test
  public void test22Act3IsSame2()
  {
    Picture pict1 = new Picture("arch.png");
    Picture pict2 = new Picture("arch.png");
    assertEquals("true", SecretText.isSame(pict1, pict2) + "");
    assertEquals("true", SecretText.isSame(pict2, pict1) + "");

    Picture pict3 = new Picture("beach.png");
    assertEquals("false", SecretText.isSame(pict1, pict3) + "");
    assertEquals("false", SecretText.isSame(pict3, pict1) + "");
  }

  @Test
  public void test23Act3FindDifferences1()
  {
    Picture arch = new Picture("arch.png");
    Picture archCopy = new Picture("arch.png");
    ArrayList<Point> pointList = SecretText.findDifferences(arch, archCopy);
    assertEquals("Differences = 0", "Differences = " + pointList.size());
  }

  @Test
  public void test24Act3FindDifferences2()
  {
    Picture pic1 = new Picture("seagull.png");
    Picture pic2 = new Picture("whiteFlower.png");
    ArrayList<Point> pointList = SecretText.findDifferences(pic1, pic2);
    assertEquals("Differences = 314928", "Differences = " + pointList.size());
  }

  @Test
  public void test25Act3FindDifferences3()
  {
    // Robot is hidden in archhidden.png
    Picture pic1 = new Picture("arch.png");
    Picture pic2 = new Picture("archhidden.png");
    ArrayList<Point> pointList = SecretText.findDifferences(pic1, pic2);
    assertEquals("Differences = 2902", "Differences = " + pointList.size());
  }

  @Test
  public void test26Act3ShowDifferentArea3()
  {
    Picture originalPic = new Picture("femaleLionAndHall.png");
    Picture hiddenPic = new Picture("femaleLionAndHallhidden.png");
    ArrayList<Point> diffList =
      SecretText.findDifferences(originalPic, hiddenPic);
    Picture boundingRectanglePic =
      SecretText.showDifferentArea(hiddenPic, diffList);
    Pixel[][] pixels = boundingRectanglePic.getPixels2D();

    assertEquals("Pixel row=50 col=275 red=255 green=0 blue=0",
                 pixels[50][275].toString());

    assertEquals("Pixel row=49 col=275 red=88 green=161 blue=212",
                 pixels[49][275].toString());

    assertEquals("Pixel row=50 col=374 red=255 green=0 blue=0",
                 pixels[50][374].toString());

    assertEquals("Pixel row=214 col=372 red=255 green=0 blue=0",
                 pixels[214][372].toString());

    assertEquals("Pixel row=212 col=315 red=86 green=43 blue=22",
                 pixels[212][315].toString());

  }

  @Test
  public void test27Act3ShowDifferentArea4()
  {
    Picture originalPic = new Picture("koala.png");
    Picture hiddenPic = new Picture("koalahidden.png");
    ArrayList<Point> diffList =
      SecretText.findDifferences(originalPic, hiddenPic);
    Picture boundingRectanglePic =
      SecretText.showDifferentArea(hiddenPic, diffList);
    Pixel[][] pixels = boundingRectanglePic.getPixels2D();

    assertEquals("Pixel row=397 col=200 red=255 green=0 blue=0",
                 pixels[397][200].toString());

    assertEquals("Pixel row=398 col=200 red=210 green=204 blue=204",
                 pixels[398][200].toString());

    assertEquals("Pixel row=181 col=399 red=255 green=0 blue=0",
                 pixels[181][399].toString());

    assertEquals("Pixel row=181 col=398 red=161 green=188 blue=152",
                 pixels[181][398].toString());

    assertEquals("Pixel row=396 col=296 red=141 green=141 blue=113",
                 pixels[396][296].toString());

  }

  @Test
  public void test28Act4HideText1()
  {
    Picture normalPic = new Picture("beach.png");
    String secretMessage =
      "Mission Statement"
        + " Our mission is to provide students and teachers with collaborative and engaging learning opportunities."
        + " Vision Statement"
        + " Our vision is to prepare students to be successful in college, careers, and life.";
    Picture hiddenMessagePic = SecretText.hideText(normalPic, secretMessage);
    Pixel[][] pixels = hiddenMessagePic.getPixels2D();

    assertEquals("Pixel row=0 col=50 red=20 green=37 blue=41",
                 pixels[0][50].toString());

    assertEquals("Pixel row=0 col=0 red=1 green=7 blue=0",
                 pixels[0][0].toString());

    assertEquals("Pixel row=1 col=120 red=38 green=46 blue=23",
                 pixels[1][120].toString());

    assertEquals("Pixel row=1 col=42 red=24 green=35 blue=48",
                 pixels[1][42].toString());

    assertEquals("Pixel row=0 col=220 red=140 green=176 blue=220",
                 pixels[0][220].toString());

  }

  @Test
  public void test29Act4HideText2()
  {
    Picture normalPic = new Picture("water.png");
    String secretMessage =
      "Just as in a face-to-face class, regular attendance, active participation, "
        + "timely completion of assignments, and thorough attention to task make "
        + "for a successful online learning experience.";
    Picture hiddenMessagePic = SecretText.hideText(normalPic, secretMessage);
    Pixel[][] pixels = hiddenMessagePic.getPixels2D();

    assertEquals("Pixel row=0 col=151 red=31 green=160 blue=153",
                 pixels[0][151].toString());

    assertEquals("Pixel row=0 col=100 red=23 green=153 blue=140",
                 pixels[0][100].toString());

    assertEquals("Pixel row=1 col=6 red=36 green=158 blue=135",
                 pixels[1][6].toString());

    assertEquals("Pixel row=1 col=42 red=31 green=161 blue=143",
                 pixels[1][42].toString());

    assertEquals("Pixel row=0 col=189 red=16 green=148 blue=152",
                 pixels[0][189].toString());

    assertEquals("Pixel row=0 col=190 red=20 green=150 blue=150",
                 pixels[0][190].toString());

  }

  @Test
  public void test30Act4RevealText1()
  {
    Picture hiddenText = new Picture("butterfly1hiddentext.png");
    String secretMessage = SecretText.revealText(hiddenText);
    assertEquals("VHS RULES", secretMessage);

  }

  @Test
  public void test31Act4RevealText2()
  {
    Picture hiddenText = new Picture("kitten2hiddentext.png");
    String secretMessage = SecretText.revealText(hiddenText);
    String expectedMessage =
      "STUDENT TO STUDENT INTERACTION IS AN INTEGRAL "
        + "PART OF ALL ASYNCHRONOUS VHS LEARNING COURSES STUDENTS COMMUNICATE "
        + "THROUGH ASYNCHRONOUS THREADED DISCUSSION AND WORK TOGETHER IN GROUP "
        + "PROJECTS ASYNCHRONOUS MEANS THAT STUDENTS CAN WORK ON THEIR COURSES "
        + "ANY TIME DURING THE DAY OR EVENING AS LONG AS THEY MEET THE "
        + "DEADLINES AND DUE DATES SET BY THEIR COURSE INSTRUCTORS";
    assertEquals(expectedMessage, secretMessage);

  }
  // Copyright VHS Learning 2025+

}
