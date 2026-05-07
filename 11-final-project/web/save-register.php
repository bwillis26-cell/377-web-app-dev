<?php
/*********************************************************************************
 * save.php
 * 
 * This page saves a single movie record based on the values submitted by the user
 *********************************************************************************/

include("library.php");

$connection = get_connection();

$username = $connection->real_escape_string($username);
$password = $connection->real_escape_string($password);
$date = date("Y-m-d");
$elo = 600;
$totalGames = 0;

$result = $connection->query("SELECT * FROM users WHERE username='$username'");
$update = "";
if ($result->num_rows > 0) {
    http_response_code(400);
} else {
    $update =<<<SQL
    INSERT INTO users (pla_username, pla_password, pla_date_created, pla_elo, pla_games_played)
    VALUES ('$username', '$password', '$date', $elo, $totalGames)
    SQL;

    try {
        if ($connection->query($update)) {
            // http_response_code(200);
            $id = $connection->insert_id;
            print($id);
        } else {
            http_response_code(400);
        }
    } catch(Exception $e) {
        http_response_code(400);
    }
}