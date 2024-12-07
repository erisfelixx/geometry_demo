#відрізок

from .shape import Shape

class LineSegment(Shape):
    def __init__(self, start, end):
        self.start = start  #початкова точка (Point)
        self.end = end      #кінцева точка (Point)

    def calculate_area(self):
        return 0  #відрізок не має площі

    def calculate_perimeter(self):
        #довжина відрізка
        return ((self.start.x - self.end.x)**2 + (self.start.y - self.end.y)**2)**0.5

    def move(self, dx, dy):
        self.start.move(dx, dy)
        self.end.move(dx, dy)

    def draw(self, screen):
        import pygame
        pygame.draw.line(screen, (0, 0, 255), (int(self.start.x), int(self.start.y)), 
                         (int(self.end.x), int(self.end.y)), 2)
