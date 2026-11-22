import pygame
pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500 
Display_Surface = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
Screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Wildlife Information Display")
Background_Image = pygame.transform.scale(pygame.image.load("Background.png").convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))
Wildlife_Image = pygame.transform.scale(pygame.image.load("Tiger.png").convert_alpha(),(220,220))
Wildlife_Rect = Wildlife_Image.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30) )
Heading_Font = pygame.font.Font(None,42)
Fact_Font = pygame.font.Font(None,28)
Heading_Text = Heading_Font.render("Wildlife Spotlight : Tiger" , True , pygame.Color("Black"))
Heading_Rect = Heading_Text.get_rect(center = (SCREEN_WIDTH // 2, 420))
Fact_Text = Fact_Font.render("Tigers Are Powerful WildCats.",True , pygame.Color("Black"))
Fact_Rect = Fact_Text.get_rect(center = (SCREEN_WIDTH // 2, 420))

def Game_Loop():
    Clock = pygame.time.Clock()
    Running = True
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
        Display_Surface.blit(Background_Image,(0,0))
        Display_Surface.blit(Wildlife_Image,Wildlife_Rect)
        Display_Surface.blit(Heading_Text,Heading_Rect)
        Display_Surface.blit(Fact_Text,Fact_Rect)
        pygame.display.flip()
        Clock.tick(30)
        pygame.quit()
if __name__ == "__main__":
    Game_Loop()