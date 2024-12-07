#функції трансформацій (переміщення, масштабування)
from math import cos, sin, radians

def translate(shape, dx, dy):
    """Перемістити фігуру на dx, dy."""
    shape.move(dx, dy)

def scale(shape, factor):
    """Масштабувати фігуру відносно центру."""
    if hasattr(shape, "points"):  #для багатокутника
        cx = sum(p.x for p in shape.points) / len(shape.points)
        cy = sum(p.y for p in shape.points) / len(shape.points)
        for point in shape.points:
            point.x = cx + factor * (point.x - cx)
            point.y = cy + factor * (point.y - cy)
    elif hasattr(shape, "x") and hasattr(shape, "y") and hasattr(shape, "radius"):  # Для кола
        shape.radius *= factor

def rotate(shape, angle):
    """Повернути фігуру на заданий кут (у градусах) навколо центру."""
    if hasattr(shape, "points"):  #для багатокутника
        cx = sum(p.x for p in shape.points) / len(shape.points)
        cy = sum(p.y for p in shape.points) / len(shape.points)
        angle = radians(angle)
        for point in shape.points:
            new_x = cx + (point.x - cx) * cos(angle) - (point.y - cy) * sin(angle)
            new_y = cy + (point.x - cx) * sin(angle) + (point.y - cy) * cos(angle)
            point.x, point.y = new_x, new_y
