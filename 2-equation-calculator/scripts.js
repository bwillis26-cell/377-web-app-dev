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

function calculateGeometric(){
    var startingval = $('#geoStart').val();
    var endingval = $('#geoEnd').val();
    var increment = $('#increment').val();

    var sequenceLength = (endingval - startingval)/increment + 1

    var total = startingval * (1 - increment**sequenceLength)/(1-increment)

    $('#total').html('The sum is ' + total);

}