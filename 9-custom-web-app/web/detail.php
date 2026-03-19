<?php

/*************************************************************************************************
 * detail.php
 *
 * Displays the details for a single movie. This page expects to be included within index.php.
 *************************************************************************************************/



$first = "";
$last = "";
$email = "";
$phone = "";
$type = "";
$description = "";
$time = "";
$date = "";
$rating = "";

$header = "";


if (isset($id)) {
    $sql =<<<SQL
    SELECT *
    FROM reviews
    WHERE rev_id = $id
    SQL;

    $connection = get_connection();


    // Run the query on the database
    $result = $connection->query($sql);

    // Store the ONE result in an associative array
    $row = $result->fetch_assoc();

    $id = $row['rev_id'];
    $first = $row['rev_first_name'];
    $last = $row['rev_last_name'];
    $email = $row['rev_email'];
    $phone = $row['rev_phone_number'];
    $type = $row['rev_type'];
    $description = $row['rev_description'];
    $time = $row['rev_time'];
    $date = $row['rev_date'];
    $rating = $row['rev_rating'];


    $header = $first . " " . $last . "'s review:";
} else {
    $header = "*** NEW REVIEW ***";
    $id = "";
}
?>
<div class='detail'>
<h2><?php echo $header; ?></h2>

<form action="save.php" method="POST">
    <input type="hidden" class="form-control" name="id" id="id" value="<?php echo $id; ?>">

    <div class="mb-3">
        <label for="first_name" class="form-label">First Name</label>
        <input type="text" class="form-control" name="first" id="first" value="<?php echo $first; ?>">
    </div>

    <div class="mb-3">
        <label for="last_name" class="form-label">Last Name</label>
        <input type="text" class="form-control" name="last" id="last" value="<?php echo $last; ?>">
    </div>

    <div class="mb-3">
        <label for="rating" class="form-label">Rating</label>
        <input type="text" class="form-control" name="rating" id="rating" value="<?php echo $rating; ?>">
    </div>

    <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="text" class="form-control" name="email" id="email" value="<?php echo $email; ?>">
    </div>

    <div class="mb-3">
        <label for="duration" class="form-label">Phone Number</label>
        <input type="text" class="form-control" name="phone" id="phone" value="<?php echo $phone; ?>">
    </div>

    <div class="mb-3">
        <label for="type" class="form-label">Type of Canvas</label>
        <!-- <input type="select" class="form-control" name="type" value="<?php echo $type; ?>"> -->
         <select name="type" id="type">
            <option value="Cushion">Cushion</option>
            <option value="Bimini">Bimini</option>
            <option value="Repair">Repair</option>
        </select>
    </div>
    <div class="mb-3">
        <label for="time" class="form-label">Time Taken</label>
        <input type="text" class="form-control" name="time" id="time" value="<?php echo $time; ?>">
    </div>
    <div class="mb-3">
        <label for="date" class="form-label">Date Completed</label>
        <input type="text" class="form-control" name="date" id="date" value="<?php echo $date; ?>">
    </div>
    <div class="mb-3">
        <label for="description" class="form-label">Description</label>
        <input type="text" class="form-control" name="description" id="description" value="<?php echo $description; ?>">
    </div>
    <br>

    <button type="button" onclick="save()" class="save">Save</button>
    <?php 
    if ($id != "") { ?>
    <a href='delete.php?id=<?php echo $id; ?>' class='delete' role='button' >Delete</a>
    <?php }?>

    <a href="index.php?nav=review" class="cancel" role="button">Cancel</a>
</div>
</form>

<script>
    function save() {
        var settings = {
            'async': true,
            'url': 'save.php?id='           + $('#id').val() +
                            '&first='       + $('#first').val() + 
                            '&last='        + $('#last').val() +
                            '&rating='      + $('#rating').val() +
                            '&email='       + $('#email').val() +
                            '&phone='       + $('#phone').val() +
                            '&type='        + $('#type').val() + 
                            '&time='        + $('#time').val() +
                            '&date='        + $('#date').val() + 
                            '&description=' + $('#description').val(),
            'method': 'POST',
            'headers': {
                'Cache-Control': 'no-cache'
            }
        };

        $.ajax(settings).done(function(response) {
            // console.log(response);
            $('#results').html('Player saved successfully!');
            showAlert('success', 'Success!', 'Player saved successfully!');
            $('#results').removeClass('text-danger');
            $('#results').addClass('text-success');
        }).fail(function() {
            $('#results').html('Error saving player.');
            showAlert('danger', 'Error!', 'Error saving player.');
            $('#results').addClass('text-danger');
            $('#results').removeClass('text-success');
        })
    }



</script>