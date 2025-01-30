import pygame
import random
import uuid  # Import UUID module for unique identifiers

class Item:
    def __init__(self, name, image, belongs_in_sea, fact):
        self.id = str(uuid.uuid4())  # Generate a unique ID for each item
        self.name = name
        self.image = pygame.image.load(image)  
        self.belongs_in_sea = belongs_in_sea  # True = should be in the sea, False = should not
        self.fact = fact  
        self.image = pygame.transform.scale(self.image, (150, 150))

    def draw(self, screen, position): # Where to position item image
        screen.blit(self.image, position)  

# List of selected items
ITEMS = [
    Item("Octopus", "game/assets/images/octopus.jpg", True, "Octopuses have nine brains and three hearts!"),
    Item("Jellyfish", "game/assets/images/jellyfish.jpg", True, "Jellyfish have no brains!"),
    Item("Plastic Bottle", "game/assets/images/plastic_bottle.png", False, "A plastic bottle takes 450 years to degrade!"),
    Item("Cans", "game/assets/images/cans.png", False, "Aluminum cans take 200 years to break down."),
    Item("Seaweed", "game/assets/images/seaweed.png", True, "Seaweed produces most of the oxygen we breathe!"),
    Item("Fishnet", "game/assets/images/fishnet.jpg", False, "Nets trap marine animals!"),
    Item("Coral", "game/assets/images/coral.png", True, "Coral reefs support 25% of all marine life!"),
    Item("Plastic Bag", "game/assets/images/plastic_bag.png", False, "Turtles mistake plastic bags for jellyfish and try to eat them!"),
    Item("Coffee Cup", "game/assets/images/coffee_cup.png", False, "Most coffee cups have plastic linings and cannot easily degrade."),
    Item("Straws", "game/assets/images/straws.png", False, "Straws are one of the top 10 plastic polluters in the ocean!")
]

def get_random_item():
    """Returns one random item from the list."""
    return random.choice(ITEMS)
