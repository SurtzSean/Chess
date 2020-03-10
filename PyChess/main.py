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

clock = pygame.time.Clock()
gameBoard = Board(8, (WINHEIGHT - WINHEIGHT*.1)/8)
gameBoard.makeBoard()

gm.setBoard(gameBoard)


def gameLoop():
    done = False
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


gameLoop()
