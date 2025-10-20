var turn = true
var selectedPiece = ""
var pieceSelected = false
var xValue = 0
var yValue = 0
const SVGTOPMARGIN = 100
const SVGLEFTMARGIN = 20

var board = [['x', 'r', 'x', 'r', 'x', 'r', 'x', 'r'], 
            ['r', 'x', 'r', 'x', 'r', 'x', 'r', 'x'], 
            ['x', 'r', 'x', 'r', 'x', 'r', 'x', 'r'], 
            [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'], 
            ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '], 
            ['b', 'x', 'b', 'x', 'b', 'x', 'b', 'x'], 
            ['x', 'b', 'x', 'b', 'x', 'b', 'x', 'b'], 
            ['b', 'x', 'b', 'x', 'b', 'x', 'b', 'x']];
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

    var color = selectedPiece.charAt(0);
    var pieceX = $('#' + selectedPiece).attr('cx');
    var pieceY = $('#' + selectedPiece).attr('cy');
    
    var currentSquareX = Math.ceil((e.pageX - SVGLEFTMARGIN) / 60);
    var currentSquareY = Math.ceil((e.pageY - SVGTOPMARGIN) / 60);
    
    var circleX = (currentSquareX * 60) - 20;
    var circleY = (currentSquareY * 60) - 20;
    
    if (pieceSelected) { 
        if () { 
            
        }
    // $('#' + selectedPiece).attr({ 'cx': circleX, 'cy': circleY});
    // pieceSelected = false;

    }
}

