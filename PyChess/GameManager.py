import Pieces
import pygame
from Player import Player


class GameManger:
    def __init__(self, screen):
        self.turn = None
        self.players = []
        self.curRow = None
        self.curCol = None
        self.prevRow = None
        self.prevCol = None
        self.whiteCaptured = []
        self.blackCaptured = []
        self.gameOver = False
        self.screen = screen
        self.winner = None
        self.tick = 0

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

    def endGame(self, player, board):
        self.prevRow = self.curRow = self.prevCol = self.curCol = None
        self.winner = player
        self.gameOver = True
        for player in self.players:
            player.clearCaptured()
        pygame.display.update()
        self.tick = 0

    def setBoard(self, gameBoard):
        whitePlayer = None
        blackPlayer = None
        for player in self.players:
            if player.team == 'W':
                whitePlayer = player
            else:
                blackPlayer = player

        for j in range(8):
            gameBoard.table[1][j].occupiedBy = Pieces.pawn("W", 1, j)
            whitePlayer.pieces.append(gameBoard.table[1][j].occupiedBy)

        for j in range(8):
            gameBoard.table[6][j].occupiedBy = Pieces.pawn("B", 6, j)
            blackPlayer.pieces.append(gameBoard.table[1][j].occupiedBy)

        gameBoard.table[7][0].occupiedBy = Pieces.rook('B', 7, 0)
        blackPlayer.pieces.append(gameBoard.table[7][0].occupiedBy)
        gameBoard.table[7][7].occupiedBy = Pieces.rook('B', 7, 7)
        blackPlayer.pieces.append(gameBoard.table[7][7].occupiedBy)
        gameBoard.table[0][0].occupiedBy = Pieces.rook('W', 0, 0)
        whitePlayer.pieces.append(gameBoard.table[0][0].occupiedBy)
        gameBoard.table[0][7].occupiedBy = Pieces.rook('W', 0, 7)
        whitePlayer.pieces.append(gameBoard.table[0][7].occupiedBy)

        gameBoard.table[7][1].occupiedBy = Pieces.knight('B', 7, 1)
        blackPlayer.pieces.append(gameBoard.table[7][1].occupiedBy)
        gameBoard.table[7][6].occupiedBy = Pieces.knight('B', 7, 6)
        blackPlayer.pieces.append(gameBoard.table[7][6].occupiedBy)
        gameBoard.table[0][1].occupiedBy = Pieces.knight('W', 0, 1)
        whitePlayer.pieces.append(gameBoard.table[0][1].occupiedBy)
        gameBoard.table[0][6].occupiedBy = Pieces.knight('W', 0, 6)
        whitePlayer.pieces.append(gameBoard.table[0][6].occupiedBy)

        gameBoard.table[7][2].occupiedBy = Pieces.bishop('B', 7, 2)
        blackPlayer.pieces.append(gameBoard.table[7][2].occupiedBy)
        gameBoard.table[7][5].occupiedBy = Pieces.bishop('B', 7, 5)
        blackPlayer.pieces.append(gameBoard.table[7][5].occupiedBy)
        gameBoard.table[0][2].occupiedBy = Pieces.bishop('W', 0, 2)
        whitePlayer.pieces.append(gameBoard.table[0][2].occupiedBy)
        gameBoard.table[0][5].occupiedBy = Pieces.bishop('W', 0, 5)
        whitePlayer.pieces.append(gameBoard.table[0][5].occupiedBy)

        gameBoard.table[7][4].occupiedBy = Pieces.queen('B', 7, 4)
        blackPlayer.pieces.append(gameBoard.table[7][4].occupiedBy)
        gameBoard.table[0][4].occupiedBy = Pieces.queen('W', 0, 4)
        whitePlayer.pieces.append(gameBoard.table[0][4].occupiedBy)

        gameBoard.table[7][3].occupiedBy = Pieces.king('B', 7, 3)
        blackPlayer.pieces.append(gameBoard.table[7][3].occupiedBy)
        gameBoard.table[0][3].occupiedBy = Pieces.king('W', 0, 3)
        whitePlayer.pieces.append(gameBoard.table[0][3].occupiedBy)
        print(whitePlayer.pieces)
        print(blackPlayer.pieces)

    def clearBoard(self, board):
        for i in range(len(board.table)):
            for j in range(len(board.table[0])):
                board.table[i][j].occupiedBy = None

    def showWinner(self):
        font = pygame.font.Font('freesansbold.ttf', 55)
        wTeam = 'Nobody'
        if self.winner.team == 'B':
            wTeam = 'Black'
        elif self.winner.team == 'W':
            wTeam = 'White'
        winText = wTeam + " has won!"
        textSurface = font.render(winText, True, (255, 0, 0))
        textRect = textSurface.get_rect()
        textRect.center = ((500/2), (500/2))
        self.screen.blit(textSurface, textRect)

    def removePiece(self, piece):
        player_to_remove = None
        for player in self.players:
            if player.team == piece.team:
                player_to_remove = player
        player_to_remove.pieces.remove(piece)
