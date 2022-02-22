# import libraries
import pygame
import sys
from food import Food
from snake import Snake
from score import Score


def Init():
    # window size
    window_x = 720
    window_y = 480

    # boot pygame
    pygame.init()

    # set window
    pygame.display.set_caption('snake')
    return pygame.display.set_mode((window_x, window_y))



def StartGame(gameWindow):
    COLOR_BLACK = pygame.Color(0, 0, 0)
    FPS = 30
    gameover = False
    clock = pygame.time.Clock()

    food = Food(gameWindow)
    snake = Snake(gameWindow)
    score = Score(gameWindow)
    eatOk = False


    # main loop of game
    while gameover==False:
        events = pygame.event.get()
        # handle key events
        for event in events:
            if event.type == pygame.KEYDOWN:
                snake.ChangeDirection(event.key)
            elif event.type == pygame.USEREVENT:  # USEREVENT is triggered by the timer in snake.py
                eatOk = snake.Move(food.GetPosition())

        #display current image
        gameWindow.fill(COLOR_BLACK)
        food.Draw(eatOk)
        snake.Draw()        
        if snake.IsGameOver():
            gameover = True
            score.ShowFinal()
        else:
            score.Update(eatOk)
        pygame.display.update()
        
        # reset eatOk to False, because speed of snake is different with FPS
        if eatOk:
            eatOk = False

        # refresh rate
        clock.tick(FPS)

def main():
    gameWindow = Init()
    startGame = True
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    startGame = True
                if event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()

        if startGame:
            StartGame(gameWindow)
            startGame = False

if __name__ == '__main__':
    main()