<?php 
/**********************************************************
 * index.php
 * main page, holds other pages
 * 
 **********************************************************/

include('library.php');




?>

<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">



        <link rel='stylesheet' type='text/css' media='screen' href='styles.css'>
        <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script> -->

        <title>Salty Canvas</title>
    </head>

    <body>
        <div class="container">
            <h1>Salty Canvas</h1>
            <?php
            extract($_REQUEST);

            if (!isset($nav)) {
                $nav = "gallery";
            } 
            
            ?>
            
            <a href="index.php?nav=gallery"     <?php if ($nav == 'gallery')     print('class="selected"'); ?>>Home</a>
            <a href="index.php?nav=review" <?php if ($nav == 'review') print('class="selected"'); ?>>Reviews</a>
            <a href="index.php?nav=media"    <?php if ($nav == 'media')    print('class="selected"'); ?>>Contact Info</a>
            

            <?php
                // if (!isset($nav))
                // {
                //     $nav = "review";
                // }
                include("$nav.php");
            ?>
        </div>
    </body>
</html>