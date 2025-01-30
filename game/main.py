import pygame

# Initialize pygame
pygame.init()

# Game Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (0, 105, 148)  # Ocean blue

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ocean Cleanup Game")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(BG_COLOR)

    # Update display
    pygame.display.flip()

pygame.quit()
