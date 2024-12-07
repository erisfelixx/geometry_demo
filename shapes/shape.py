from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        """Обчислення площі фігури"""
        pass

    @abstractmethod
    def calculate_perimeter(self):
        """Обчислення периметра фігури"""
        pass

    @abstractmethod
    def move(self, dx, dy):
        """Переміщення фігури"""
        pass

    @abstractmethod
    def draw(self, screen):
        """Малювання фігури на екрані"""
        pass   