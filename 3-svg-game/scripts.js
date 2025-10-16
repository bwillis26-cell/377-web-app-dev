var turn = true
var selectedPiece = ""
var pieceSelected = false
var xValue = 0
var yValue = 0
$(document).ready(function() {
  // Your code here will run after the DOM is ready
  $("#squareOdd").click(movePiece);

});

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

function movePiece() {
    var color = selectedPiece.charAt(0);
    if ()
}

