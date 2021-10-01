import time
import pygame

class View:

    def __init__(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Intelligence Artificielle M1')
        self.clock = pygame.time.Clock()
        self.crashed = False

    def refresh(self):
        while not self.crashed:
            self.screenUpdate(self)
            pygame.display.update()
            self.clock.tick(60)

    def screenUpdate(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.crashed = True
        self.gameDisplay.fill((50, 50, 50))
        pygame.draw.circle(self.gameDisplay, (0, 0, 255), (250, 250), 75)
        pygame.display.flip()
