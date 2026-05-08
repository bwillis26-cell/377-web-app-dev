<?php

$id = "";
$username = "";
$password = "";
$date = "";
$elo = "";
$totalGames = "";


?>

<div class='detail'>
<h2 id="header">Login Here</h2>

<form action="save-login.php" method="POST">
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

    <button type="button" onclick="saveLogin()" class="save">Save</button>
</div>
</form>

<script>
    function saveLogin() {
        var settings = {
            'async': true,
            'url': 'save-login.php?id='           + $('#id').val() +
                            '&username='    + $('#username').val() + 
                            '&password='    + $('#password').val(),
            'method': 'POST',
            'headers': {
                'Cache-Control': 'no-cache'
            }
        };

        $.ajax(settings).done(function(response) {
            console.log(response);
            showAlert('success', 'Success!', 'Successfully logged in.');
            if ($('#id').val() == "") {
                $('#id').val(response);
            }
            }).fail(function() {
            showAlert('danger', 'Error!', 'Error logging in. Username or password may be incorrect.');
        })
        // Redirect to chess game page after successful login
        .done(function() {
            window.location.href = "http://localhost/webappdev/11-final-project/web/index.php?nav=game";
        });
    }



</script>



