# import libraries
import pygame


# define colors
COLOR_GREEN = pygame.Color(0, 255, 0)
SPEED_OF_SNAKE = 5 # times of move in 1 sec
USEREVENT_SNAKE_MOVE = pygame.USEREVENT

class Snake:
    def __init__(self, surface):
        self.surface = surface
        self.width = 10
        self.head = [100, 50]
        self.body = [ [100, 50], [90, 50], [80, 50], [70, 50] ]
        self.direction = pygame.K_RIGHT
        pygame.time.set_timer(USEREVENT_SNAKE_MOVE, 1000//SPEED_OF_SNAKE)

    def ChangeDirection(self, key):
        if key == pygame.K_UP and self.direction != pygame.K_DOWN:
            self.direction = pygame.K_UP
        elif key == pygame.K_DOWN and self.direction != pygame.K_UP:
            self.direction = pygame.K_DOWN
        elif key == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
            self.direction = pygame.K_LEFT
        elif key == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
            self.direction = pygame.K_RIGHT

    def Move(self, foodPosition):
        if self.direction == pygame.K_UP:
            self.head[1] -= self.width
        elif self.direction == pygame.K_DOWN:
            self.head[1] += self.width
        elif self.direction == pygame.K_LEFT:
            self.head[0] -= self.width
        elif self.direction == pygame.K_RIGHT:
            self.head[0] += self.width
        self.body.insert(0, list(self.head))
        if self.head == foodPosition:
            return True
        else:
            self.body.pop()
            return False

    
    def Draw(self):
        for pos in self.body:
            pygame.draw.rect(self.surface, COLOR_GREEN, pygame.Rect(pos[0], pos[1], self.width, self.width))

    def IsGameOver(self):
        # game over conditions
        if self.head[0] < 0 or self.head[0] > self.surface.get_width()-10:
            return True

        if self.head[1] < 0 or self.head[1] > self.surface.get_height()-10:
            return True
            
        # snake touching itself
        for block in self.body[1:]:
            if self.head  == block:
                return True
        
        return False

if __name__ == '__main__':
    print('this file can not be run as main')
