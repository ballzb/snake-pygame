# import libraries
import pygame
import random

COLOR_GREEN = pygame.Color(0, 255, 0)

class Food:
    def __init__(self, surface):
        self.surface = surface
        self.Draw(True)

    def Draw(self, isMoved):
        if isMoved:
            x = self.surface.get_width()
            y = self.surface.get_height()
            self.position = [random.randrange(1, x//10) * 10, random.randrange(1, y//10) * 10]
        pygame.draw.rect(self.surface, COLOR_GREEN, pygame.Rect(self.position[0], self.position[1], 10, 10))

    def GetPosition(self):
        return self.position



if __name__ == '__main__':
    print('this file can not be run as main')