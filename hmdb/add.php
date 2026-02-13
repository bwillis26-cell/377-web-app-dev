<?php

/*************************************************************************************************
 * detail.php
 *
 * Displays the details for a single movie. This page expects to be included within index.php.
 *************************************************************************************************/

$connection = get_connection();

// $sql =<<<SQL
// SELECT *
//   FROM movie
//  WHERE mov_id = $id
// SQL;

// Run the query on the database
// $result = $connection->query($sql);

// Store the ONE result in an associative array
// $row = $result->fetch_assoc();

?>

<h2>NEW MOVIE</h2>
<form action="save.php" method="POST">
    <input type="hidden" class="form-control" name="id">

    <div class="mb-3">
        <label for="title" class="form-label">Title</label>
        <input type="text" class="form-control" name="title">
    </div>

    <div class="mb-3">
        <label for="genre" class="form-label">Genre</label>
        <input type="text" class="form-control" name="genre">
    </div>

    <div class="mb-3">
        <label for="rating" class="form-label">Rating</label>
        <input type="text" class="form-control" name="rating">
    </div>

    <div class="mb-3">
        <label for="mpaa" class="form-label">MPAA</label>
        <input type="text" class="form-control" name="mpaa">
    </div>

    <div class="mb-3">
        <label for="duration" class="form-label">Duration</label>
        <input type="text" class="form-control" name="duration">
    </div>

    <div class="mb-3">
        <label for="release_year" class="form-label">Release Year</label>
        <input type="text" class="form-control" name="release_year">
    </div>

    <button type="submit" class="btn btn-primary">Create Record</button>
    <a href="delete.php?id=" class="btn btn-secondary" role="button">Cancel</a>

</form>