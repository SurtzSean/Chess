class Player:
    def __init__(self, team, name):
        self.team = team
        self.name = name

    def setPrevCircle(self, oldRow, oldCol, newRow, newCol):
        self.oldRow = oldRow
        self.oldCol = oldCol
        self.newRow = newRow
        self.newCol = newCol
