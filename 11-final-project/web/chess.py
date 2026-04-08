from browser import document, html

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
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        # Set up pawns
        for col in range(8):
            self.board[1][col] = Piece('black', 'pawn', 1, col)
            self.board[6][col] = Piece('white', 'pawn', 6, col)

        # Set up rooks
        self.board[0][0] = self.board[0][7] = Piece('black', 'rook', 0, 0)
        self.board[7][0] = self.board[7][7] = Piece('white', 'rook', 7, 0)

        # Set up knights
        self.board[0][1] = self.board[0][6] = Piece('black', 'knight', 0, 1)
        self.board[7][1] = self.board[7][6] = Piece('white', 'knight', 7, 1)

        # Set up bishops
        self.board[0][2] = self.board[0][5] = Piece('black', 'bishop', 0, 2)
        self.board[7][2] = self.board[7][5] = Piece('white', 'bishop', 7, 2)

        # Set up queens
        self.board[0][3] = Piece('black', 'queen', 0, 3)
        self.board[7][3] = Piece('white', 'queen', 7, 3)

        # Set up kings
        self.board[0][4] = Piece('black', 'king', 0, 4)
        self.board[7][4] = Piece('white', 'king', 7, 4)

    def __str__(self):
        board_str = ""
        for row in self.board:
            for piece in row:
                if piece is None:
                    board_str += ". "
                elif piece.color == 'white':
                    board_str += piece.name[0].upper() + " "
                else:
                    board_str += piece.name[0].lower() + " "
            board_str += "\n"
        return board_str
    
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.board[from_row][from_col]
        if piece is None:
            print("No piece at the source position.")
            return False
        if self.board[to_row][to_col] is not None:
            print("Destination position is occupied.")
            return False
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = None
        piece.row = to_row
        piece.col = to_col
        return True
    
    def is_valid_move(self, from_row, from_col, to_row, to_col):
        piece = self.board[from_row][from_col]
        if piece is None:
            return False
        # Implement specific move rules for each piece type here
        # For simplicity, we will just allow any move for now
        return True
    
    def draw_square_colors(self):
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    print("White square at ({}, {})".format(row, col))
                else:
                    print("Black square at ({}, {})".format(row, col))

board = html.TABLE()
for row in range(8):
    tr = html.TR()
    for col in range(8):
        td = html.TD()
        if (row + col) % 2 == 0:
            td.style.backgroundColor = "#e68a00"
        else:
            td.style.backgroundColor = "#ffd699"
        tr <= td
    board <= tr
document <= board