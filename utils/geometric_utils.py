 #допоміжні функції (обчислення площі, перевірка точок і тд)


from math import sqrt

def calculate_distance(point1, point2):
    """Обчислення відстані між двома точками."""
    return sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

def is_point_in_circle(point, circle):
    """Перевірка, чи точка знаходиться всередині кола."""
    distance = calculate_distance(point, circle)
    return distance <= circle.radius

def is_point_in_polygon(point, polygon):
    """Перевірка, чи точка знаходиться всередині багатокутника.
    Використовується алгоритм променевого перетину.
    """
    n = len(polygon.points)
    inside = False

    x, y = point.x, point.y
    for i in range(n):
        x1, y1 = polygon.points[i].x, polygon.points[i].y
        x2, y2 = polygon.points[(i + 1) % n].x, polygon.points[(i + 1) % n].y

        if min(y1, y2) < y <= max(y1, y2) and x <= max(x1, x2):
            if y1 != y2:
                xinters = (y - y1) * (x2 - x1) / (y2 - y1) + x1
            if x1 == x2 or x <= xinters:
                inside = not inside

    return inside

def calculate_polygon_centroid(polygon):
    """Обчислення центроїда (центру мас) багатокутника."""
    n = len(polygon.points)
    signed_area = 0
    cx = 0
    cy = 0

    for i in range(n):
        x1, y1 = polygon.points[i].x, polygon.points[i].y
        x2, y2 = polygon.points[(i + 1) % n].x, polygon.points[(i + 1) % n].y
        a = x1 * y2 - x2 * y1
        signed_area += a
        cx += (x1 + x2) * a
        cy += (y1 + y2) * a

    signed_area *= 0.5
    cx /= (6.0 * signed_area)
    cy /= (6.0 * signed_area)

    return cx, cy

def calculate_bounding_box(polygon):
    """Обчислення мінімального прямокутника, що охоплює багатокутник."""
    min_x = min(point.x for point in polygon.points)
    max_x = max(point.x for point in polygon.points)
    min_y = min(point.y for point in polygon.points)
    max_y = max(point.y for point in polygon.points)

    return min_x, min_y, max_x, max_y