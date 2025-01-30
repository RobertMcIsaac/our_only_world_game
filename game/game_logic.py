from items import get_random_item

def spawn_centered_item():
    """Get a random item from the predefined list."""
    return get_random_item()  # Use teammate's function


# import pygame
# import random
# import os

# # Constants
# SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# # Define the assets folder path
# ASSETS_PATH = "game/assets/"

# # Load images
# rubbish_images = [
#     os.path.join(ASSETS_PATH, ""),
#     os.path.join(ASSETS_PATH, "")
# ]
# sea_life_images = [
#     os.path.join(ASSETS_PATH, ""),
#     os.path.join(ASSETS_PATH, "")
# ]

# class Item:
#     def __init__(self, image_path, category):
#         """Create an item with an image and a category ('rubbish' or 'sea_life')."""
#         self.image = pygame.image.load(image_path)
#         self.image = pygame.transform.scale(self.image, (100, 100))  # Resize if needed
#         self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))  # Centered
#         self.category = category  # Store the category directly

#     def draw(self, screen):
#         """Draw the item on the screen."""
#         screen.blit(self.image, self.rect)

# def spawn_centered_item():
#     """Spawns an item at the center of the screen with a correct category."""
#     if not rubbish_images or not sea_life_images:  # Safety check
#         raise ValueError("Error: Image list is empty. Check file paths!")

#     category = random.choice(["rubbish", "sea_life"])
#     if category == "rubbish":
#         image_path = random.choice(rubbish_images)
#     else:
#         image_path = random.choice(sea_life_images)

#     return Item(image_path, category)  # Pass the category explicitly