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
    $sql =<<<SQL
    SELECT *
    FROM reviews
    ORDER BY rev_last_name
SQL;
}
else
{
    $filter = $connection->real_escape_string($filter);
    $sql =<<<SQL
    SELECT *
    FROM movie
    WHERE rev_rating IN BETWEEN $filter AND ($filter + 1)
    ORDER BY rev_last_name
SQL;
}



$recordCount = 0;
$result = $connection->query($sql);
while ($row = $result->fetch_assoc())
{
    echo "<tr>";
    echo "<td>" . $row["rev_rating"] . "</td>";
    echo "<td>" . $row["rev_last_name"] . "</td>";
    echo "<td>" . $row["rev_first_name"] . "</td>";
    echo "<td>" . $row["rev_type"] . "</td>";
    echo "<td>" . $row["rev_time"] . "</td>";
    echo "<td><a href='index.php?content=detail&id=". $row["rev_id"] . "'>" . $row["rev_description"] . "</a></td>";
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