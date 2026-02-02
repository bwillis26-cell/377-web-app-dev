<html>
    <head>
        <title>HHS Indoor Track</title>

        <style>
            a {
                border: solid 1px blue;
                background-color: lightblue;
                color: blue;
                text-decoration: none;
                padding: 5px;
                width:200px;
            }
            .selected{
                border: solid 1px black;
                background-color: blue;
                color: lightblue;
            }
            table, tr, th, td{
                border: solid 1px black;
            }
            </style>
    </head>

    <body>
        <!-- Section 1: Header -->
        <h1>Hanover High School Indoor Track</h1>

        <!-- Section 2: Menu -->
         <?php
            extract($_REQUEST);

            if (!isset($nav)) {
                $nav = "home";
            }
        ?>
        <a href="club.php?nav=home"     <?php if ($nav == 'home')     print('class="selected"'); ?>>Home</a>
        <a href="club.php?nav=schedule" <?php if ($nav == 'schedule') print('class="selected"'); ?>>Schedule</a>
        <a href="club.php?nav=media"    <?php if ($nav == 'media')    print('class="selected"'); ?>>Media</a>
        <a href="club.php?nav=roster"   <?php if ($nav == 'roster')   print('class="selected"'); ?>>Roster</a>

        <br><br><br><br>
        <!-- Section 3: Content -->
        <?php include("club-$nav.php") ?>
    </body>
</html>