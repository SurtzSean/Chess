import pygame


class BoardPiece():
    def __init__(self, occupiedBy, color, SIZE, row, col):
        self.occupiedBy = occupiedBy
        self.color = color
        self.SIZE = SIZE
        self.row = row
        self.col = col
        self.MARGIN = SIZE * .1
        self.area = pygame.Rect((self.MARGIN + self.SIZE) * self.col + self.MARGIN,
                                (self.MARGIN + self.SIZE) * self.row + self.MARGIN, self.SIZE, self.SIZE)
        self.center = self.area.center

    def drawPiece(self, screen):
        pygame.draw.rect(screen, self.color, [(self.MARGIN + self.SIZE) * self.col + self.MARGIN,
                                              (self.MARGIN + self.SIZE) * self.row + self.MARGIN, self.SIZE, self.SIZE])
        if(self.occupiedBy != None):
            image = pygame.image.load(self.occupiedBy.image)
            screen.blit(
                image, [self.center[0] - (self.SIZE/2.45), self.center[1] - (self.SIZE/2.45)])

    def drawValid(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.center, 10)

    def drawPrev(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), self.center,
                           27, 2)
