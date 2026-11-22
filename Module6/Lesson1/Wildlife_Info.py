# import pygame
# pygame.init()
# SCREEN_WIDTH = 500
# SCREEN_HEIGHT = 500 
# Display_Surface = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
# Screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# pygame.display.set_caption("Wildlife Information Display")
# Background_Image = pygame.transform.scale(pygame.image.load("Background.png").convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))
# Wildlife_Image = pygame.transform.scale(pygame.image.load("Tiger.png").convert_alpha(),(220,220))
# Wildlife_Rect = Wildlife_Image.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30) )
# Heading_Font = pygame.font.Font(None,42)
# Fact_Font = pygame.font.Font(None,28)
# Heading_Text = Heading_Font.render("Wildlife Spotlight : Tiger" , True , pygame.Color("Black"))
# Heading_Rect = Heading_Text.get_rect(center = (SCREEN_WIDTH // 2, 420))
# Fact_Text = Fact_Font.render("Tigers Are Powerful WildCats.",True , pygame.Color("Black"))
# Fact_Rect = Fact_Text.get_rect(center = (SCREEN_WIDTH // 2, 420))

# def Game_Loop():
#     Clock = pygame.time.Clock()
#     Running = True
#     while Running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 Running = False
#         Display_Surface.blit(Background_Image,(0,0))
#         Display_Surface.blit(Wildlife_Image,Wildlife_Rect)
#         Display_Surface.blit(Heading_Text,Heading_Rect)
#         Display_Surface.blit(Fact_Text,Fact_Rect)
#         pygame.display.flip()
#         Clock.tick(30)
#         pygame.quit()
# if __name__ == "__main__":
#     Game_Loop()

# Wildlife Information Display
 
# Import necessary library
import pygame
 
# Initialize Pygame
pygame.init()
 
# Set screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 650
 
# Create the display window
display_surface = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)
 
# Set the window title
pygame.display.set_caption(
    "Wildlife Information Display"
)
 
# Load and scale the background image
background_image = pygame.transform.scale(
    pygame.image.load("Background.png").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)
 
# Load and scale the wildlife image
wildlife_image = pygame.transform.scale(
    pygame.image.load("Tiger.png").convert_alpha(),
    (220, 200)
)
 
# Position the wildlife image at the centre
wildlife_rect = wildlife_image.get_rect(
    center=(
        SCREEN_WIDTH // 2,
        SCREEN_HEIGHT // 2 - 30
    )
)
 
# Create fonts for the heading and information
heading_font = pygame.font.Font(None, 42)
fact_font = pygame.font.Font(None, 30)
 
# Render the heading text
heading_text = heading_font.render(
    "Wildlife Spotlight: Tiger",
    True,
    pygame.Color("black")
)
 
# Position the heading
heading_rect = heading_text.get_rect(
    center=(SCREEN_WIDTH // 2, 45)
)
 
# Render the wildlife fact
fact_text = fact_font.render(
    "Tigers are powerful wild cats.",
    True,
    pygame.Color("black")
)
 
# Position the fact text
fact_rect = fact_text.get_rect(
    center=(SCREEN_WIDTH // 2, 420)
)

# Main game loop
def game_loop():
    # Create a clock to control the frame rate
    clock = pygame.time.Clock()
 
    running = True
 
    while running:
        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
 
        # Draw the background
        display_surface.blit(
            background_image,
            (0, 0)
        )
 
        # Draw the wildlife image
        display_surface.blit(
            wildlife_image,
            wildlife_rect
        )
 
        # Display the heading and fact
        display_surface.blit(
            heading_text,
            heading_rect
        )
 
        display_surface.blit(
            fact_text,
            fact_rect
        )
 
        # Update the screen
        pygame.display.flip()
 
        # Limit the game to 30 frames per second
        clock.tick(30)
 
    # Close Pygame
    pygame.quit()
 
 
# Run the application
if __name__ == "__main__":
    game_loop()
