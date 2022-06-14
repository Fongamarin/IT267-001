class Rectangle:
    def __init__(self,width,length) -> None:
        self.windth = width
        self.length = width
        self.area = 0

    def get_data(self):
        pass

    def get_data(self):
        pass
    
    def compute_area(self):
        self.area= self.widt * self.length
    
    def print_area(self):
        print(f"Rectangle Area : {self.area}")

#create object
rec_obj = Rectangle(4,8)
rec_obj.compute_area()
rec_obj.print_area()