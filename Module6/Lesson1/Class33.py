# Pygame : Library of ready-made python tools for creating/building games(graphic and sound)
# TO CREATE A DISPLAY FOLLOW THE GIVEN CODE
import pygame
pygame.init()
Screen = pygame.display.set_mode((400,500)) #Dimensions
Done = False
while not Done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
