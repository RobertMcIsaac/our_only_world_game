import pygame

class UI:
    def __init__(self, font_path, screen):
        self.font = pygame.font.Font(font_path, 24)
        self.screen = screen
        self.score = 0

    def display_score(self):
        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

    def increase_score(self):
        self.score += 10
