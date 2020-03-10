import pygame
from Board import Board
import Pieces
from GameManager import GameManger
from Player import Player

WIDTH = 20
HEIGHT = 20
WHITE = (255, 255, 255)
GRAY = (211, 211, 211)
MARGIN = 5

gm = GameManger()
gm.makePlayer('B', "Sean", gm)
gm.makePlayer('W', "Sean2", gm)
grid = []
for row in range(8):
    grid.append([])
    for col in range(8):
        grid[row].append(0)
pygame.init()
WINHEIGHT = 500
WINWIDTH = 500
WINDOW_SIZE = [WINHEIGHT, WINWIDTH]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("pyChess")

done = False
clock = pygame.time.Clock()
gameBoard = Board(8, (WINHEIGHT - WINHEIGHT*.1)/8)
gameBoard.makeBoard()
for j in range(8):
    gameBoard.table[1][j].occupiedBy = Pieces.pawn("W", 1, j)

for j in range(8):
    gameBoard.table[6][j].occupiedBy = Pieces.pawn("B", 6, j)

gameBoard.table[7][0].occupiedBy = Pieces.rook('B', 7, 0)
gameBoard.table[7][7].occupiedBy = Pieces.rook('B', 7, 7)
gameBoard.table[0][0].occupiedBy = Pieces.rook('W', 0, 0)
gameBoard.table[0][7].occupiedBy = Pieces.rook('W', 0, 7)

gameBoard.table[7][1].occupiedBy = Pieces.knight('B', 7, 1)
gameBoard.table[7][6].occupiedBy = Pieces.knight('B', 7, 6)
gameBoard.table[0][1].occupiedBy = Pieces.knight('W', 0, 1)
gameBoard.table[0][6].occupiedBy = Pieces.knight('W', 0, 6)

gameBoard.table[7][2].occupiedBy = Pieces.bishop('B', 7, 2)
gameBoard.table[7][5].occupiedBy = Pieces.bishop('B', 7, 5)
gameBoard.table[0][2].occupiedBy = Pieces.bishop('W', 0, 2)
gameBoard.table[0][5].occupiedBy = Pieces.bishop('W', 0, 5)

gameBoard.table[7][4].occupiedBy = Pieces.queen('B', 7, 4)
gameBoard.table[0][4].occupiedBy = Pieces.queen('W', 0, 4)

gameBoard.table[7][3].occupiedBy = Pieces.king('B', 7, 3)
gameBoard.table[0][3].occupiedBy = Pieces.king('W', 0, 3)

selected = None

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0]
            row = pos[1]
            for i in range(gameBoard.SIZE):
                for j in range(gameBoard.SIZE):
                    if selected != None and gameBoard.table[i][j].area.collidepoint(pos) and gameBoard.table[i][j] in selected.getMoves(gameBoard):
                        gm.takeTurn(gameBoard, selected, i, j)
                        print('test')
                        selected = None
                    elif gameBoard.table[i][j].area.collidepoint(pos):
                        selected = gameBoard.table[i][j].occupiedBy
    gameBoard.drawBoard(screen, selected, gm)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
