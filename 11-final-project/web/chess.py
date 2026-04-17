from browser import document, html, svg
from browser.template import Template


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

currArr = [[Piece("black", "rook", 0, 0), Piece("black", "knight", 0, 1), Piece("black", "bishop", 0, 2), Piece("black", "queen", 0, 3), Piece("black", "king", 0, 4), Piece("black", "bishop", 0, 5), Piece("black", "knight", 0, 6), Piece("black", "rook", 0, 7),],
           [Piece("black", "pawn", 1, 0), Piece("black", "pawn", 1, 1), Piece("black", "pawn", 1, 2), Piece("black", "pawn", 1, 3), Piece("black", "pawn", 1, 4), Piece("black", "pawn", 1, 5), Piece("black", "pawn", 1, 6), Piece("black", "pawn", 1, 7)],
           [Piece(None, None, 2, 0), Piece(None, None, 2, 1), Piece(None, None, 2, 2), Piece(None, None, 2, 3), Piece(None, None, 2, 4), Piece(None, None, 2, 5), Piece(None, None, 2, 6), Piece(None, None, 2, 7)],
           [Piece(None, None, 3, 0), Piece(None, None, 3, 1), Piece(None, None, 3, 2), Piece(None, None, 3, 3), Piece(None, None, 3, 4), Piece(None, None, 3, 5), Piece(None, None, 3, 6), Piece(None, None, 3, 7)],
           [Piece(None, None, 4, 0), Piece(None, None, 4, 1), Piece(None, None, 4, 2), Piece(None, None, 4, 3), Piece(None, None, 4, 4), Piece(None, None, 4, 5), Piece(None, None, 4, 6), Piece(None, None, 4, 7)],
           [Piece(None, None, 5, 0), Piece(None, None, 5, 1), Piece(None, None, 5, 2), Piece(None, None, 5, 3), Piece(None, None, 5, 4), Piece(None, None, 5, 5), Piece(None, None, 5, 6), Piece(None, None, 5, 7)],
           [Piece("white", "pawn", 6, 0), Piece("white", "pawn", 6, 1), Piece("white", "pawn", 6, 2), Piece("white", "pawn", 6, 3), Piece("white", "pawn", 6, 4), Piece("white", "pawn", 6, 5), Piece("white", "pawn", 6, 6), Piece("white", "pawn", 6, 7)],
           [Piece("white", "rook", 7, 0), Piece("white", "knight", 7, 1), Piece("white", "bishop", 7, 2), Piece("white", "queen", 7, 3), Piece("white", "king", 7, 4), Piece("white", "bishop", 7, 5), Piece("white", "knight", 7, 6), Piece("white", "rook", 7, 7)]]

def displayLegalMoves(id):
    currPiece = None
    for row in currArr:
        for piece in row:
            if (piece != None and "r" + str(piece.get_position()[0] * 8 + piece.get_position()[1]) == id):
                currPiece = piece
                break

    #Track Legal Moves for Pawn
    print("Current Piece: " + currPiece.get_name() + " at position " + str(currPiece.get_position()))
    if (currPiece != None):
    # print("Current Piece: " + currPiece.get_name() + " at position " + str(currPiece.get_position()))
        legalMoves = []
        if (currPiece.get_name() == "pawn"):
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
        print("Legal Moves: " + str(legalMoves))
        for move in legalMoves:
            document["r" + str(move[0] * 8 + move[1])].style.display = "block"
    

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
        if (row + col) % 2 == 0:
            td.style.backgroundColor = "#e68a00"
        else:
            td.style.backgroundColor = "#ffd699"
        print("Current Square: (" + str(row) + ", " + str(col) + ")")
        
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
            td.html = ""
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