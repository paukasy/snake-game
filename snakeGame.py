import pygame, sys, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cellNumber - 1)
        self.y = random.randint(0,cellNumber - 1)
        self.pos = Vector2(self.x,self.y)
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cellSize),int(self.pos.y * cellSize),cellSize,cellSize)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

pygame.init()
cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellNumber * cellSize,cellNumber * cellSize))
clock = pygame.time.Clock()

fruit = FRUIT()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175,215,70))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)