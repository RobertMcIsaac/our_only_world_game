import pygame

# List of fun facts
facts = [
    "Plastic waste can take up to 450 years to decompose in the ocean.",
    "Sea turtles have been around for over 100 million years!",
    "Over 8 million tons of plastic enter the ocean every year.",
    "Coral reefs support over 25% of all marine life."
]

def show_fact(screen, fact):
    """Displays a fact message at the bottom of the screen."""
    font = pygame.font.Font(None, 30)  # Move font initialization inside function
    fact_text = font.render(fact, True, (255, 255, 255))
    screen.blit(fact_text, (50, 500))
