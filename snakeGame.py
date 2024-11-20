import pygame
import random #for placing random food for snake

pygame.init()

screenWidth = 640
screenHeight = 480
gameWindow = pygame.display.set_mode((screenWidth, screenHeight))

# Game Title
pygame.display.set_caption("Snake Game")

black = (0, 0, 0)  # Black color for background
white = (255, 255, 255)  # White color for text or the snake body

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    gameWindow.fill(black)
    
    pygame.display.update()
    
    pygame.time.Clock().tick(15)
    
    

pygame.quit()