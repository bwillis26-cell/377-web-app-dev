<html>
    <head>
        <title></title>
    </head>

    <body>
        <h1>hMDB: The Hanover Movie Database</h1>

        <h2>Movies</h2>

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

$sql = "SELECT * FROM movie";

$result = $connection->query($sql);
while ($row = $result->fetch_assoc()) {

    echo "<tr>";
    echo "<td>" . $row["mov_id"] . "</td>";
    echo "<td>" . $row["mov_title"] . "</td>";
    echo "<td>" . $row["mov_duration"] . "</td>";
    echo "<td>" . $row["mov_release"] . "</td>";
    echo "</tr>";
}

?>
        </table>


    </body>
</html>