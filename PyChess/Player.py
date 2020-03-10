import Pieces


class Player:
    def __init__(self, team, name, gm):
        self.team = team
        self.name = name
        self.gm = gm
        self.captured = []
        self.score = 0

    def setPrevCircle(self, oldRow, oldCol, newRow, newCol):
        self.oldRow = oldRow
        self.oldCol = oldCol
        self.newRow = newRow
        self.newCol = newCol

    def movePiece(self, board, selected, row, col):
        if board.table[row][col].occupiedBy != None:
            self.captured.append(board.table[row][col].occupiedBy)
        self.gm.movePiece(board, selected, row, col)
        if any(isinstance(piece, Pieces.king) for piece in self.captured):
            print("Game over")
            self.gm.endGame(self, board)

    def clearCaptured(self):
        self.captured = []
