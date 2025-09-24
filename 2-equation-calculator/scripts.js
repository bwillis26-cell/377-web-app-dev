function calculateAccel(){
    var initialV = $('#vi').val();
    var finalV = $('#vf').val();
    var time = $('#timeA').val();

    var accel = (finalV - initialV)/time

    $('#accel').html(accel + 'm/s&sup2;');
}

function calculateVelocity(){
    var startingD = $('#di').val();
    var endingD = $('#df').val();
    var time = $('#timeV').val();

    var velocity = (endingD - startingD)/time

    $('#velocity').html(velocity + 'm/s')


}