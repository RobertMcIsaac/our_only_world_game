import pygame
from game_logic import spawn_centered_item  # Now uses items.py
from ui import draw_buttons, handle_click
from facts import show_fact

# Initialize pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ocean Cleanup Game")

# Load background
background = pygame.image.load("game/assets/images/background_image.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load turtle character
turtle = pygame.image.load("game/assets/images/shelley_front.png")
turtle = pygame.transform.scale(turtle, (100, 100))


# Turtle position
turtle_x = 10
turtle_y = SCREEN_HEIGHT - turtle.get_height() - 10

# Start with an item
current_item = spawn_centered_item()
selected_fact = ""
fact_shown = False  # Track if a fact is being displayed

# Game loop
running = True
while running:
    screen.blit(background, (0, 0))  # Draw background
    screen.blit(turtle, (turtle_x, turtle_y))  # Draw turtle
    current_item.draw(screen, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50))  # Center the item
    draw_buttons(screen)  # Draw tick and cross buttons

    # Display fact if available
    if selected_fact:
        show_fact(screen, selected_fact)
        fact_shown = True  # Prevent further item interaction until the player clicks again

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if fact_shown:  # If fact is being displayed, reset and spawn a new item
                current_item = spawn_centered_item()  # Get a new item from `items.py`
                selected_fact = ""  # Clear fact
                fact_shown = False  # Allow next click
            else:  # If no fact is displayed, handle game logic
                selected_fact = handle_click(event, current_item)

    pygame.display.flip()

pygame.quit()
