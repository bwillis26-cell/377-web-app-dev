var turn = true
var selectedPiece = ""
var pieceSelected = false

const SVGTOPMARGIN = 100
const SVGLEFTMARGIN = 20

var pieceX = 0;
var pieceY = 0;

var board = [['x', 'r1', 'x', 'r2', 'x', 'r3', 'x', 'r4'], 
            ['r5', 'x', 'r6', 'x', 'r7', 'x', 'r8', 'x'], 
            ['x', 'r9', 'x', 'r10', 'x', 'r11', 'x', 'r12'], 
            ['', 'x', '', 'x', '', 'x', '', 'x'], 
            ['x', '', 'x', '', 'x', '', 'x', ''], 
            ['b1', 'x', 'b2', 'x', 'b3', 'x', 'b4', 'x'], 
            ['x', 'b5', 'x', 'b6', 'x', 'b7', 'x', 'b8'], 
            ['b9', 'x', 'b10', 'x', 'b11', 'x', 'b12', 'x']];
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
            
            pieceSelected = true;

        } else {
            console.log("Wrong piece or Not your turn! Select a different piece");
        }

    } else {
        if (color == "r") {
            
            pieceSelected = true;

        } else {
            console.log("Wrong piece or Not your turn! Select a different piece");
        }
    }
}

function movePiece(e) {


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

    var currentColor = previousSpot[0];
    var nextColor = boardSpot[0];

    
    if (pieceSelected) {
        if (boardSpot == '') { 
            if (previousPieceX + 1 == currentSquareX || previousPieceX - 1 == currentSquareX) {
                if (currentColor == 'b' && previousPieceY - 1 == currentSquareY)  {
                    $('#' + selectedPiece).attr({ 'cx': circleX, 'cy': circleY});
                    boardRow[currentSquareX - 1] = previousSpot;
                    board[currentSquareY - 1] = boardRow;
                    turn = false;

                    previousRow[previousPieceX - 1] = '';
                    board[previousPieceY - 1] = previousRow;

                } else if (currentColor == 'r' && previousPieceY + 1 == currentSquareY) {
                    $('#' + selectedPiece).attr({ 'cx': circleX, 'cy': circleY});
                    boardRow[currentSquareX - 1] = previousSpot;
                    board[currentSquareY - 1] = boardRow;
                    turn = true;

                    previousRow[previousPieceX - 1] = '';
                    board[previousPieceY - 1] = previousRow;
                }
                pieceSelected = false;
            }
        } else if ((turn) && (boardSpot[0] == 'r') && (currentSquareX != 1 && currentSquareX != 8) && (currentSquareY != 1 && currentSquareY != 8)) {
            if (previousPieceY < currentSquareY) {
                var nextBoardRow = board[currentSquareY];
                circleY += 60;
                if (previousPieceX < currentSquareX) {
                    var nextBoardSpot = nextBoardRow[currentSquareX];
                    circleX += 60;
                    if (nextBoardSpot == '') { 
                        $('#' + selectedPiece).attr({ 'cx': circleX, 'cy': circleY});
                        pieceSelected = false;
                        boardRow[currentSquareX - 1] = '';
                        board[currentSquareY - 1] = boardRow;
                        turn = false;

                        previousRow[previousPieceX - 1] = '';
                        board[previousPieceY - 1] = previousRow;

                        nextBoardRow[currentSquareX] = previousSpot;
                        board[currentSquareY] = nextBoardRow;

                        $('#' + boardSpot).css('visibility', 'hidden');
                    } else {
                        console.log("You can't take that piece!")
                    }
                } else if (previousPieceX > currentSquareX) {
                    var nextBoardSpot = nextBoardRow[currentSquareX - 2];
                    circleX -= 60;
                    if (nextBoardSpot == '') { 
                        $('#' + selectedPiece).attr({ 'cx': circleX, 'cy': circleY});
                        pieceSelected = false;
                        boardRow[currentSquareX - 1] = '';
                        board[currentSquareY - 1] = boardRow;
                        turn = false;

                        previousRow[previousPieceX - 1] = '';
                        board[previousPieceY - 1] = previousRow;

                        nextBoardRow[currentSquareX - 2] = previousSpot;
                        board[currentSquareY] = nextBoardRow;

                        $('#' + boardSpot).css('visibility', 'hidden');
                    } else {
                        console.log("You can't take that piece!")
                    }
                }
            } else if (previousPieceY > currentSquareY) {
                var nextBoardRow = board[currentSquareY - 2];
                circleY -= 60;
                if (previousPieceX < currentSquareX) {
                    var nextBoardSpot = nextBoardRow[currentSquareX];
                    circleX += 60;
                    if (nextBoardSpot == '') { 
                        $('#' + selectedPiece).attr({ 'cx': circleX, 'cy': circleY});
                        pieceSelected = false;
                        boardRow[currentSquareX - 1] = '';
                        board[currentSquareY - 1] = boardRow;
                        turn = false;

                        previousRow[previousPieceX - 1] = '';
                        board[previousPieceY - 1] = previousRow;

                        nextBoardRow[currentSquareX] = previousSpot;
                        board[currentSquareY - 2] = nextBoardRow;

                        $('#' + boardSpot).css('visibility', 'hidden');
                    } else {
                        console.log("You can't take that piece!")
                    }
                } else if (previousPieceX > currentSquareX) {
                    var nextBoardSpot = nextBoardRow[currentSquareX - 2];
                    circleX -= 60;
                    if (nextBoardSpot == '') { 
                        $('#' + selectedPiece).attr({ 'cx': circleX, 'cy': circleY});
                        pieceSelected = false;
                        boardRow[currentSquareX - 1] = '';
                        board[currentSquareY - 1] = boardRow;
                        turn = false;

                        previousRow[previousPieceX - 1] = '';
                        board[previousPieceY - 1] = previousRow;

                        nextBoardRow[currentSquareX - 2] = previousSpot;
                        board[currentSquareY - 2] = nextBoardRow;

                        $('#' + boardSpot).css('visibility', 'hidden');
                    } else {
                        console.log("You can't take that piece!")
                    }
                }
            
            }
        } else if ((!turn) && (boardSpot[0] == 'b') && (currentSquareX != 1 && currentSquareX != 8) && (currentSquareY != 1 && currentSquareY != 8)) {
            if (previousPieceY < currentSquareY) {
                var nextBoardRow = board[currentSquareY];
                circleY += 60;
                if (previousPieceX < currentSquareX) {
                    var nextBoardSpot = nextBoardRow[currentSquareX];
                    circleX += 60;
                    if (nextBoardSpot == '') { 
                        $('#' + selectedPiece).attr({ 'cx': circleX, 'cy': circleY});
                        pieceSelected = false;
                        boardRow[currentSquareX - 1] = '';
                        board[currentSquareY - 1] = boardRow;
                        turn = true;

                        previousRow[previousPieceX - 1] = '';
                        board[previousPieceY - 1] = previousRow;

                        nextBoardRow[currentSquareX] = previousSpot;
                        board[currentSquareY] = nextBoardRow;

                        $('#' + boardSpot).css('visibility', 'hidden');
                    } else {
                        console.log("You can't take that piece!")
                    }
                } else if (previousPieceX > currentSquareX) {
                    var nextBoardSpot = nextBoardRow[currentSquareX - 2];
                    circleX -= 60;
                    if (nextBoardSpot == '') { 
                        $('#' + selectedPiece).attr({ 'cx': circleX, 'cy': circleY});
                        pieceSelected = false;
                        boardRow[currentSquareX - 1] = '';
                        board[currentSquareY - 1] = boardRow;
                        turn = true;

                        previousRow[previousPieceX - 1] = '';
                        board[previousPieceY - 1] = previousRow;

                        nextBoardRow[currentSquareX - 2] = previousSpot;
                        board[currentSquareY] = nextBoardRow;

                        $('#' + boardSpot).css('visibility', 'hidden');
                    } else {
                        console.log("You can't take that piece!")
                    }
                }
            } else if (previousPieceY > currentSquareY) {
                var nextBoardRow = board[currentSquareY - 2];
                circleY -= 60;
                if (previousPieceX < currentSquareX) {
                    var nextBoardSpot = nextBoardRow[currentSquareX];
                    circleX += 60;
                    if (nextBoardSpot == '') { 
                        $('#' + selectedPiece).attr({ 'cx': circleX, 'cy': circleY});
                        pieceSelected = false;
                        boardRow[currentSquareX - 1] = '';
                        board[currentSquareY - 1] = boardRow;
                        turn = true;

                        previousRow[previousPieceX - 1] = '';
                        board[previousPieceY - 1] = previousRow;

                        nextBoardRow[currentSquareX] = previousSpot;
                        board[currentSquareY - 2] = nextBoardRow;

                        $('#' + boardSpot).css('visibility', 'hidden');
                    } else {
                        console.log("You can't take that piece!")
                    }
                } else if (previousPieceX > currentSquareX) {
                    var nextBoardSpot = nextBoardRow[currentSquareX - 2];
                    circleX -= 60;
                    if (nextBoardSpot == '') { 
                        $('#' + selectedPiece).attr({ 'cx': circleX, 'cy': circleY});
                        pieceSelected = false;
                        boardRow[currentSquareX - 1] = '';
                        board[currentSquareY - 1] = boardRow;
                        turn = true;

                        previousRow[previousPieceX - 1] = '';
                        board[previousPieceY - 1] = previousRow;

                        nextBoardRow[currentSquareX - 2] = previousSpot;
                        board[currentSquareY - 2] = nextBoardRow;

                        $('#' + boardSpot).css('visibility', 'hidden');
                    } else {
                        console.log("You can't take that piece!")
                }
            }
            
            }
        }
    }
}
