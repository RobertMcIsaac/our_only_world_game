import pygame

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # Set the window size
FPS = 60  # Frames per second

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ocean Cleanup Game")

# Load images
background = pygame.image.load("game/assets/background_image.jpg")  # Load background image
# turtle = pygame.image.load("assets/turtle.png")  # Load turtle image

# Resize images if necessary
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale background
# turtle = pygame.transform.scale(turtle, (100, 100))  # Resize turtle if needed

# Set turtle position (bottom-left corner)
turtle_x = 10  # Slight padding from the left
# turtle_y = SCREEN_HEIGHT - turtle.get_height() - 10  # Slight padding from the bottom

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.blit(background, (0, 0))  # Draw background at (0,0)
    # screen.blit(turtle, (turtle_x, turtle_y))  # Draw turtle at bottom-left

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Quit the game loop

    pygame.display.flip()  # Update display
    clock.tick(FPS)  # Limit frame rate

pygame.quit()
