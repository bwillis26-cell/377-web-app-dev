from browser import document, html, svg

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

def selectPiece(piece_id):
    color = ""
    if piece_id.endswith("w"):
        color = "white"
    else:
        color = "black"
    name = piece_id[:-1]
    print(f"Selected piece: {color} {name}")



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
                td.html = "<button class='pawnb' id='pawnb" + str(bp) + "'>" if piece.get_color() == "black" else "<button class='pawnw' id='pawnw" + str(wp) + "'>"
                # td.html = "<img src='chess-svg/bpawn2-b.svg' width=40 height=40 id='pawnb" + str(bp) + "'>" if piece.get_color() == "black" else "<img src='chess-svg/bpawn2-w.svg' width=40 height=40 id='pawnw" + str(wp) + "'>"
                # document["pawnb" + str(bp)].bind("click", selectPiece("pawnb" + str(bp))) if piece.get_color() == "black" else document["pawnw" + str(wp)].bind("click", selectPiece("pawnw" + str(wp)))
                bp += 1 if piece.get_color() == "black" else 0
                wp += 1 if piece.get_color() == "white" else 0
            elif (piece.get_name() == "rook"):
                td.html = "<button class='rookb' id='rookb" + str(br) + "'>" if piece.get_color() == "black" else "<button class='rookw' id='rookw" + str(wr) + "'>"
                # td.html = "<img src='chess-svg/rook-b.svg' width=40 height=40 id='rookb" + str(br) + "'>" if piece.get_color() == "black" else "<img src='chess-svg/rook-w.svg' width=40 height=40 id='rookw" + str(wr) + "'>"
                # document["rookb" + str(br)].bind("click", selectPiece("rookb" + str(br))) if piece.get_color() == "black" else document["rookw" + str(wr)].bind("click", selectPiece("rookw" + str(wr)))
                br += 1 if piece.get_color() == "black" else 0
                wr += 1 if piece.get_color() == "white" else 0
            elif (piece.get_name() == "knight"):
                td.html = "<button class='knightb' id='knightb" + str(bn) + "'>" if piece.get_color() == "black" else "<button class='knightw' id='knightw" + str(wn) + "'>"
                # td.html = "<img src='chess-svg/knight-b.svg' width=40 height=40 id='knightb" + str(bn) + "'>" if piece.get_color() == "black" else "<img src='chess-svg/knight-w.svg' width=40 height=40 id='knightw" + str(wn) + "'>"
                # document["knightb" + str(bn)].bind("click", selectPiece("knightb" + str(bn))) if piece.get_color() == "black" else document["knightw" + str(wn)].bind("click", selectPiece("knightw" + str(wn)))
                bn += 1 if piece.get_color() == "black" else 0
                wn += 1 if piece.get_color() == "white" else 0
            elif (piece.get_name() == "queen"):
                td.html = "<button class='queenb' id='queenb" + str(bq) + "'>" if piece.get_color() == "black" else "<button class='queenw' id='queenw" + str(wq) + "'>"
                # td.html = "<img src='chess-svg/queen-b.svg' width=40 height=40 id='queenb" + str(bq) + "'>" if piece.get_color() == "black" else "<img src='chess-svg/queen-w.svg' width=40 height=40 id='queenw" + str(wq) + "'>"
                # document["queenb" + str(bq)].bind("click", selectPiece("queenb" + str(bq))) if piece.get_color() == "black" else document["queenw" + str(wq)].bind("click", selectPiece("queenw" + str(wq)))
                bq += 1 if piece.get_color() == "black" else 0
                wq += 1 if piece.get_color() == "white" else 0
            elif (piece.get_name() == "king"):
                td.html = "<button class='kingb' id='kingb" + str(bk) + "'>" if piece.get_color() == "black" else "<button class='kingw' id='kingw" + str(wk) + "'>"
                # td.html = "<img src='chess-svg/nrking-b.svg' width=40 height=40 id='kingb" + str(bk) + "'>" if piece.get_color() == "black" else "<img src='chess-svg/nrking-w.svg' width=40 height=40 id='kingw" + str(wk) + "'>"
                # document["kingb" + str(bk)].bind("click", selectPiece("kingb" + str(bk))) if piece.get_color() == "black" else document["kingw" + str(wk)].bind("click", selectPiece("kingw" + str(wk)))
                bk += 1 if piece.get_color() == "black" else 0
                wk += 1 if piece.get_color() == "white" else 0
            elif (piece.get_name() == "bishop"):
                td.html = "<button class='bishopb' id='bishopb" + str(bb) + "'>" if piece.get_color() == "black" else "<button class='bishopw' id='bishopw" + str(wb) + "'>"
                # td.html = "<img src='chess-svg/bishop-b.svg' width=40 height=40 id='bishopb" + str(bb) + "'>" if piece.get_color() == "black" else "<img src='chess-svg/bishop-w.svg' width=40 height=40 id='bishopw" + str(wb) + "'>"
                # document["bishopb" + str(bb)].bind("click", selectPiece("bishopb" + str(bb))) if piece.get_color() == "black" else document["bishopw" + str(wb)].bind("click", selectPiece("bishopw" + str(wb)))
                bb += 1 if piece.get_color() == "black" else 0
                wb += 1 if piece.get_color() == "white" else 0
            else:
                td.text = ""
            
        
        tr <= td
    board <= tr
document <= board

document["rookb0"].bind("click", selectPiece("rookb0"))
document["rookb1"].bind("click", selectPiece("rookb1"))
document["rookw0"].bind("click", selectPiece("rookw0"))
document["rookw1"].bind("click", selectPiece("rookw1"))
document["knightb0"].bind("click", selectPiece("knightb0"))
document["knightb1"].bind("click", selectPiece("knightb1"))
document["knightw0"].bind("click", selectPiece("knightw0"))
document["knightw1"].bind("click", selectPiece("knightw1"))
document["bishopb0"].bind("click", selectPiece("bishopb0"))
document["bishopb1"].bind("click", selectPiece("bishopb1"))
document["bishopw0"].bind("click", selectPiece("bishopw0"))
document["bishopw1"].bind("click", selectPiece("bishopw1"))
document["queenb0"].bind("click", selectPiece("queenb0"))
document["queenw0"].bind("click", selectPiece("queenw0"))
document["kingb0"].bind("click", selectPiece("kingb0"))
document["kingw0"].bind("click", selectPiece("kingw0"))
for i in range(8):
    document["pawnb" + str(i)].bind("click", selectPiece("pawnb" + str(i)))
    document["pawnw" + str(i)].bind("click", selectPiece("pawnw" + str(i)))