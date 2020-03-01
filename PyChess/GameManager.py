import Pieces
from Player import Player


class GameManger:
    def __init__(self):
        self.players = []
        self.curRow = None
        self.curCol = None
        self.prevRow = None
        self.prevCol = None
        self.whiteCaptured = []
        self.blackCaptured = []
        self.gameOver = False

    def makePlayer(self, team, name):
        self.players.append(Player(team, name))
        self.manageTurn(self.players[0])

    def manageTurn(self, turn):
        self.turn = turn

    def movePiece(self, board, selected, row, col):
        if len(self.players) < 2:
            print("need 2 players to play chess")
            return
        if(self.turn.team != selected.team):
            print("You are " + self.turn.team +
                  " but you are trying to move a " + selected.team + " at ", selected.row, ",", selected.col)
            return
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
        if self.turn == self.players[0]:
            self.manageTurn(self.players[1])
            self.players[0].setPrevCircle(
                self.prevRow, self.prevCol, self.curRow, self.curCol)
        else:
            self.manageTurn(self.players[0])
            self.players[1].setPrevCircle(
                self.prevRow, self.prevCol, self.curRow, self.curCol)
        print("moved ", selected, 'to : ', row, ',', col)
