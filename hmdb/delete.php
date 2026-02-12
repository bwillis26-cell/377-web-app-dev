<?php 
/************************
 * delete.php
 * 
 * Deletes a whole movie from the database
 */



$connection = get_connection();

$delete =<<<SQL
DELETE FROM movie
WHERE mov_id = $id
SQL;

header('Location: index.php?content=list');