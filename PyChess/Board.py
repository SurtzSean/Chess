from BoardPiece import BoardPiece


class Board(object):
    def __init__(self, boardSize, pieceSize):
        self.SIZE = boardSize
        self.pieceSize = pieceSize
        self.table = []
        for x in range(self.SIZE):
            self.table.append([])
            for col in range(self.SIZE):
                self.table[x].append(0)

    # set up empty board
    def makeBoard(self):
        other = False
        for col in range(self.SIZE):
            other = not other
            for row in range(self.SIZE):
                if other == True:
                    color = (255, 255, 255)
                    other = False
                else:
                    color = (211, 211, 211)
                    other = True
                self.table[row][col] = (BoardPiece(
                    None, color, self.pieceSize, row, col))

    def drawBoard(self, screen, selected, gm):
        curr = selected
        for row in range(self.SIZE):  # draw board
            for col in range(self.SIZE):
                self.table[row][col].drawPiece(screen)
        if selected != None:  # draw potential moves
            for move in selected.getMoves(self):
                if(gm.turn == selected.team):
                    move.drawValid(screen, 'RED')
                elif(gm.turn != selected.team):
                    move.drawValid(screen, 'BLUE')
        if gm.curRow != None and gm.curCol != None and gm.prevRow != None and gm.prevCol != None:
            self.drawPrev(
                screen, self.table[gm.curRow][gm.curCol], self.table[gm.prevRow][gm.prevCol])

    def drawPrev(self, screen, curr, prev):
        curr.drawPrev(screen)
        prev.drawPrev(screen)
