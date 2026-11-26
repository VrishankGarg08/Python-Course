# Basic Concepts Of Game Building.
# Sequence Of Colour : Red Green Blue
# DRAWING A RECTANGLE WITH pygame.draw.rect :
import pygame
pygame.init()
Screen = pygame.display.set_mode((200,200))
Done = False
while not Done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True
    pygame.draw.rect(Screen,(0,125,255),pygame.Rect(60,60,90,60))
    pygame.display.flip()

# 