# import libraries
import pygame



# define colors
COLOR_WHITE = pygame.Color(255, 255, 255)
COLOR_RED = pygame.Color(255, 0, 0)



class Score:
    def __init__(self, surface):
        self.surface = surface
        self.value = 0
        self.font = 'times new roman'

    # display the realtime score
    def Update(self, eatOK):
        if eatOK:
            self.value += 10
        # create font object
        score_font = pygame.font.SysFont(self.font, 20)
        
        # display surface object
        score_surface = score_font.render('Score: ' + str(self.value), True, COLOR_WHITE)

        # rectangle for surface object
        score_rect = score_surface.get_rect()
        
        # display the text
        self.surface.blit(score_surface, score_rect)

    # display the final score
    def ShowFinal(self):
        # create font object
        font = pygame.font.SysFont(self.font, 50)
        surface = font.render('Final Score: ' + str( self.value), True, COLOR_WHITE) # create text surface
        rect = surface.get_rect()# rectangle for surface
        rect.midtop = (self.surface.get_width()/2, self.surface.get_height()/4) # set position of text
        self.surface.blit(surface, rect) # draw text

        font = pygame.font.SysFont(self.font, 30)
        surface = font.render('Do you want to play again?(y/n)', True, COLOR_RED) # create text surface
        rect = surface.get_rect()# rectangle for surface
        rect.midtop = (self.surface.get_width()/2, self.surface.get_height()/4 + 60) # set position of text
        self.surface.blit(surface, rect) # draw text

if __name__ == '__main__':
    print('this file can not be run as main')