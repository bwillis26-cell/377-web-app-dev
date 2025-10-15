turn = true


function selectPiece(pieceID) {
    var color = pieceID.charAt(0)
    var xValue = $('#' + pieceID).attr('x');
    var yValue = $('#' + pieceID).attr('y');
    if (turn) {
        if (color == "b") {
            var turn = false;
        } else {
            console.log("Wrong piece or Not your turn! Select a different piece");
        }

    } else {
        if (color == "r") {
            turn = true;
        } else {
            console.log("Wrong piece or Not your turn! Select a different piece");
        }
    }
}

