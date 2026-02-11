<html>
    <head>
        <title>hMDB</title>
    </head>

    <body>
        <h1>hMDB: The Hanover Movie Database</h1>

<?php 

//Include the library
include("library.php");
include("style.css");

//Include the proper content based on the `nav` request
if (!isset($nav)) {
    $nav = "list";
}
include("$nav.php");

?>

    </body>
</html>