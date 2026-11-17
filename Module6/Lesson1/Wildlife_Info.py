import pygame
pygame.init()
Screen_Width = 500
Screen_Height = 500 
display_surface = pygame.display.set_mode(Screen_Width,Screen_Height)
Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
pygame.display.set_caption("Wildlife Information Display")
Background_Image = pygame.transform.scale(pygame.image.load("Background.png").convert(Screen_Width,Screen_Height))
Wildlife_Image = pygame.transform.scale(pygame.image.load("Tiger.png").convert_alpha(220,220))
Wildlife_Rect = Wildlife_Image.get_rect(center = (Screen_Width // 2, Screen_Height // 2 - 30) )
Heading_Font = pygame.font.Font(None,42)
Fact_Font = pygame.font.Font(None,28)
Heading_Text = Heading_Font.render("Wildlife Spotlight : Tiger" , True , pygame.Color("Black"))
Heading_Rect = Heading_Text.get_rect(center = (Screen_Width // 2, 420))
Fact_Text = Fact_Font.render("Tigers Are Powerful WildCats.",True , pygame.Color("Black"))
Fact_Rect = Fact_Text.get_rect(center = (Screen_Width // 2, 420))

def Game_Loop():
    Clock = pygame.time.Clock()
    Running = True
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                Running = False
        display_surface.blit(Background_Image(0,0))
        display_surface.blit(Wildlife_Image,Wildlife_Rect)
        display_surface.blit(Heading_Text,Heading_Rect)
        display_surface.blit(Fact_Text,Fact_Rect)
        pygame.display.flip()
        Clock.tick(30)
        pygame.quit()
if __name__ == "__main__":
    Game_Loop