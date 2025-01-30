import pygame

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Load button images
tick = pygame.image.load("game/assets/tick.png")
cross = pygame.image.load("game/assets/cross.png")

# Resize buttons
tick = pygame.transform.scale(tick, (80, 80))
cross = pygame.transform.scale(cross, (80, 80))

# Button positions (below the item)
tick_rect = tick.get_rect(center=(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100))
cross_rect = cross.get_rect(center=(SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2 + 100))

def draw_buttons(screen):
    """Draw tick and cross buttons on the screen."""
    screen.blit(tick, tick_rect)
    screen.blit(cross, cross_rect)

def handle_click(event, current_item, show_fact):
    """Handles button clicks and determines if the player was correct."""
    if event.type == pygame.MOUSEBUTTONDOWN:
        if tick_rect.collidepoint(event.pos):  # Player clicked tick
            if current_item.category == "sea_life":
                show_fact(f"✅ Correct! {current_item.category} belongs in the ocean.")
            else:
                show_fact(f"❌ Wrong! {current_item.category} should not be in the ocean.")

        elif cross_rect.collidepoint(event.pos):  # Player clicked cross
            if current_item.category == "rubbish":
                show_fact(f"✅ Correct! {current_item.category} does not belong in the ocean.")
            else:
                show_fact(f"❌ Wrong! {current_item.category} is part of the ecosystem.")

