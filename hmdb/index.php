<html>
    <head>
        <title></title>
    </head>

    <body>
        <h1>hMDB: The Hanover Movie Database</h1>

        <h2>Movies</h2>

<?php 

for ($i = 0; $i < 26; $i++) {
    $letter = chr($i + ord("A"));
    echo "<a href='index.php?filter=$letter'>$letter</a> ";
}

echo "<a href='index.php'>All</a> ";

?>

        <table border='1'>
            <tr>
                <th>ID</th>
                <th>Title</th>
                <th>Duration</th>
                <th>Release Date</th>

<?php 

$servername = "localhost";
$username = "root";
$password = "password";
$dbname = "hmdb";

//Connect tp the database and make sure it was successful
$connection = new mysqli($servername, $username, $password, $dbname);
if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

extract($_REQUEST);
if (!isset($filter)) {
    $filter = '';
}

$sql =<<<SQL
SELECT * 
FROM movie
WHERE mov_title LIKE '$filter%'
ORDER BY mov_title
SQL;

$result = $connection->query($sql);
while ($row = $result->fetch_assoc()) {

    echo "<tr>";
    echo "<td>" . $row["mov_id"] . "</td>";
    echo "<td>" . $row["mov_title"] . "</td>";
    echo "<td>" . $row["mov_duration"] . "</td>";
    echo "<td>" . $row["mov_release_year"] . "</td>";
    echo "</tr>";
}

?>
        </table>


    </body>
</html>