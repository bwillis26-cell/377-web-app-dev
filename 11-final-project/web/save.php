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






$update = "";
if ($id == "") {
    $update =<<<SQL
    INSERT INTO reviews (pla_username, pla_password, pla_date_created, pla_elo, pla_games_played)
    VALUES ('$username', '$password', '$date', $elo, $totalGames)
    SQL;
} else {
    $update =<<<SQL
    UPDATE reviews
    SET pla_username = '$username',
    pla_password = '$password',
    pla_date_created = '$date',
    pla_elo = $elo,
    pla_games_played = $totalGames
    WHERE pla_id = $id
    SQL;
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