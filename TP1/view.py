import time
import pygame

class View:

    def __init__(self, _house):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((700, 700))
        pygame.display.set_caption('Intelligence Artificielle M1')
        self.clock = pygame.time.Clock()
        self.crashed = False
        self.environment = _house
        self.offset = 10
        self.squareSize = ((700-self.offset)/self.environment.size) - self.offset

    def refresh(self):
        while not self.crashed:
            self.screenUpdate()
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()

    def screenUpdate(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.crashed = True
        self.gameDisplay.fill((100, 100, 100))
        x = 0
        for lin in self.environment.m_rooms:
            x += 1
            y = 0
            for col in lin:
                y += 1
                posX = (x-1) * self.squareSize + x * self.offset
                posY = (y-1) * self.squareSize + y * self.offset
                room = pygame.Rect(posX, posY, self.squareSize, self.squareSize)
                pygame.draw.rect(self.gameDisplay, (200, 200, 200), room)
                if col.hasDust():
                    dust = pygame.Rect(posX + (self.squareSize/5), posY + (self.squareSize/5), self.squareSize/6, self.squareSize/6)
                    pygame.draw.rect(self.gameDisplay, (0, 0, 0), dust)
                if col.hasJewel():
                    jewel = pygame.Rect(posX + 3*(self.squareSize / 5), posY + (self.squareSize / 5), self.squareSize / 6,
                                       self.squareSize / 6)
                    pygame.draw.rect(self.gameDisplay, (255, 255, 0), jewel)
                if col.hasRobot():
                    robot = pygame.Rect(posX + (self.squareSize / 5), posY + 3*(self.squareSize / 5), self.squareSize / 6,
                                       self.squareSize / 6)
                    pygame.draw.rect(self.gameDisplay, (255, 255, 255), robot)


