<?php

$id = "";
$username = "";
$password = "";
$date = "";
$elo = "";
$totalGames = "";

?>

<div class='detail'>
<h2 id="header">Register Here</h2>

<form action="save-register.php" method="POST">
    <input type="hidden" class="form-control" name="id" id="id" value="<?php echo $id; ?>">

    <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" class="form-control" name="username" id="username" value="<?php echo $username; ?>">
    </div>

    <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" class="form-control" name="password" id="password" value="<?php echo $password; ?>">
    </div>

    <br>

    <button type="button" onclick="save()" class="save">Save</button>
</div>
</form>

<script>
    function save() {
        var settings = {
            'async': true,
            'url': 'save.php?id='           + $('#id').val() +
                            '&username='    + $('#username').val() + 
                            '&password='    + $('#password').val() +
                            '&date='        + $('#date').val() +
                            '&elo='         + $('#elo').val() +
                            '&totalGames='  + $('#totalGames').val(),
            'method': 'POST',
            'headers': {
                'Cache-Control': 'no-cache'
            }
        };

        $.ajax(settings).done(function(response) {
            console.log(response);
            showAlert('success', 'Success!', 'Player saved successfully!');
            if ($('#id').val() == "") {
                $('#id').val(response);
            }
            }).fail(function() {
            showAlert('danger', 'Error!', 'Error saving player.');
        })
    }



</script>