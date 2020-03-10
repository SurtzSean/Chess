import Pieces
from Player import Player


class GameManger:
    def __init__(self):
        self.turn = None
        self.players = []
        self.curRow = None
        self.curCol = None
        self.prevRow = None
        self.prevCol = None
        self.whiteCaptured = []
        self.blackCaptured = []
        self.gameOver = False

    def makePlayer(self, team, name, gm):
        self.players.append(Player(team, name, gm))
        if len(self.players) == 2:
            self.manageTurn()

    def takeTurn(self, gameBoard, selected, i, j):
        for player in self.players:
            if player.team == self.turn and selected.team == player.team:
                player.movePiece(gameBoard, selected, i, j)
                self.manageTurn()

    def manageTurn(self):
        if self.turn == None:
            self.turn = 'B'
        else:
            if self.turn == 'B':
                self.turn = 'W'
            elif self.turn == 'W':
                self.turn = 'B'

    def movePiece(self, board, selected, row, col):
        self.curRow = row
        self.curCol = col
        self.prevRow = selected.row
        self.prevCol = selected.col
        board.table[self.prevRow][self.prevCol].occupiedBy = None
        board.table[row][col].occupiedBy = selected
        selected.row = row
        selected.col = col
        if type(selected) == type(Pieces.pawn(None, None, None)):
            selected.firstMove = False
        if self.turn == 'W':
            self.players[0].setPrevCircle(
                self.prevRow, self.prevCol, self.curRow, self.curCol)
        else:
            self.players[1].setPrevCircle(
                self.prevRow, self.prevCol, self.curRow, self.curCol)
        print("moved ", selected, 'to : ', row, ',', col)
