import pygame
from Board import Board
import Pieces
from GameManager import GameManger
from Player import Player
from AI import AI

pygame.init()

WINHEIGHT = 500
WINWIDTH = 500
MARGIN = 5
WIDTH = 20
HEIGHT = 20
WHITE = (255, 255, 255)
GRAY = (211, 211, 211)

WINDOW_SIZE = [WINHEIGHT, WINWIDTH]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("pyChess")

clock = pygame.time.Clock()


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()


def mainMenu():
    while True:
        screen.fill((0, 0, 0))
        textFont = pygame.font.Font('freesansbold.ttf', 115)
        playGame = "PLAY"
        TextSurf, TextRect = text_objects(playGame, textFont)
        TextRect.center = ((WINWIDTH/2), (WINHEIGHT/2))
        screen.blit(TextSurf, TextRect)

        pygame.display.update()

        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and TextRect.collidepoint(pos):
                screen.fill((0, 0, 0))
                gameLoop()
            elif event.type == pygame.QUIT:
                pygame.quit()


def gameLoop():
    gm = GameManger(screen)
    gameBoard = setup(gm)
    done = False
    selected = None
    AIPlayer = None
    for player in gm.players:
        if player.name == "AI":
            AIPlayer = player
    AIP = AI(None, gameBoard, AIPlayer)
    while not done:
        if gm.gameOver:
            gm.tick += 1
            if(gm.tick >= 100):
                del gm
                mainMenu()
            else:
                gm.showWinner()
        else:
            if AIP != None and AIP.player.team == gm.turn:
                AIP.move()
                gm.manageTurn()
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
                                selected = None
                            elif gameBoard.table[i][j].area.collidepoint(pos):
                                selected = gameBoard.table[i][j].occupiedBy
            gameBoard.drawBoard(screen, selected, gm)
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()


def setup(gm):
    gm.makePlayer('B', "P1", gm)
    gm.makePlayer('W', "AI", gm)

    grid = []
    for row in range(8):
        grid.append([])
        for col in range(8):
            grid[row].append(0)
    gameBoard = Board(8, (WINHEIGHT - WINHEIGHT*.1)/8)
    gameBoard.makeBoard()
    gm.setBoard(gameBoard)
    return gameBoard


mainMenu()
