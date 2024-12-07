#функції для малювання у Pygame

def draw_circle(screen, x, y, radius, color=(0, 0, 255)):
    import pygame
    pygame.draw.circle(screen, color, (int(x), int(y)), int(radius))

def draw_line(screen, start, end, color=(0, 0, 255)):
    import pygame
    pygame.draw.line(screen, color, start, end, 2)

def draw_polygon(screen, points, color=(0, 255, 0)):
    import pygame
    pygame.draw.polygon(screen, color, points, 2)
