import pygame
from shapes.circle import Circle
from shapes.line_segment import LineSegment
from shapes.polygon import Polygon
from shapes.point import Point
from shapes.transformations import translate
from operations.intersection import intersection

# Ініціалізація Pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
COMMAND_HEIGHT = 200
CANVAS_HEIGHT = SCREEN_HEIGHT - COMMAND_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geometry Viewer")

font = pygame.font.Font(None, 36)
running = True
menu_active = True
shapes = []
active_shape_index = -1

commands = [
    "1. Додати фігуру (Circle, Line, Polygon)",
    "2. Перевірити перетин двох фігур",
    "3. Переглянути властивості активної фігури",
    "4. Об'єднати дві фігури",
    "5. Вийти"
]

def draw_menu():
    """Малює меню з командами у верхній частині вікна."""
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, SCREEN_WIDTH, COMMAND_HEIGHT))
    title = font.render("Виберіть команду:", True, (0, 0, 0))
    screen.blit(title, (10, 10))
    
    for i, command in enumerate(commands):
        text = font.render(command, True, (0, 0, 0))
        screen.blit(text, (10, 50 + i * 30))

def draw_canvas():
    """Малює полотно для фігур у нижній частині вікна."""
    pygame.draw.rect(screen, (255, 255, 255), (0, COMMAND_HEIGHT, SCREEN_WIDTH, CANVAS_HEIGHT))
    for shape in shapes:
        shape.draw(screen)

def get_user_input(prompt):
    """Отримує введення від користувача через консоль."""
    print(prompt)
    return input("> ")

def add_figure():
    """Додає нову фігуру за вибором користувача."""
    figure_type = get_user_input("Оберіть тип фігури (circle, line, polygon):").strip().lower()

    if figure_type == "circle":
        x = int(get_user_input("Введіть координату x центру:"))
        y = int(get_user_input("Введіть координату y центру:"))
        radius = int(get_user_input("Введіть радіус кола:"))
        shapes.append(Circle(x, y + COMMAND_HEIGHT, radius))
    elif figure_type == "line":
        x1 = int(get_user_input("Введіть x початкової точки:"))
        y1 = int(get_user_input("Введіть y початкової точки:"))
        x2 = int(get_user_input("Введіть x кінцевої точки:"))
        y2 = int(get_user_input("Введіть y кінцевої точки:"))
        shapes.append(LineSegment(Point(x1, y1 + COMMAND_HEIGHT), Point(x2, y2 + COMMAND_HEIGHT)))
    elif figure_type == "polygon":
        num_points = int(get_user_input("Введіть кількість точок багатокутника:"))
        points = []
        for i in range(num_points):
            x = int(get_user_input(f"Введіть x для точки {i + 1}:"))
            y = int(get_user_input(f"Введіть y для точки {i + 1}:"))
            points.append(Point(x, y + COMMAND_HEIGHT))
        shapes.append(Polygon(points))
    else:
        print("Невідомий тип фігури.")

def check_intersection():
    """Перевіряє перетин двох фігур."""
    if len(shapes) < 2:
        print("Недостатньо фігур для перевірки перетину.")
        return
    
    # Запитуємо індекси фігур для перевірки
    index1 = int(get_user_input("Введіть індекс першої фігури (0 для першої):"))
    index2 = int(get_user_input("Введіть індекс другої фігури (1 для другої):"))

    if index1 < 0 or index1 >= len(shapes) or index2 < 0 or index2 >= len(shapes):
        print("Некоректний індекс фігури.")
        return

    shape1 = shapes[index1]
    shape2 = shapes[index2]

    # Використовуємо функцію intersection
    if intersection(shape1, shape2):
        print("Фігури перетинаються!")
    else:
        print("Фігури не перетинаються.")

def set_active_shape():
    """Задає активну фігуру для перегляду властивостей."""
    if len(shapes) == 0:
        print("Немає доступних фігур.")
        return

    # Запитуємо індекс активної фігури
    index = int(get_user_input("Введіть індекс фігури (0 для першої):"))

    if index < 0 or index >= len(shapes):
        print("Некоректний індекс фігури.")
        return

    global active_shape_index
    active_shape_index = index
    print(f"Активна фігура: {type(shapes[active_shape_index]).__name__}")

def view_properties():
    """Виводить властивості активної фігури."""
    if active_shape_index == -1 or active_shape_index >= len(shapes):
        print("Немає активної фігури.")
        return
    shape = shapes[active_shape_index]
    print(f"Властивості фігури ({type(shape).__name__}):")
    print(f"  Площа: {shape.calculate_area()}")
    print(f"  Периметр: {shape.calculate_perimeter()}")

def combine_figures():
    """Об'єднує дві фігури, переміщуючи їх для дотику."""
    if len(shapes) < 2:
        print("Недостатньо фігур для об'єднання.")
        return

    shape1 = shapes[-2]
    shape2 = shapes[-1]

    if isinstance(shape1, Circle) and isinstance(shape2, Circle):
        dx = shape2.x - shape1.x
        dy = shape2.y - shape1.y
        distance = ((dx) ** 2 + (dy) ** 2) ** 0.5
        overlap = shape1.radius + shape2.radius - distance
        if overlap > 0:
            translate(shape2, -dx * overlap / distance, -dy * overlap / distance)
    else:
        print("Об'єднання реалізовано лише для кіл.")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                add_figure()
            elif event.key == pygame.K_2:
                check_intersection()
            elif event.key == pygame.K_3:
                set_active_shape()
                view_properties()
            elif event.key == pygame.K_4:
                combine_figures()
            elif event.key == pygame.K_5:
                running = False

    # Малюємо меню та полотно
    draw_menu()
    draw_canvas()
    pygame.display.flip()

pygame.quit()
