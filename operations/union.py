#клас для обчислення об’єднання фігур

from shapes.polygon import Polygon

def union(polygon1, polygon2):
    """Об'єднання двох багатокутників (наївна реалізація, злиття точок)."""
    if isinstance(polygon1, Polygon) and isinstance(polygon2, Polygon):
        new_points = polygon1.points + polygon2.points
        #потрібна додаткова обробка для коректної геометрії
        return Polygon(new_points)
    return None
