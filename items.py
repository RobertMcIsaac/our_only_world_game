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

    def draw(self, screen, position): # Where to position item image
        screen.blit(self.image, position)  

# List of selected items
ITEMS = [
    Item("Octopus", "octopus.jpg", True, "Octopuses have nine brains and three hearts!"),
    Item("Jellyfish", "jellyfish.jpg", True, "Jellyfish have no brains!"),
    Item("Plastic Bottle", "plastic_bottle.jpg", False, "A plastic bottle takes 450 years to degrade!"),
    Item("Cans", "can.jpg", False, "Aluminum cans take 200 years to break down."),
    Item("Seaweed", "seaweed.jpg", True, "Seaweed produces most of the oxygen we breathe!"),
    Item("Fishnet", "fishnet.jpg", False, "Nets trap marine animals!"),
    Item("Coral", "coral.jpg", True, "Coral reefs support 25% of all marine life!"),
    Item("Plastic Bag", "plastic_bag.jpg", False, "Turtles mistake plastic bags for jellyfish and try to eat them!"),
    Item("Coffee Cup", "coffee_cup.jpg", False, "Most coffee cups have plastic linings and cannot easily degrade."),
    Item("Straws", "straws.jpg", False, "Straws are one of the top 10 plastic polluters in the ocean!")
]

def get_random_item():
    """Returns one random item from the list."""
    return random.choice(ITEMS)
