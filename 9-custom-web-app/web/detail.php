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
    <input type="hidden" class="form-control" name="id" value="<?php echo $id; ?>">

    <div class="mb-3">
        <label for="first_name" class="form-label">First Name</label>
        <input type="text" class="form-control" name="first" value="<?php echo $first; ?>">
    </div>

    <div class="mb-3">
        <label for="last_name" class="form-label">Last Name</label>
        <input type="text" class="form-control" name="last" value="<?php echo $last; ?>">
    </div>

    <div class="mb-3">
        <label for="rating" class="form-label">Rating</label>
        <input type="text" class="form-control" name="rating" value="<?php echo $rating; ?>">
    </div>

    <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="text" class="form-control" name="email" value="<?php echo $email; ?>">
    </div>

    <div class="mb-3">
        <label for="duration" class="form-label">Phone Number</label>
        <input type="text" class="form-control" name="phone" value="<?php echo $phone; ?>">
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
        <input type="text" class="form-control" name="time" value="<?php echo $time; ?>">
    </div>
    <div class="mb-3">
        <label for="date" class="form-label">Date Completed</label>
        <input type="text" class="form-control" name="date" value="<?php echo $date; ?>">
    </div>
    <div class="mb-3">
        <label for="description" class="form-label">Description</label>
        <input type="text" class="form-control" name="description" value="<?php echo $description; ?>">
    </div>
    <br>

    <button type="submit" onclick="save()" class="save">Save</button>
    <?php 
    if ($id != "") { ?>
    <a href='delete.php?id=<?php echo $id; ?>' class='delete' role='button' >Delete</a>
    <?php }?>

    <a href="index.php?nav=review" class="cancel" role="button">Cancel</a>
</div>
</form>

<script>
    function save() {
        
    }



</script>