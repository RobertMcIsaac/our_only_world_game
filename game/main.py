import pygame
from game_logic import spawn_centered_item
from ui import draw_buttons, handle_click

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

# Font for displaying facts
font = pygame.font.Font(None, 28)  # Adjust font size as needed

# Fact font color and position
FACT_COLOR = (0, 0, 0)  # Light blue
FACT_Y_POSITION = 20  # Near the top

def show_fact(screen, message):
    """Displays a multi-line fact message at the top center of the screen."""
    lines = message.split("\n")  # Split fact into multiple lines
    y_offset = FACT_Y_POSITION  # Start near the top

    for line in lines:
        text_surface = font.render(line, True, FACT_COLOR)
        text_width = text_surface.get_width()
        x_position = (SCREEN_WIDTH - text_width) // 2  # Center horizontally
        screen.blit(text_surface, (x_position, y_offset))
        y_offset += 30  # Move down for the next line


# Game loop
running = True
while running:
    screen.blit(background, (0, 0))  # Draw background
    screen.blit(turtle, (turtle_x, turtle_y))  # Draw turtle
    # Adjust Y-position to move item further down
    ITEM_Y_OFFSET = 60  # Increase this value to move it further down

    # Draw the current item lower on the screen
    current_item.draw(screen, (
        (SCREEN_WIDTH - current_item.image.get_width()) // 2,
        ((SCREEN_HEIGHT - current_item.image.get_height()) // 2) + ITEM_Y_OFFSET  # Move item down
    ))
    draw_buttons(screen)  # Draw tick and cross buttons

    # Display fact if available
    if selected_fact:
        show_fact(screen, selected_fact)
        fact_shown = True  # Prevent further item interaction until the player clicks again

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Game is quitting...")  # Debugging output
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse clicked")  # Debugging output
            if fact_shown:  # If fact is being displayed, reset and spawn a new item
                print("Fact acknowledged, spawning new item...")  # Debugging output
                current_item = spawn_centered_item()  # Get a new item from `items.py`
                selected_fact = ""  # Clear fact
                fact_shown = False  # Allow next click
            else:  # If no fact is displayed, handle game logic
                print("Checking button clicks...")  # Debugging output
                fact = handle_click(event, current_item)
                if fact:  # Only update if a fact was returned
                    selected_fact = fact

    pygame.display.flip()

pygame.quit()
