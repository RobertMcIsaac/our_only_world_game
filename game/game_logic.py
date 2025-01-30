import pygame
import random
import os

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Define the assets folder path
ASSETS_PATH = "game/assets/"

# Load images
# rubbish_images = ["assets/plastic_bag.png", "assets/bottle.png"]
rubbish_images = ["game/assets/coffee.png"]
sea_life_images = ["game/assets/butterfly-fish.png"]

class Item:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))  # Resize if needed
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))  # Centered
        self.category = "rubbish" if "plastic" in image_path or "bottle" in image_path else "sea_life"

    def draw(self, screen):
        """Draw the item on the screen."""
        screen.blit(self.image, self.rect)

def spawn_centered_item():
    """Spawns an item at the center of the screen."""
    if not rubbish_images or not sea_life_images:  # Safety check
        raise ValueError("Error: Image list is empty. Check file paths!")

    category = random.choice(["rubbish", "sea_life"])
    image_path = random.choice(rubbish_images if category == "rubbish" else sea_life_images)
    return Item(image_path)
