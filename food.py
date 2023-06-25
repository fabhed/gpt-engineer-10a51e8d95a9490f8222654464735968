import pygame
import random

class Food:
    def __init__(self, x_range, y_range, size):
        self.x = random.randint(x_range[0], x_range[1]) * size
        self.y = random.randint(y_range[0], y_range[1]) * size
        self.size = size

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.size, self.size))
