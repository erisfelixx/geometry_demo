#багатокутник

import pygame
from .shape import Shape

class Polygon(Shape):
    def __init__(self, points):
        self.points = points  #список точок (екземпляри класу point)

    def calculate_area(self):
        #площа багатокутника (ф-ла шоеля)
        n = len(self.points)
        area = 0
        for i in range(n):
            x1, y1 = self.points[i].x, self.points[i].y
            x2, y2 = self.points[(i + 1) % n].x, self.points[(i + 1) % n].y
            area += x1 * y2 - y1 * x2
        return abs(area) / 2

    def calculate_perimeter(self):
        #периметр багатокутника
        n = len(self.points)
        perimeter = 0
        for i in range(n):
            x1, y1 = self.points[i].x, self.points[i].y
            x2, y2 = self.points[(i + 1) % n].x, self.points[(i + 1) % n].y
            perimeter += ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        return perimeter

    def move(self, dx, dy):
        for point in self.points:
            point.move(dx, dy)

    def draw(self, screen):
        pygame.draw.polygon(screen, (0, 255, 0), [(p.x, p.y) for p in self.points], 2)
