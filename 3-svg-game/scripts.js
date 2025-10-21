var turn = true
var selectedPiece = ""
var pieceSelected = false

const SVGTOPMARGIN = 100
const SVGLEFTMARGIN = 20

var pieceX = 0;
var pieceY = 0;

var board = [['x', 'r', 'x', 'r', 'x', 'r', 'x', 'r'], 
            ['r', 'x', 'r', 'x', 'r', 'x', 'r', 'x'], 
            ['x', 'r', 'x', 'r', 'x', 'r', 'x', 'r'], 
            ['', 'x', '', 'x', '', 'x', '', 'x'], 
            ['x', '', 'x', '', 'x', '', 'x', ''], 
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
    pieceX = $('#' + pieceID).attr('cx');
    pieceY = $('#' + pieceID).attr('cy');
    
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
    
    var previousPieceX = Math.ceil((pieceX - 20) / 60)
    var previousPieceY = Math.ceil((pieceY - 20) / 60)
    
    var currentSquareX = Math.ceil((e.pageX - SVGLEFTMARGIN) / 60);
    var currentSquareY = Math.ceil((e.pageY - SVGTOPMARGIN) / 60);
    
    var circleX = (currentSquareX * 60) - 20;
    var circleY = (currentSquareY * 60) - 20;
    
    var previousRow = board[previousPieceY - 1];
    var previousSpot = previousRow[previousPieceX - 1];

    var boardRow = board[currentSquareY - 1];
    var boardSpot = boardRow[currentSquareX - 1];
    if (pieceSelected) {
        if (boardSpot == '') { 
            if (previousPieceX + 1 == currentSquareX || previousPieceX - 1 == currentSquareX) {
                if (previousSpot == 'b' && previousPieceY - 1 == currentSquareY)  {
                    $('#' + selectedPiece).attr({ 'cx': circleX, 'cy': circleY});
                    pieceSelected = false;
                    boardRow[currentSquareX - 1] = previousSpot;
                    board[currentSquareY - 1] = boardRow;

                    previousRow[previousPieceX - 1] = '';
                    board[previousPieceY - 1] = previousRow;

                } else if (previousSpot == 'r' && previousPieceY + 1 == currentSquareY) {
                    $('#' + selectedPiece).attr({ 'cx': circleX, 'cy': circleY});
                    pieceSelected = false;
                    boardRow[currentSquareX - 1] = previousSpot;
                    board[currentSquareY - 1] = boardRow;

                    previousRow[previousPieceX - 1] = '';
                    board[previousPieceY - 1] = previousRow;

                } else if (previousSpot == 'bk' || previousSpot == 'rk') {
                    $('#' + selectedPiece).attr({ 'cx': circleX, 'cy': circleY});
                    pieceSelected = false;
                    boardRow[currentSquareX - 1] = previousSpot;
                    board[currentSquareY - 1] = boardRow;

                    previousRow[previousPieceX - 1] = '';
                    board[previousPieceY - 1] = previousRow;

                }
            }
        } else if ((turn) && (boardSpot[0] == 'r') && (currentSquareX != 1 && currentSquareX != 8) && (currentSquareY != 1 && currentSquareY != 8)) {
            if (previousPieceX < currentSquareX) {
                circleX += 60
            } 
        }
    }
}
