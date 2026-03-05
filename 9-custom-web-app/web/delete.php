<?php 
/************************
 * delete.php
 * 
 * Deletes a whole movie from the database
 */

include("library.php");
$connection = get_connection();

$delete =<<<SQL
DELETE FROM reviews
WHERE rev_id = $id
SQL;

$connection->query($delete);

header('Location: index.php?nav=review');