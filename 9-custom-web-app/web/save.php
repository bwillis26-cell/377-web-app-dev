<?php
/*********************************************************************************
 * save.php
 * 
 * This page saves a single movie record based on the values submitted by the user
 *********************************************************************************/

include("library.php");

$connection = get_connection();

$first = $connection->real_escape_string($first);
$last = $connection->real_escape_string($last);
$email = $connection->real_escape_string($email);
$phone = $connection->real_escape_string($phone);
$type = $connection->real_escape_string($type);
$description = $connection->real_escape_string($description);
$time = $connection->real_escape_string($time);
$date = $connection->real_escape_string($date);
$rating = $connection->real_escape_string($rating);

$update = "";
if ($id == "") {
    $update =<<<SQL
    INSERT INTO reviews (rev_first_name, rev_last_name, rev_email, rev_phone_number, rev_type, rev_description, rev_time, rev_rating, rev_date)
    VALUES ('$first', '$last', '$email', '$phone', '$type', '$description', $time, $rating, '$date')
    SQL;
} else {
    $update =<<<SQL
    UPDATE reviews
    SET rev_first_name = '$first',
    rev_last_name = '$last',
    rev_email = '$email',
    rev_phone_number = '$phone',
    rev_type = '$type',
    rev_description = '$description',
    rev_time = $time,
    rev_rating = $rating,
    rev_date = '$date'
    WHERE rev_id = $id
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