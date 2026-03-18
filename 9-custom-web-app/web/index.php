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



        <link rel='stylesheet' type='text/css' media='screen' href='styles.css?v=<?php echo rand(); ?>'>
        
        <script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

        <title>Salty Canvas</title>
    </head>

    <body>
        <div class="container">
            <h1 class='title'>Salty Canvas</h1>
            <?php
            extract($_REQUEST);

            if (!isset($nav)) {
                $nav = "gallery";
            } 
            
            ?>
            <div class='navbar'>
            <a href="index.php?nav=gallery"     <?php if ($nav == 'gallery')     print('class="selected"'); ?>>Home</a>
            <a href="index.php?nav=review" <?php if ($nav == 'review') print('class="selected"'); ?>>Reviews</a>
            <a href="index.php?nav=media"    <?php if ($nav == 'media')    print('class="selected"'); ?>>Contact Info</a>
            </div>
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