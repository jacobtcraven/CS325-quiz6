from abc import ABC, abstractmethod

class Shape():
    def get_area(self, length, width):
        print("Processing payment")

class SetWidthHeight:
    def set_width(self, width):
        raise NotImplementedError("Subclass must implement width")

    def set_height(self, height):
        raise NotImplementedError("Subclass must implement height")

class Circle(Shape, SetWidthHeight):
    def get_area(self):
        return 3.14 * self.height * self.width
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
class Square(Shape, SetWidthHeight):
    def get_area(self):
        return self.width * self.height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
class Rectangle(Shape):
    def get_area(self, length, width):
        return length * width
    
class Triangle(Shape):
    def get_area(self, base, height):
        return 0.5 * base * height
    
def get_area(shape):
    if isinstance(shape, SetWidthHeight):
        shape.set_width(5)
        shape.set_height(10)
        shape.get_area(shape.width, shape.height)
    else:
        print("Shape does not have a set width and height")



if __name__ == "__main__":
    circle = Circle()
    circle.set_width(5)
    circle.set_height(10)
    print(circle.get_area())
    square = Square()
    square.set_width(5)
    square.set_height(10)
    print(square.get_area())
    rectangle = Rectangle()
    print(rectangle.get_area(5, 10))
    triangle = Triangle()
    print(triangle.get_area(5, 10))