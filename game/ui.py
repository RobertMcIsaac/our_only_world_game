import pygame

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Load button images
tick = pygame.image.load("game/assets/images/tick.png")
cross = pygame.image.load("game/assets/images/cross.png")

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

def handle_click(event, current_item):
    """Handles button clicks and returns the item's fact."""
    if event.type == pygame.MOUSEBUTTONDOWN:
        if tick_rect.collidepoint(event.pos):  # Player clicked tick
            if current_item.belongs_in_sea:
                return f"✅ Correct! {current_item.name} belongs in the ocean.\n{current_item.fact}"
            else:
                return f"❌ Wrong! {current_item.name} should not be in the ocean.\n{current_item.fact}"

        elif cross_rect.collidepoint(event.pos):  # Player clicked cross
            if not current_item.belongs_in_sea:
                return f"✅ Correct! {current_item.name} does not belong in the ocean.\n{current_item.fact}"
            else:
                return f"❌ Wrong! {current_item.name} is part of the ecosystem.\n{current_item.fact}"

    return None  # If no button was clicked
