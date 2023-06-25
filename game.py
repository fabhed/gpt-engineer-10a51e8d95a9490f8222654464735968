import pygame
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.screen_size = (640, 480)
        self.snake_size = 20
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.screen_size[0] // 2, self.screen_size[1] // 2, self.snake_size)
        self.food = Food((0, self.screen_size[0] // self.snake_size - 1), (0, self.screen_size[1] // self.snake_size - 1), self.snake_size)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.snake.direction = (0, -1)
            elif keys[pygame.K_DOWN]:
                self.snake.direction = (0, 1)
            elif keys[pygame.K_LEFT]:
                self.snake.direction = (-1, 0)
            elif keys[pygame.K_RIGHT]:
                self.snake.direction = (1, 0)

            self.snake.move()

            if self.snake.segments[0].x == self.food.x and self.snake.segments[0].y == self.food.y:
                self.snake.grow()
                self.food = Food((0, self.screen_size[0] // self.snake_size - 1), (0, self.screen_size[1] // self.snake_size - 1), self.snake_size)

            self.screen.fill((0, 0, 0))
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(10)
