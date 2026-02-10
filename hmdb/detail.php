<?php
$servername = "localhost";
$username = "root";
$password = "password";
$dbname = "hmdb";

$connection = new mysqli($servername, $username, $password, $dbname);
if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

extract($_REQUEST);

$sql =<<<SQL
SELECT *
FROM movie
WHERE mov_id = $id
SQL;

$result = $connection->query($sql);
$row = $result->fetch_assoc();

echo "<table><tr>";

echo "<td>" . $row["mov_id"] . "</td>";
echo "<td>" . $row["mov_title"] . "</td>";
echo "<td>" . $row["mov_genre"] . "</td>";
echo "<td>" . $row["mov_rating"] . "</td>";
echo "<td>" . $row["mov_mpaa"] . "</td>";
echo "<td>" . $row["mov_duration"] . "</td>";
echo "<td>" . $row["mov_release_year"] . "</td>";

echo "</tr></table>";

?>