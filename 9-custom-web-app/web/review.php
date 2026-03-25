<?php

/*************************************************************************************************
 * review.php
 *
 * Displays a list of the reviews, you can add, edit, or delete reviews
 *************************************************************************************************/
?>
<div class='header'>
<h2>Reviews <span id="record-count"></span></h2>

<table id="main" class="stripe hover row-border compact"></table>

<?php 

$sql =<<<SQL
SELECT *
FROM reviews
ORDER BY rev_last_name
SQL;

$connection = get_connection();


$row = [];
$result = $connection->query($sql);
while ($row = $result->fetch_assoc()) {
    $rows[] = $row;
}

echo ('<script>');
echo ('var data = ' . json_encode($rows, JSON_PARTIAL_OUTPUT_ON_ERROR) . ';');
echo ('</script>');

?>

<script>
    var dataTable = $('#main').DataTable({
        data: data,
        columns: [
            { title: "Name", data: "rev_last_name", render: function(data, type, row) {
                return '<a href="index.php?nav=detail&id=' + row.rev_id + '">' + data + ', ' + row.rev_first_name + '</a>';
            }},
            // { title: "First Name", data: "rev_first_name" },
            { title: "Rating", data: "rev_rating" },
            { title: "Date Completed", data: "rev_comp_date", render: },
            { title: "Work Done", data: "rev_type" },
            { title: "Hours Taken", data: "rev_time" },
            { title: "Description", data: "rev_description" }
        ]
    });

</script>


<hr>

<a href='index.php?nav=review'>All</a>

<?php


for ($rating = 0; $rating <=5; $rating++)
{
    
    echo "<a href='index.php?nav=review&filter=$rating'>$rating Stars</a> ";
}

?>

<a href='index.php?nav=detail' id='add'>Add</a></div>
<br><br>
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
    FROM reviews
    WHERE rev_rating = $filter
    ORDER BY rev_last_name
SQL;
}



$recordCount = 0;
$totalStars = 0;
$result = $connection->query($sql);
while ($row = $result->fetch_assoc())
{
    $totalStars += $row["rev_rating"];
    $recordCount++;
    echo "<tr>";
    echo "<td>" . $row["rev_rating"] . "</td>";
    echo "<td>" . $row["rev_last_name"] . "</td>";
    echo "<td>" . $row["rev_first_name"] . "</td>";
    echo "<td>" . $row["rev_type"] . "</td>";
    echo "<td>" . $row["rev_time"] . "</td>";
    echo "<td><a href='index.php?nav=detail&id=". $row["rev_id"] . "'>" . $row["rev_description"] . "</a></td>";
    echo "</tr>";

    
}

?>

    </tbody>
</table>

<?php

$code =<<<JS
<script>
document.getElementById('record-count').innerHTML = '(' + ($totalStars / $recordCount) + ' stars)';
</script>
JS;

echo $code;

?>