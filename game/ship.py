import pygame
import random

class Ship:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = random.randint(100, 500)
        self.speed_x = random.choice([-1, 1]) * random.uniform(0.1, 1)
        self.speed_y = random.choice([-1, 1]) * random.uniform(0.1, 1)
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Ограничиваем движение по экрану
        if self.x < 0 or self.x > 800:
            self.speed_x = -self.speed_x
        if self.y < 0 or self.y > 600:
            self.speed_y = -self.speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)
