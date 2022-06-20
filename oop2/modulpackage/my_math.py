PI = 3.1416

def square(number):
    #return (number * number)
    return (number **2)

def circle_area(radius):
    area = PI * radius * radius
    return area

if __name__ == "_main_":
    print(square(5))
    print(circle_area(1))
    print(PI)
