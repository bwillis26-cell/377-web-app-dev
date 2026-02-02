<html>
    <head>
        <title>PHP Lesson 1</title>
    </head>
    <body>
        <h1>PHP Lesson 1</h1>

        <p>     
        This is the first PHP lesson with simple PHP markup.
    
        <?php 
        for ($i = 0; $i < 10; $i++)
        {
            echo "Hello<br>"; 
        }

        $firstName = 'Will';
        $lastName = 'Davidson';

        $fullName = $firstName . ' ' . $lastName;
        echo $fullName;

        echo "<p>" . $fullName . " is in Web App Development</p>";
        echo "<p>$fullName is in Web App Development</p>";

        // Double quotes work with variables, single don't

        echo '<p>$fullName is in Web App Development</p>';


        
        ?>
    
        </p>
    </body>
</html>