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
    def move_piece(self, piece, new_row, new_col):
        piece.row = new_row
        piece.col = new_col

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
                td.html = "<img src='chess-svg/bpawn2-b.svg' width=40 height=40>" if piece.get_color() == "black" else "<img src='chess-svg/bpawn2-w.svg' width=40 height=40>"
            elif (piece.get_name() == "rook"):
                td.html = "<img src='chess-svg/rook-b.svg' width=40 height=40>" if piece.get_color() == "black" else "<img src='chess-svg/rook-w.svg' width=40 height=40>"
            elif (piece.get_name() == "knight"):
                td.html = "<img src='chess-svg/knight-b.svg' width=40 height=40>" if piece.get_color() == "black" else "<img src='chess-svg/knight-w.svg' width=40 height=40>"
            elif (piece.get_name() == "queen"):
                td.html = "<img src='chess-svg/queen-b.svg' width=40 height=40>" if piece.get_color() == "black" else "<img src='chess-svg/queen-w.svg' width=40 height=40>"
            elif (piece.get_name() == "king"):
                td.html = "<img src='chess-svg/nrking-b.svg' width=40 height=40>" if piece.get_color() == "black" else "<img src='chess-svg/nrking-w.svg' width=40 height=40>"
            elif (piece.get_name() == "bishop"):
                td.html = "<img src='chess-svg/bishop-b.svg' width=40 height=40>" if piece.get_color() == "black" else "<img src='chess-svg/bishop-w.svg' width=40 height=40>"
            else:
                td.text = ""
        # if (row, col) in [(piece.get_position()) for piece in Board().pieces]:
        #     piece = next(piece for piece in Board().pieces if piece.get_position() == (row, col))
        #     if (piece.get_name() == "knight"):
        #         td.text = "N" if piece.get_color() == "white" else "n"
        #     elif (piece.get_name() == "king"):
        #         td.svg = html.SVG(width=40, height=40)
        #     else:
        #         td.text = ""
        
        tr <= td
    board <= tr
document <= board