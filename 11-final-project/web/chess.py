from browser import document, html, svg
from browser.template import Template

turn = True #True for white's turn, False for black
moveCount = 0
moves = []
enPassantCheck = False

# Class to represent a chess piece, with attributes for color, type, position, and HTML element ID.

class Piece:

    def __init__(self, color, name, row, col, id):
        self.color = color
        self.name = name
        self.row = row
        self.col = col
        self.id = id

    def get_color(self):
        return self.color
    def get_name(self):
        return self.name
    def get_position(self):
        return (self.row, self.col)
    def get_row(self):
        return self.row
    def get_col(self):
        return self.col
    def get_id(self):
        return self.id
    def set_row(self, row):
        self.row = row
    def set_col(self, col):
        self.col = col
    def set_id(self, id):
        self.id = id

# Starting Board of the Chess Game represented as a 2D array of Piece objects, with None representing empty squares.

currArr = [[Piece("black", "rook", 0, 0, "rookb0"), Piece("black", "knight", 0, 1, "knightb1"), Piece("black", "bishop", 0, 2, "bishopb2"), Piece("black", "queen", 0, 3, "queenb3"), Piece("black", "king", 0, 4, "kingb4"), Piece("black", "bishop", 0, 5, "bishopb5"), Piece("black", "knight", 0, 6, "knightb6"), Piece("black", "rook", 0, 7, "rookb7")],
           [Piece("black", "pawn", 1, 0, "pawnb8"), Piece("black", "pawn", 1, 1, "pawnb9"), Piece("black", "pawn", 1, 2, "pawnb10"), Piece("black", "pawn", 1, 3, "pawnb11"), Piece("black", "pawn", 1, 4, "pawnb12"), Piece("black", "pawn", 1, 5, "pawnb13"), Piece("black", "pawn", 1, 6, "pawnb14"), Piece("black", "pawn", 1, 7, "pawnb15")],
           [None, None, None, None, None, None, None, None],
           [None, None, None, None, None, None, None, None],
           [None, None, None, None, None, None, None, None],
           [None, None, None, None, None, None, None, None],
           [Piece("white", "pawn", 6, 0, "pawnw48"), Piece("white", "pawn", 6, 1, "pawnw49"), Piece("white", "pawn", 6, 2, "pawnw50"), Piece("white", "pawn", 6, 3, "pawnw51"), Piece("white", "pawn", 6, 4, "pawnw52"), Piece("white", "pawn", 6, 5, "pawnw53"), Piece("white", "pawn", 6, 6, "pawnw54"), Piece("white", "pawn", 6, 7, "pawnw55")],
           [Piece("white", "rook", 7, 0, "rookw56"), Piece("white", "knight", 7, 1, "knightw57"), Piece("white", "bishop", 7, 2, "bishopw58"), Piece("white", "queen", 7, 3, "queenw59"), Piece("white", "king", 7, 4, "kingw60"), Piece("white", "bishop", 7, 5, "bishopw61"), Piece("white", "knight", 7, 6, "knightw62"), Piece("white", "rook", 7, 7, "rookw63")]]

currPiece = None
legalMoves = []


# Displays the legal moves for a selected piece by checking the piece's type and position, 
# and comparing it to the current state of the board in currArr.

def displayLegalMoves(id):
    global currPiece, legalMoves, turn, moves, moveCount
    for row in currArr:
        for piece in row:
            if (piece != None):
                # print("Checking piece at position " + str(piece.get_position()) + " with id " + str(piece.get_name()) + str(piece.get_position()[0] * 8 + piece.get_position()[1]) + " against selected id " + id)
                currId = str(piece.get_name()) + str(piece.get_color()[0]) + str(piece.get_position()[0] * 8 + piece.get_position()[1])
                # print("Current Piece ID: " + currId + " | Selected ID: " + id)
                if (currId == id):
                    currPiece = piece
                    break
    hideLegalMoves()
    #Track Legal Moves for Pawn
    # print("Current Piece: " + currPiece.get_name() + " at position " + str(currPiece.get_position()))
    if (currPiece != None and ((turn and currPiece.get_color() == "white") or (not turn and currPiece.get_color() == "black"))):
    # print("Current Piece: " + currPiece.get_name() + " at position " + str(currPiece.get_position()))
        
        legalMoves = []
        
        if (currPiece.get_name() == "pawn" and not isPawnBlocked(currPiece.get_position()[0], currPiece.get_position()[1])):
            if (moveCount > 0):
                enPassant()
            if (currPiece.get_color() == "white"):
                if (currPiece.get_position()[0] > 0 and currArr[currPiece.get_position()[0] - 1][currPiece.get_position()[1]] == None):
                    legalMoves.append((currPiece.get_position()[0] - 1, currPiece.get_position()[1]))
                if (currPiece.get_position()[0] == 6 and currArr[currPiece.get_position()[0] - 2][currPiece.get_position()[1]] == None):
                    legalMoves.append((currPiece.get_position()[0] - 2, currPiece.get_position()[1]))
                if (currPiece.get_position()[0] > 0 and currPiece.get_position()[1] > 0 and currArr[currPiece.get_position()[0] - 1][currPiece.get_position()[1] - 1] != None and currArr[currPiece.get_position()[0] - 1][currPiece.get_position()[1] - 1].get_color() == "black"):
                    legalMoves.append((currPiece.get_position()[0] - 1, currPiece.get_position()[1] - 1))
                if (currPiece.get_position()[0] > 0 and currPiece.get_position()[1] < 7 and currArr[currPiece.get_position()[0] - 1][currPiece.get_position()[1] + 1] != None and currArr[currPiece.get_position()[0] - 1][currPiece.get_position()[1] + 1].get_color() == "black"):
                    legalMoves.append((currPiece.get_position()[0] - 1, currPiece.get_position()[1] + 1))
            else:
                if (currPiece.get_position()[0] < 7 and currArr[currPiece.get_position()[0] + 1][currPiece.get_position()[1]] == None):
                    legalMoves.append((currPiece.get_position()[0] + 1, currPiece.get_position()[1]))
                if (currPiece.get_position()[0] == 1 and currArr[currPiece.get_position()[0] + 2][currPiece.get_position()[1]] == None):
                    legalMoves.append((currPiece.get_position()[0] + 2, currPiece.get_position()[1]))
                if (currPiece.get_position)()[0] < 7 and currPiece.get_position()[1] > 0 and currArr[currPiece.get_position()[0] + 1][currPiece.get_position()[1] - 1] != None and currArr[currPiece.get_position()[0] + 1][currPiece.get_position()[1] - 1].get_color() == "white":
                    legalMoves.append((currPiece.get_position()[0] + 1, currPiece.get_position()[1] - 1))
                if (currPiece.get_position()[0] < 7 and currPiece.get_position()[1] < 7 and currArr[currPiece.get_position()[0] + 1][currPiece.get_position()[1] + 1] != None and currArr[currPiece.get_position()[0] + 1][currPiece.get_position()[1] + 1].get_color() == "white"):
                    legalMoves.append((currPiece.get_position()[0] + 1, currPiece.get_position()[1] + 1))

    #Track Legal Moves for Rook
        elif (currPiece.get_name() == "rook"):
            for i in range(currPiece.get_position()[0] + 1, 8):
                if (currArr[i][currPiece.get_position()[1]] == None):
                    legalMoves.append((i, currPiece.get_position()[1]))
                elif (currArr[i][currPiece.get_position()[1]].get_color() != currPiece.get_color()):
                    legalMoves.append((i, currPiece.get_position()[1]))
                    break
                else:
                    break
            for i in range(currPiece.get_position()[0] - 1, -1, -1):
                if (currArr[i][currPiece.get_position()[1]] == None):
                    legalMoves.append((i, currPiece.get_position()[1]))
                elif (currArr[i][currPiece.get_position()[1]].get_color() != currPiece.get_color()):
                    legalMoves.append((i, currPiece.get_position()[1]))
                    break
                else:
                    break
            for j in range(currPiece.get_position()[1] + 1, 8):
                if (currArr[currPiece.get_position()[0]][j] == None):
                    legalMoves.append((currPiece.get_position()[0], j))
                elif (currArr[currPiece.get_position()[0]][j].get_color() != currPiece.get_color()):
                    legalMoves.append((currPiece.get_position()[0], j))
                    break
                else:
                    break
            for j in range(currPiece.get_position()[1] - 1, -1, -1):
                if (currArr[currPiece.get_position()[0]][j] == None):
                    legalMoves.append((currPiece.get_position()[0], j))
                elif (currArr[currPiece.get_position()[0]][j].get_color() != currPiece.get_color()):
                    legalMoves.append((currPiece.get_position()[0], j))
                    break
                else:
                    break
    #Track Legal Moves for Knight
        elif (currPiece.get_name() == "knight"):
            knightMoves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
            for move in knightMoves:
                newRow = currPiece.get_position()[0] + move[0]
                newCol = currPiece.get_position()[1] + move[1]
                if (newRow >= 0 and newRow < 8 and newCol >= 0 and newCol < 8):
                    if (currArr[newRow][newCol] == None or currArr[newRow][newCol].get_color() != currPiece.get_color()):
                        legalMoves.append((newRow, newCol))
    #Track Legal Moves for Bishop
        elif (currPiece.get_name() == "bishop"):
            for i, j in zip(range(currPiece.get_position()[0] + 1, 8), range(currPiece.get_position()[1] + 1, 8)):
                if (currArr[i][j] == None):
                    legalMoves.append((i, j))
                elif (currArr[i][j].get_color() != currPiece.get_color()):
                    legalMoves.append((i, j))
                    break
                else:
                    break
            for i, j in zip(range(currPiece.get_position()[0] + 1, 8), range(currPiece.get_position()[1] - 1, -1, -1)):
                if (currArr[i][j] == None):
                    legalMoves.append((i, j))
                elif (currArr[i][j].get_color() != currPiece.get_color()):
                    legalMoves.append((i, j))
                    break
                else:
                    break
            for i, j in zip(range(currPiece.get_position()[0] - 1, -1, -1), range(currPiece.get_position()[1] + 1, 8)):
                if (currArr[i][j] == None):
                    legalMoves.append((i, j))
                elif (currArr[i][j].get_color() != currPiece.get_color()):
                    legalMoves.append((i, j))
                    break
                else:
                    break
            for i, j in zip(range(currPiece.get_position()[0] - 1, -1, -1), range(currPiece.get_position()[1] - 1, -1, -1)):
                if (currArr[i][j] == None):
                    legalMoves.append((i, j))
                elif (currArr[i][j].get_color() != currPiece.get_color()):
                    legalMoves.append((i, j))
                    break
                else:
                    break
    #Track Legal Moves for Queen
        elif (currPiece.get_name() == "queen"):
            for i in range(currPiece.get_position()[0] + 1, 8):
                if (currArr[i][currPiece.get_position()[1]] == None):
                    legalMoves.append((i, currPiece.get_position()[1]))
                elif (currArr[i][currPiece.get_position()[1]].get_color() != currPiece.get_color()):
                    legalMoves.append((i, currPiece.get_position()[1]))
                    break
                else:
                    break
            for i in range(currPiece.get_position()[0] - 1, -1, -1):
                if (currArr[i][currPiece.get_position()[1]] == None):
                    legalMoves.append((i, currPiece.get_position()[1]))
                elif (currArr[i][currPiece.get_position()[1]].get_color() != currPiece.get_color()):
                    legalMoves.append((i, currPiece.get_position()[1]))
                    break
                else:
                    break
            for j in range(currPiece.get_position()[1] + 1, 8):
                if (currArr[currPiece.get_position()[0]][j] == None):
                    legalMoves.append((currPiece.get_position()[0], j))
                elif (currArr[currPiece.get_position()[0]][j].get_color() != currPiece.get_color()):
                    legalMoves.append((currPiece.get_position()[0], j))
                    break
                else:
                    break
            for j in range(currPiece.get_position()[1] - 1, -1, -1):
                if (currArr[currPiece.get_position()[0]][j] == None):
                    legalMoves.append((currPiece.get_position()[0], j))
                elif (currArr[currPiece.get_position()[0]][j].get_color() != currPiece.get_color()):
                    legalMoves.append((currPiece.get_position()[0], j))
                    break
                else:
                    break
            for i, j in zip(range(currPiece.get_position()[0] + 1, 8), range(currPiece.get_position()[1] + 1, 8)):
                if (currArr[i][j] == None):
                    legalMoves.append((i, j))
                elif (currArr[i][j].get_color() != currPiece.get_color()):
                    legalMoves.append((i, j))
                    break
                else:
                    break
            for i, j in zip(range(currPiece.get_position()[0] + 1, 8), range(currPiece.get_position()[1] - 1, -1, -1)):              
                if (currArr[i][j] == None):
                    legalMoves.append((i, j))
                elif (currArr[i][j].get_color() != currPiece.get_color()):
                    legalMoves.append((i, j))
                    break
                else:
                    break
            for i, j in zip(range(currPiece.get_position()[0] - 1, -1, -1), range(currPiece.get_position()[1] + 1, 8)):
                if (currArr[i][j] == None):
                    legalMoves.append((i, j))
                elif (currArr[i][j].get_color() != currPiece.get_color()):
                    legalMoves.append((i, j))
                    break
                else:
                    break
            for i, j in zip(range(currPiece.get_position()[0] - 1, -1, -1), range(currPiece.get_position()[1] - 1, -1, -1)):
                if (currArr[i][j] == None):
                    legalMoves.append((i, j))
                elif (currArr[i][j].get_color() != currPiece.get_color()):
                    legalMoves.append((i, j))
                    break
                else:
                    break
    #Track Legal Moves for King
        elif (currPiece.get_name() == "king"):
            kingMoves = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
            for move in kingMoves:
                newRow = currPiece.get_position()[0] + move[0]
                newCol = currPiece.get_position()[1] + move[1]
                if (newRow >= 0 and newRow < 8 and newCol >= 0 and newCol < 8):
                    if (currArr[newRow][newCol] == None or currArr[newRow][newCol].get_color() != currPiece.get_color()):
                        legalMoves.append((newRow, newCol))
    #Highlight Legal Moves
        for move in legalMoves:
            print(str(move[0] * 8 + move[1]))
            document["r" + str(move[0] * 8 + move[1])].style.display = "block"
        
# Added to the =displayed moves to register what move the user wants to make
# Resets legal moves shown, adds to moveCount, and keeps track of moves made

def legalMoveClicked(event, element):
    global turn, moveCount, moves, enPassantCheck

    moveCount += 1


    elementID = element.data.id

    newSquareNum = int(elementID[1:])
    newRow = newSquareNum // 8
    newCol = newSquareNum % 8

    oldSquareNum = currPiece.get_row() * 8 + currPiece.get_col()
    oldRow = currPiece.get_row()
    oldCol = currPiece.get_col()

    moves.append((currPiece.get_name(), currPiece.get_color(), oldSquareNum, newSquareNum))

    #Move Piece in currArr
    print("Moving piece " + currPiece.get_name() + " from position " + str(currPiece.get_position()) + " to position (" + str(newRow) + ", " + str(newCol) + ")")

    if (currArr[newRow][newCol] != None): # This is the check for taking a piece
        takenPiece = currArr[newRow][newCol]
        takenPieceID = takenPiece.get_id()
        currArr[newRow][newCol] = currPiece
        currArr[currPiece.get_row()][currPiece.get_col()] = None
        currPiece.set_row(newRow)
        currPiece.set_col(newCol)
        #Update Board
        oldSquareNum = oldRow * 8 + oldCol
        originalSquare = document[currPiece.get_id()]
        document[originalSquare.id].id = "empty" + str(oldSquareNum)
        document[originalSquare.id].innerHTML = ""
        # originalSquare.html = "<div id='empty" + str(oldSquareNum) + "'></div>"
        document[takenPieceID].innerHTML = "<button class='" + currPiece.get_name() + currPiece.get_color()[0] + "' b-on='click:selectPiece'></button></div>"
        document[takenPieceID].id = currPiece.get_name() + currPiece.get_color()[0] + str(newSquareNum)
        # newSquare.html = "<div id='" + currPiece.get_id() + "'><button class='" + currPiece.get_name() + currPiece.get_color()[0] + "' b-on='click:selectPiece'></button></div>"
        currPiece.set_id(currPiece.get_name() + currPiece.get_color()[0] + str(newSquareNum))
        Template(currPiece.get_id(), [selectPiece]).render(id=currPiece.get_id())
    elif (currArr[newRow][newCol] == None): # Check for En Passant/Not Taking Piece
        if (enPassantCheck): # En Passant Check
            if (currPiece.get_color() == "white"):
                takenPiece = currArr[newRow + 1][newCol]
                takenPieceID = takenPiece.get_id()
                currArr[newRow + 1][newCol] = None
                document[takenPieceID].innerHTML = "<div id='empty" + str((newRow + 1) * 8 + newCol) + "'></div>"
            else:
                takenPiece = currArr[newRow - 1][newCol]
                takenPieceID = takenPiece.get_id()
                currArr[newRow - 1][newCol] = None
                document[takenPieceID].innerHTML = "<div id='empty" + str((newRow - 1) * 8 + newCol) + "'></div>"
            enPassantCheck = not enPassantCheck
        
        currArr[newRow][newCol] = currPiece
        currArr[currPiece.get_row()][currPiece.get_col()] = None
        currPiece.set_row(newRow)
        currPiece.set_col(newCol)
        #Update Board
        oldSquareNum = oldRow * 8 + oldCol
        originalSquare = document[currPiece.get_id()]
        document[originalSquare.id].id = "empty" + str(oldSquareNum)
        document[originalSquare.id].innerHTML = ""
        # originalSquare.html = "<div id='empty" + str(oldSquareNum) + "'></div>"
        document["empty" + str(newSquareNum)].innerHTML = "<button class='" + currPiece.get_name() + currPiece.get_color()[0] + "' b-on='click:selectPiece'></button></div>"
        document["empty" + str(newSquareNum)].id = currPiece.get_name() + currPiece.get_color()[0] + str(newSquareNum)
        # newSquare.html = "<div id='" + currPiece.get_id() + "'><button class='" + currPiece.get_name() + currPiece.get_color()[0] + "' b-on='click:selectPiece'></button></div>"
        currPiece.set_id(currPiece.get_name() + currPiece.get_color()[0] + str(newSquareNum))
        Template(currPiece.get_id(), [selectPiece]).render(id=currPiece.get_id())
    hideLegalMoves()
    turn = not turn

# Checks if the square in front of a pawn is blocked
# Needed because if a piece was in front on an unmoved pawn, the pawn could jump over it.

def isPawnBlocked(row, col):
    if (currPiece.get_color() == "white"):
        if (row > 0 and currArr[row - 1][col] != None):
            return True
    else:
        if (row < 7 and currArr[row + 1][col] != None):
            return True
    return False


# Checks if En Passant is possible and if so, adds the En Passant move to legalMoves 
# and toggles the enPassantCheck variable to track whether the En Passant move is currently available. 
# This function is called in displayLegalMoves when a pawn is selected, and checks the last move made to 
# see if it was a two-square pawn advance that would allow for an En Passant capture on the next turn.

def enPassant():
    global legalMoves, moves, moveCount, enPassantCheck
    lastMove = moves[moveCount - 1]
    if (lastMove[0] == "pawn" and abs(lastMove[3] - lastMove[2]) == 16):
        lastMoveCol = lastMove[3] % 8
        lastMoveRow = lastMove[3] // 8
        if (currPiece.get_position()[0] == lastMoveRow and abs(currPiece.get_position()[1] - lastMoveCol) == 1):
            if (currPiece.get_color() == "white" and lastMove[1] == "black" and currPiece.get_position()[0] == 3):
                legalMoves.append((2, lastMoveCol))
            elif (currPiece.get_color() == "black" and lastMove[1] == "white" and currPiece.get_position()[0] == 4):
                legalMoves.append((5, lastMoveCol))
            enPassantCheck = not enPassantCheck
    



def hideLegalMoves():
    for move in legalMoves:
        document["r" + str(move[0] * 8 + move[1])].style.display = "none"



def selectPiece(event, element):
    elementID = element.data.id
    # print("Selected Piece: " + elementID)
    displayLegalMoves(elementID)
    
squareCount = 0

board = html.TABLE()

for row in range(8):
    tr = html.TR()
    tr.style.height = "50px"

    for col in range(8):
        td = html.TD()
        td.style.width = "50px"
        if (row + col) % 2 == 1:
            td.style.backgroundColor = "#e68a00"
        else:
            td.style.backgroundColor = "#ffd699"
        
        # Creates the HTML for the piece on the current square, if there is one, 
        # and adds it to the td element. Also adds a button for legal moves on each square.

        if (currArr[row][col] != None and currArr[row][col].get_name() != None):
            piece = currArr[row][col]

            if (piece.get_name() == "pawn"):
                td.html = "<div id='pawnb" + str(squareCount) + "'><button class='pawnb' b-on='click:selectPiece'></button>" if piece.get_color() == "black" else "<div id='pawnw" + str(squareCount) + "'><button class='pawnw' b-on='click:selectPiece'></button>"
                
            elif (piece.get_name() == "rook"):
                td.html = "<div id='rookb" + str(squareCount) + "'><button class='rookb' b-on='click:selectPiece'></button>" if piece.get_color() == "black" else "<div id='rookw" + str(squareCount) + "'><button class='rookw' b-on='click:selectPiece'></button>"

            elif (piece.get_name() == "knight"):
                td.html = "<div id='knightb" + str(squareCount) + "'><button class='knightb' b-on='click:selectPiece'></button>" if piece.get_color() == "black" else "<div id='knightw" + str(squareCount) + "'><button class='knightw' b-on='click:selectPiece'></button>"
               
            elif (piece.get_name() == "queen"):
                td.html = "<div id='queenb" + str(squareCount) + "'><button class='queenb' b-on='click:selectPiece'></button>" if piece.get_color() == "black" else "<div id='queenw" + str(squareCount) + "'><button class='queenw' b-on='click:selectPiece'></button>"
                
            elif (piece.get_name() == "king"):
                td.html = "<div id='kingb" + str(squareCount) + "'><button class='kingb' b-on='click:selectPiece'></button>" if piece.get_color() == "black" else "<div id='kingw" + str(squareCount) + "'><button class='kingw' b-on='click:selectPiece'></button>"
               
            elif (piece.get_name() == "bishop"):
                td.html = "<div id='bishopb" + str(squareCount) + "'><button class='bishopb' b-on='click:selectPiece'></button>" if piece.get_color() == "black" else "<div id='bishopw" + str(squareCount) + "'><button class='bishopw' b-on='click:selectPiece'></button>"
                
            else:
                td.html = "<div>"
        else:
            td.html = "<div id='empty" + str(squareCount) + "'></div>"
        # td.html = "<circle cx='25' cy='25' r='20' fill='red' id='r" + str(squareCount) + "' style='display:none;' ></circle>" + td.html 
        # td.html =  td.html + "<svg width='50' height='50' style='display:none;' id='r" + str(squareCount) + "'><circle cx='25' cy='25' r='10' fill='red' onClick='legalMoveClicked(" + str(squareCount) + ")'></circle></svg></div>"
        td.html = td.html + "<div class='legal-move' id='r" + str(squareCount) + "'><button class='legal-move-button' b-on='click:legalMoveClicked'></button></div>"

        squareCount += 1

        tr <= td
    board <= tr
document <= board # Displays the board on the webpage

# Adds the OnClick event listeners to each piece and legal move button, and renders the initial chess board with pieces in their starting positions.

Template("rookb0", [selectPiece]).render(id="rookb0")
Template("knightb1", [selectPiece]).render(id="knightb1")
Template("bishopb2", [selectPiece]).render(id="bishopb2")
Template("queenb3", [selectPiece]).render(id="queenb3")
Template("kingb4", [selectPiece]).render(id="kingb4")
Template("bishopb5", [selectPiece]).render(id="bishopb5")
Template("knightb6", [selectPiece]).render(id="knightb6")
Template("rookb7", [selectPiece]).render(id="rookb7")

Template("pawnb8", [selectPiece]).render(id="pawnb8")
Template("pawnb9", [selectPiece]).render(id="pawnb9")
Template("pawnb10", [selectPiece]).render(id="pawnb10")
Template("pawnb11", [selectPiece]).render(id="pawnb11")
Template("pawnb12", [selectPiece]).render(id="pawnb12")
Template("pawnb13", [selectPiece]).render(id="pawnb13")
Template("pawnb14", [selectPiece]).render(id="pawnb14")
Template("pawnb15", [selectPiece]).render(id="pawnb15")

Template("rookw56", [selectPiece]).render(id="rookw56")
Template("knightw57", [selectPiece]).render(id="knightw57")
Template("bishopw58", [selectPiece]).render(id="bishopw58")
Template("queenw59", [selectPiece]).render(id="queenw59")
Template("kingw60", [selectPiece]).render(id="kingw60")
Template("bishopw61", [selectPiece]).render(id="bishopw61")
Template("knightw62", [selectPiece]).render(id="knightw62")
Template("rookw63", [selectPiece]).render(id="rookw63")

Template("pawnw48", [selectPiece]).render(id="pawnw48")
Template("pawnw49", [selectPiece]).render(id="pawnw49")
Template("pawnw50", [selectPiece]).render(id="pawnw50")
Template("pawnw51", [selectPiece]).render(id="pawnw51")
Template("pawnw52", [selectPiece]).render(id="pawnw52")
Template("pawnw53", [selectPiece]).render(id="pawnw53")
Template("pawnw54", [selectPiece]).render(id="pawnw54")
Template("pawnw55", [selectPiece]).render(id="pawnw55")

for i in range(64):
    Template("r" + str(i), [legalMoveClicked]).render(id="r" + str(i))