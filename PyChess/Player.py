class Player:
    def __init__(self, team, name, gm):
        self.team = team
        self.name = name
        self.gm = gm

    def setPrevCircle(self, oldRow, oldCol, newRow, newCol):
        self.oldRow = oldRow
        self.oldCol = oldCol
        self.newRow = newRow
        self.newCol = newCol

    def movePiece(self, board, selected, row, col):
        self.gm.movePiece(board, selected, row, col)
