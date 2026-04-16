from browser import document, html, svg
from browser.template import Template

boardArr = [[None for _ in range(8)] for _ in range(8)]

class Piece:

    def __init__(self, color, name, row, col):
        self.color = color
        self.name = name
        self.row = row
        self.col = col

    def get_color(self):
        return self.color
    def get_name(self):
        return self.name
    def get_position(self):
        return (self.row, self.col)

class Board:
    def __init__(self):
        self.pieces = []
        self.create_pieces()

    def create_pieces(self):
        # Create pawns
        for col in range(8):
            self.pieces.append(Piece("white", "pawn", 6, col))
            self.pieces.append(Piece("black", "pawn", 1, col))

        # Create rooks
        self.pieces.append(Piece("white", "rook", 7, 0))
        self.pieces.append(Piece("white", "rook", 7, 7))
        self.pieces.append(Piece("black", "rook", 0, 0))
        self.pieces.append(Piece("black", "rook", 0, 7))

        # Create knights
        self.pieces.append(Piece("white", "knight", 7, 1))
        self.pieces.append(Piece("white", "knight", 7, 6))
        self.pieces.append(Piece("black", "knight", 0, 1))
        self.pieces.append(Piece("black", "knight", 0, 6))

        # Create bishops
        self.pieces.append(Piece("white", "bishop", 7, 2))
        self.pieces.append(Piece("white", "bishop", 7, 5))
        self.pieces.append(Piece("black", "bishop", 0, 2))
        self.pieces.append(Piece("black", "bishop", 0, 5))

        # Create queens
        self.pieces.append(Piece("white", "queen", 7, 3))
        self.pieces.append(Piece("black", "queen", 0, 3))

        # Create kings
        self.pieces.append(Piece("white", "king", 7, 4))
        self.pieces.append(Piece("black", "king", 0, 4))

    def get_pieces(self):
        return self.pieces

def displayLegalMoves(id):
    global boardArr
    currPiece = None
    for row in boardArr:
        for piece in row:
            if piece is not None and id in document[piece.get_name() + piece.get_color()[0] + str(boardArr.index(row)) + str(row.index(piece))].id:
                currPiece = piece
                break
    if currPiece is not None:
        legalMoves = []
        if currPiece.get_name() == "pawn":
            direction = -1 if currPiece.get_color() == "white" else 1
            nextRow = currPiece.get_position()[0] + direction
            if 0 <= nextRow < 8 and boardArr[nextRow][currPiece.get_position()[1]] is None:
                legalMoves.append((nextRow, currPiece.get_position()[1]))
        elif currPiece.get_name() == "rook":
            for i in range(8):
                if i != currPiece.get_position()[0] and boardArr[i][currPiece.get_position()[1]] is None:
                    legalMoves.append((i, currPiece.get_position()[1]))
                if i != currPiece.get_position()[1] and boardArr[currPiece.get_position()[0]][i] is None:
                    legalMoves.append((currPiece.get_position()[0], i))
        elif currPiece.get_name() == "knight":
            knightMoves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
            for move in knightMoves:
                nextRow = currPiece.get_position()[0] + move[0]
                nextCol = currPiece.get_position()[1] + move[1]
                if 0 <= nextRow < 8 and 0 <= nextCol < 8 and boardArr[nextRow][nextCol] is None:
                    legalMoves.append((nextRow, nextCol))
        # Add logic for other pieces (bishop, queen, king) here

        for move in legalMoves:
            document["r" + str(move[0] * 8 + move[1])].style.display = "block"
    

def selectPiece(event, element):
    elementID = element.data.id
    displayLegalMoves(elementID)
    



wp = 0
bp = 0
wr = 0
br = 0
wn = 0
bn = 0
wq = 0
bq = 0
wb = 0
bb = 0
wk = 0
bk = 0

squareCount = 0



board = html.TABLE()

for row in range(8):
    tr = html.TR()
    tr.style.height = "50px"

    for col in range(8):
        td = html.TD()
        td.style.width = "50px"
        if (row + col) % 2 == 0:
            td.style.backgroundColor = "#e68a00"
        else:
            td.style.backgroundColor = "#ffd699"
        if (row, col) in [(piece.get_position()) for piece in Board().pieces]:
            piece = next(piece for piece in Board().pieces if piece.get_position() == (row, col))
            if (piece.get_name() == "pawn"):
                td.html = "<div id='pawnb" + str(bp) + "'><button class='pawnb' b-on='click:selectPiece'></button>" if piece.get_color() == "black" else "<div id='pawnw" + str(wp) + "'><button class='pawnw' b-on='click:selectPiece'></button>"
                
                boardArr[row][col] = piece
                bp += 1 if piece.get_color() == "black" else 0
                wp += 1 if piece.get_color() == "white" else 0
            elif (piece.get_name() == "rook"):
                td.html = "<div id='rookb" + str(br) + "'><button class='rookb' b-on='click:selectPiece'></button>" if piece.get_color() == "black" else "<div id='rookw" + str(wr) + "'><button class='rookw' b-on='click:selectPiece'></button>"
                boardArr[row][col] = piece
                br += 1 if piece.get_color() == "black" else 0
                wr += 1 if piece.get_color() == "white" else 0
            elif (piece.get_name() == "knight"):
                td.html = "<div id='knightb" + str(bn) + "'><button class='knightb' b-on='click:selectPiece'></button>" if piece.get_color() == "black" else "<div id='knightw" + str(wn) + "'><button class='knightw' b-on='click:selectPiece'></button>"
                boardArr[row][col] = piece
                bn += 1 if piece.get_color() == "black" else 0
                wn += 1 if piece.get_color() == "white" else 0
            elif (piece.get_name() == "queen"):
                td.html = "<div id='queenb" + str(bq) + "'><button class='queenb' b-on='click:selectPiece'></button>" if piece.get_color() == "black" else "<div id='queenw" + str(wq) + "'><button class='queenw' b-on='click:selectPiece'></button>"
                boardArr[row][col] = piece
                # td.html = "<img src='chess-svg/queen-b.svg' width=40 height=40 id='queenb" + str(bq) + "'>" if piece.get_color() == "black" else "<img src='chess-svg/queen-w.svg' width=40 height=40 id='queenw" + str(wq) + "'>"
                # document["queenb" + str(bq)].bind("click", selectPiece("queenb" + str(bq))) if piece.get_color() == "black" else document["queenw" + str(wq)].bind("click", selectPiece("queenw" + str(wq)))
                bq += 1 if piece.get_color() == "black" else 0
                wq += 1 if piece.get_color() == "white" else 0
            elif (piece.get_name() == "king"):
                td.html = "<div id='kingb" + str(bk) + "'><button class='kingb' b-on='click:selectPiece'></button>" if piece.get_color() == "black" else "<div id='kingw" + str(wk) + "'><button class='kingw' b-on='click:selectPiece'></button>"
                boardArr[row][col] = piece
                bk += 1 if piece.get_color() == "black" else 0
                wk += 1 if piece.get_color() == "white" else 0
            elif (piece.get_name() == "bishop"):
                td.html = "<div id='bishopb" + str(bb) + "'><button class='bishopb' b-on='click:selectPiece'></button>" if piece.get_color() == "black" else "<div id='bishopw" + str(wb) + "'><button class='bishopw' b-on='click:selectPiece'></button>"
                boardArr[row][col] = piece
                bb += 1 if piece.get_color() == "black" else 0
                wb += 1 if piece.get_color() == "white" else 0
            else:
                td.html = "<div>"
                boardArr[row][col] = None
        else:
            td.html = ""
            boardArr[row][col] = None
        # td.html = "<circle cx='25' cy='25' r='20' fill='red' id='r" + str(squareCount) + "' style='display:none;' ></circle>" + td.html 
        td.html =  td.html + "<svg width='50' height='50' style='display:none; id='r" + str(squareCount) + "'><circle cx='25' cy='25' r='10' fill='red' ></circle></svg></div>"    
   
        squareCount += 1

        tr <= td
    board <= tr
document <= board

# document["rookb0"].bind("click", selectPiece("rookb0"))
# document["rookb1"].bind("click", selectPiece("rookb1"))
# document["rookw0"].bind("click", selectPiece("rookw0"))
# document["rookw1"].bind("click", selectPiece("rookw1"))
# document["knightb0"].bind("click", selectPiece("knightb0"))
# document["knightb1"].bind("click", selectPiece("knightb1"))
# document["knightw0"].bind("click", selectPiece("knightw0"))
# document["knightw1"].bind("click", selectPiece("knightw1"))
# document["bishopb0"].bind("click", selectPiece("bishopb0"))
# document["bishopb1"].bind("click", selectPiece("bishopb1"))
# document["bishopw0"].bind("click", selectPiece("bishopw0"))
# document["bishopw1"].bind("click", selectPiece("bishopw1"))
# document["queenb0"].bind("click", selectPiece("queenb0"))
# document["queenw0"].bind("click", selectPiece("queenw0"))
# document["kingb0"].bind("click", selectPiece("kingb0"))
# document["kingw0"].bind("click", selectPiece("kingw0"))
# for i in range(8):
#     document["pawnb" + str(i)].bind("click", selectPiece("pawnb" + str(i)))
#     document["pawnw" + str(i)].bind("click", selectPiece("pawnw" + str(i)))


for i in range(2):
    Template("rookb" + str(i), [selectPiece]).render(id="rookb" + str(i))
    Template("rookw" + str(i), [selectPiece]).render(id="rookw" + str(i))
    Template("knightb" + str(i), [selectPiece]).render(id="knightb" + str(i))
    Template("knightw" + str(i), [selectPiece]).render(id="knightw" + str(i))
    Template("bishopb" + str(i), [selectPiece]).render(id="bishopb" + str(i))
    Template("bishopw" + str(i), [selectPiece]).render(id="bishopw" + str(i))

Template("queenb0", [selectPiece]).render(id="queenb0")
Template("queenw0", [selectPiece]).render(id="queenw0")
Template("kingb0", [selectPiece]).render(id="kingb0")
Template("kingw0", [selectPiece]).render(id="kingw0")
for i in range(8):
    Template("pawnb" + str(i), [selectPiece]).render(id="pawnb" + str(i))
    Template("pawnw" + str(i), [selectPiece]).render(id="pawnw" + str(i))
