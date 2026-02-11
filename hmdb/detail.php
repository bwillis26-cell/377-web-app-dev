<?php

$connection = get_connection();

$sql =<<<SQL
SELECT *
FROM movie
WHERE mov_id = $id
SQL;


$result = $connection->query($sql);
$row = $result->fetch_assoc();

echo "<a href='index.php'>Back to Full Database</a> ";

echo "<table border=1>";

echo "<tr><th>ID</th><td><input type='text' value='" . $row['mov_id'] . "'></input></td></tr>"; 
echo "<tr><th>Title</th><td><input type='text' value='" . $row['mov_title'] . "'></input></td></tr>";
echo "<tr><th>Duration</th><td><input type='text' value='" . $row['mov_duration'] . "'></input></td></tr>";
echo "<tr><th>Release Year</th><td><input type='text' value='" . $row['mov_release_year'] . "'></input></td></tr>";
echo "<tr><th>MPAA Rating</th><td><input type='text' value='" . $row['mov_mpaa'] . "'></input></td></tr>";
echo "<tr><th>Star Rating</th><td><input type='text' value='" . $row['mov_rating'] . "'></input></td></tr>";
echo "<tr><th>Genre</th><td><input type='text' value='" . $row['mov_genre'] . "'></input></td></tr>";

echo "</table>";

?>