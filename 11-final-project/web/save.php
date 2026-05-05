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
$date = $connection->real_escape_string($date);
$elo = $connection->real_escape_string($elo);
$totalGames = $connection->real_escape_string($totalGames);





$result = $connection->query("SELECT * FROM reviews WHERE pla_username = '$username'");
$update = "";
if ($id == "") {
    if ($result->num_rows > 0) {
        http_response_code(400);
        exit();
    } else {
        $playerOneUsername = $username;
        $update =<<<SQL
        INSERT INTO reviews (pla_username, pla_password, pla_date_created, pla_elo, pla_games_played)
        VALUES ('$username', '$password', '$date', $elo, $totalGames)
        SQL;
    }
} else {
    $row = $result->fetch_assoc();
    if ($row['pla_password'] != $password) {
        http_response_code(400);
        exit();
    } else {
        $playerOneUsername = $username;
    }
}

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