# Topic : PYGAME INFO..
# Pygame : Library of ready-made python tools for creating/building games(Graphic and Sound)
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

# pygame.init() : It is Basically A Switch Used Turning On All The Features Of Pygame,Like : Graphic,Sound,Input....IT IS ALSO CALLED INITALLIZING PYGAME
# pygame.display :Creates A Window / Screen For Pygame
# pygame.display.set_mode() : [set_mode() = Function ] Over Here in Set_Mode Tells The Dimensions (Size) Of The Window. First No. = Width & Second No. = Height..THERE ARE ALWAYS 2 () AFTER set_mode()
# pygame.event : Things That Need External Force(Input) In The Window..Like : Key Pressing,Mouse Clicking,etc..
# pygame.event.get() : .get() = Is Used For Capturing The Events
# pygame.display.flip() : Updates The Window Everytime 