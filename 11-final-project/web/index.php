<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta charset="utf-8">

        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <link rel='stylesheet' type='text/css' media='screen' href='styles.css?v=<?php echo rand(); ?>'>
        
        <script> 
            function showAlert(type, title, message) {
                $('#alert').hide();
                $('#alert').removeClass('alert-success alert-info alert-warning alert-danger').addClass('alert-' + type);
                $('#alertTitle').text(title);
                $('#alertMessage').html(message);
                $('#alert').fadeIn();
            }
        </script>
        <script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.13.2/brython.min.js"></script>
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.13.2/brython_stdlib.js"></script>
        <title>Chess</title>
    </head>

    <body onload="brython()">
        <div class="container">
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <a class="navbar-brand" href="?nav=game">Chess</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="?nav=game">Game</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="?nav=leaderboard">Leaderboard</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="?nav=login">Login</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="?nav=register">Register</a>
                        </li>
                    </ul>
                </div>
            </nav>


            <?php
            extract($_REQUEST);

            $playerOneUsername = "";
            $playerTwoUsername = "";



            if (!isset($nav)) {
                $nav = "login";
            }
            include("$nav.php");
            ?>
        </div>
    </body>
</html>