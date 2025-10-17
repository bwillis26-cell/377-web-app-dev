var turn = true
var selectedPiece = ""
var pieceSelected = false
var xValue = 0
var yValue = 0
const SVGTOPMARGIN = 100
const SVGLEFTMARGIN = 20
$(document).ready(function() {
  // Your code here will run after the DOM is ready
  $(".squareOdd").click(movePiece);

});

var mouseX, mouseY;
$(document).mousemove(function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
}).mouseover();

function selectPiece(pieceID) {
    selectedPiece = pieceID;
    var color = pieceID.charAt(0)
    xValue = $('#' + pieceID).attr('cx');
    yValue = $('#' + pieceID).attr('cy');
    if (turn) {
        if (color == "b") {
            turn = false;
            pieceSelected = true;

        } else {
            console.log("Wrong piece or Not your turn! Select a different piece");
        }

    } else {
        if (color == "r") {
            turn = true;
            pieceSelected = true;

        } else {
            console.log("Wrong piece or Not your turn! Select a different piece");
        }
    }
}

function movePiece(e) {
    console.log(e);
    var color = selectedPiece.charAt(0);
    console.log("Current MouseX: " + mouseX + " Current MouseY: " + mouseY);
    var currentX = Math.ceil((e.pageX - SVGLEFTMARGIN) / 60);
    var currentY = Math.ceil((e.pageY - SVGTOPMARGIN) / 60);
    console.log("Square Mouse X: " + currentX + " Square Mouse Y: " + currentY);
    


    
}

