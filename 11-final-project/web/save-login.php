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

$result = $connection->query("SELECT * FROM users WHERE username='$username' AND password='$password'");
if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    $id = $row['pla_id'];
    $playerOneUsername = $row['pla_username'];
    print($id);
} else {
    http_response_code(400);
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