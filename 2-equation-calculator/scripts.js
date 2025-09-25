function calculateAccel(){
    var initialV = $('#vi').val();
    var finalV = $('#vf').val();
    var time = $('#timeA').val();

    var accel = (finalV - initialV)/time
    accel = Math.round((accel + Number.EPSILON) * 100) / 100

    $('#accel').html(accel + 'm/s&sup2;');
}

function calculateVelocity(){
    var startingD = $('#di').val();
    var endingD = $('#df').val();
    var time = $('#timeV').val();

    var velocity = Math.round((endingD - startingD)/time)
    velocity =  Math.round((velocity + Number.EPSILON) * 100) / 100

    $('#velocity').html(velocity + 'm/s')


}

function calculateGeometric(){
    var startingVal = $('#geoStart').val();
    var endingVal = $('#geoEnd').val();
    var increment = $('#increment').val();

    var tempEndVal = endingVal
    var sequenceLength = 1
    while (tempEndVal != startingVal){
        tempEndVal = tempEndVal / startingVal
        sequenceLength += 1
    }

    var total = startingVal * (1 - increment**sequenceLength)/(1-increment)

    $('#total').html('The sum is ' + total);

}