import pygame
from .shape import Shape

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (int(self.x), int(self.y)), int(self.radius), 2)
