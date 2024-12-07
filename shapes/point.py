#точка

from .shape import Shape

class Point(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_area(self):
        return 0  #точка не має площі

    def calculate_perimeter(self):
        return 0  #точка не має периметра

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        import pygame
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), 2)
