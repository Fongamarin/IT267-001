from shape import Shape
from math import pi

class Square(Shape):
    def __init__(self, length = 0) -> None:
        super().__init__('Square')
        self.__length = length

    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self,value):
        self.__length = value
    
    #overiding
    def computer_area(self):
        super().computer_area()
        self.area = self.length ** 2
        #area มาจาก superclass Shape

    #newmethod
    def print_sqaure(self):
        print(f'{self.shape} area = {self.area:,.2f}')
        #shape มาจาก superclass Shape
class Circle(Shape):
    def __init__(self, radius = 0) -> None:
        super().__init__('Circle')
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,value):
        self.__radius = value
    
    #overiding
    def computer_area(self):
        super().computer_area()
        self.area = pi * (self.radius ** 2)
        #area มาจาก superclass Shape

    #newmethod
    def print_circle(self):
        print(f'{self.shape} area = {self.area:,.2f}')
        #shape มาจาก superclass Shape

class Triangle(Shape):
    def __init__(self,height = 0, base = 0) -> None:
        super().__init__('Square')
        self.__base = base
        self.__height = height

    @property
    def base(self):
        return self.base
    @base.setter
    def base(self,value):
        self.__base = value
    @property
    def height(self):
        return self.height
    @height.setter
    def height(self,value):
        self.__height = value
    #overiding
    def computer_area(self):
        super().computer_area()
        self.area = 0.5*self.height*self.base
        #area มาจาก superclass Shape

    #newmethod
    def print_triangle(self):
        self.computer_area()
        print(f'{self.shape} area = {self.area:,.2f}')
        #shape มาจาก superclass Shape