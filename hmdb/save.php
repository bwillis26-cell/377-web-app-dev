<?php
/*********************************************************************************
 * save.php
 * 
 * This page saves a single movie record based on the values submitted by the user
 *********************************************************************************/

include("library.php");

$connection = get_connection();

$title = $connection->real_escape_string($title);
$genre = $connection->real_escape_string($genre);
$mpaa = $connection->real_escape_string($mpaa);
$rating = $connection->real_escape_string($rating);
$duration = $connection->real_escape_string($duration);
$release_year = $connection->real_escape_string($release_year);

if ($id == null || $id == 0 || !isset($id)) {
    $update =<<<SQL
    INSERT INTO movie 
    (mov_title, mov_genre, mov_rating, mov_mpaa, mov_duration, mov_release_year)
    VALUES ('$title', '$genre', $rating, '$mpaa', $duration, $release_year)
    SQL;
} else {
    $update =<<<SQL
    UPDATE movie
    SET mov_title = '$title',
    mov_genre = '$genre',
    mov_mpaa = '$mpaa',
    mov_rating = $rating,
    mov_duration = $duration,
    mov_release_year = $release_year
    WHERE mov_id = $id
    SQL;

}
$connection->query($update);
header('Location: index.php?content=list');