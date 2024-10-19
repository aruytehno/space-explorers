import random
import pygame

class StarSystem:
    def __init__(self, width, height, star_count=100):
        self.width = width
        self.height = height
        self.star_count = star_count
        self.stars = self.generate_stars()

    def generate_stars(self):
        stars = []
        for _ in range(self.star_count):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(1, 3)
            stars.append((x, y, size))
        return stars

    def draw(self, screen):
        for star in self.stars:
            pygame.draw.circle(screen, (255, 255, 255), (star[0], star[1]), star[2])
