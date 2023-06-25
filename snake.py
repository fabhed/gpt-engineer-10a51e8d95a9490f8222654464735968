import pygame
from dataclasses import dataclass

@dataclass
class SnakeSegment:
    x: int
    y: int

class Snake:
    def __init__(self, x, y, size):
        self.size = size
        self.segments = [SnakeSegment(x, y)]
        self.direction = (1, 0)

    def move(self):
        x, y = self.segments[0].x + self.direction[0] * self.size, self.segments[0].y + self.direction[1] * self.size
        self.segments.insert(0, SnakeSegment(x, y))
        self.segments.pop()

    def grow(self):
        self.segments.append(self.segments[-1])

    def draw(self, screen):
        for segment in self.segments:
            pygame.draw.rect(screen, (255, 255, 255), (segment.x, segment.y, self.size, self.size))
