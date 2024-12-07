from math import sqrt
from shapes.circle import Circle
from shapes.polygon import Polygon
from shapes.line_segment import LineSegment
from shapes.point import Point

def circles_intersect(circle1, circle2):
    """Перевірка перетину двох кіл."""
    distance = sqrt((circle1.x - circle2.x) ** 2 + (circle1.y - circle2.y) ** 2)
    return distance <= (circle1.radius + circle2.radius)

def point_in_circle(point, circle):
    """Перевіряє, чи знаходиться точка всередині кола."""
    distance = sqrt((point.x - circle.x) ** 2 + (point.y - circle.y) ** 2)
    return distance <= circle.radius

def polygon_circle_intersect(polygon, circle):
    """Перевірка перетину багатокутника і кола."""
    # Перевіряємо, чи одна з точок багатокутника всередині кола
    for point in polygon.points:
        if point_in_circle(point, circle):
            return True

    # Перевіряємо перетин ребер багатокутника з колом
    n = len(polygon.points)
    for i in range(n):
        p1 = polygon.points[i]
        p2 = polygon.points[(i + 1) % n]
        if line_segment_circle_intersect(LineSegment(p1, p2), circle):
            return True

    return False

def line_segment_circle_intersect(segment, circle):
    """Перевіряє, чи перетинається відрізок з колом."""
    ax, ay = segment.start.x, segment.start.y
    bx, by = segment.end.x, segment.end.y
    cx, cy, r = circle.x, circle.y, circle.radius

    # Вектор AB
    ABx = bx - ax
    ABy = by - ay

    # Вектор AC
    ACx = cx - ax
    ACy = cy - ay

    # Проекція вектора AC на AB
    t = (ACx * ABx + ACy * ABy) / (ABx ** 2 + ABy ** 2)

    # Найближча точка на відрізку до центру кола
    t = max(0, min(1, t))
    nearest_x = ax + t * ABx
    nearest_y = ay + t * ABy

    # Відстань від найближчої точки до центру кола
    distance = sqrt((nearest_x - cx) ** 2 + (nearest_y - cy) ** 2)
    return distance <= r

def line_segments_intersect(line1, line2):
    """Перевіряє, чи перетинаються два відрізки."""
    def ccw(a, b, c):
        return (c.y - a.y) * (b.x - a.x) > (b.y - a.y) * (c.x - a.x)

    def intersect(p1, q1, p2, q2):
        return (ccw(p1, p2, q2) != ccw(q1, p2, q2)) and (ccw(p1, q1, p2) != ccw(p1, q1, q2))

    return intersect(line1.start, line1.end, line2.start, line2.end)

def intersection(obj1, obj2):
    """Універсальна функція для перевірки перетину фігур."""
    if isinstance(obj1, Circle) and isinstance(obj2, Circle):
        return circles_intersect(obj1, obj2)
    elif isinstance(obj1, Polygon) and isinstance(obj2, Circle):
        return polygon_circle_intersect(obj1, obj2)
    elif isinstance(obj1, Circle) and isinstance(obj2, Polygon):
        return polygon_circle_intersect(obj2, obj1)
    elif isinstance(obj1, LineSegment) and isinstance(obj2, LineSegment):
        return line_segments_intersect(obj1, obj2)
    else:
        raise TypeError("Непідтримувані типи для перевірки перетину.")
