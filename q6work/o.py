from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self, length, width):
        print("Processing payment")

class CircleArea(Shape):
    def get_area(self, radius):
        return 3.14 * radius * radius
    
class SquareArea(Shape):
    def get_area(self, side):
        return side * side
    
class RectangleArea(Shape):
    def get_area(self, length, width):
        return length * width
    
class TriangleArea(Shape):
    def get_area(self, base, height):
        return 0.5 * base * height
    

if __name__ == "__main__":
    circle = CircleArea()
    print(circle.get_area(5))
    square = SquareArea()
    print(square.get_area(5))
    rectangle = RectangleArea()
    print(rectangle.get_area(5, 10))
    triangle = TriangleArea()
    print(triangle.get_area(5, 10))