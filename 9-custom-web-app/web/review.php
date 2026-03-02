<?php

/*************************************************************************************************
 * list.php
 *
 * Displays a list of movies. This page expects to be included within index.php.
 *************************************************************************************************/

?>

<h2>Reviews <span id="record-count"></span></h2>

<a href='index.php?content=review'>All</a>

<?php


for ($rating = 0; $rating < 5; $rating++)
{
    
    echo "<a href='index.php?content=review&filter=$rating'>$rating</a> ";
}

?>

<a href='index.php?content=detail' class='btn btn-primary'>Add</a>

<table class="table table-bordered table-hover">
    <thead class="thead-dark">
        <tr>
            <th>Rating</th>
            <th>Last Name</th>
            <th>First Name</th>
            <th>Work Done</th>
            <th>Hours Taken</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>

<?php

$connection = get_connection();

if (!isset($filter))
{
    $filter = '';
}
else
{
    $filter = $connection->real_escape_string($filter);
}

$sql =<<<SQL
 SELECT *
   FROM movie
  WHERE rev_rating IN BETWEEN $filter AND ($filter + 1)
  ORDER BY mov_title
SQL;

$recordCount = 0;
$result = $connection->query($sql);
while ($row = $result->fetch_assoc())
{
    echo "<tr>";
    echo "<td><a href='index.php?content=detail&id=". $row["mov_id"] . "'>" . $row["mov_title"] . "</a></td>";
    echo "<td>" . $row["mov_duration"] . "</td>";
    echo "<td>" . $row["mov_release_year"] . "</td>";
    echo "</tr>";

    $recordCount++;
}

?>

    </tbody>
</table>

<?php

$code =<<<JS
<script>
document.getElementById('record-count').innerHTML = '(' + $recordCount + ' records)';
</script>
JS;

echo $code;

?>