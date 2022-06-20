#global variable
from tkinter import Variable


bird_type = 'parrot'

class Bird:
    #class variable
    bird_name = 'Peter'

    def __init__(self,color) -> None:
        #instance variable
        self.color = color

        #local variable
        country = 'Thailand'
        print(country)

    def show(self):
        return f'{Bird.bird_name} has {self.color}'

if __name__ == '__main__':
    print(f'***** {bird_type} *****') #เรียกใช้ global variable
    my_bird = Bird('Red,Yellow')
    print(my_bird.show())
    
    #เรียก class variable
    #print(Bird.bird_name) error

    #เรียก class variable
    print(Bird.bird_name)

    #ชื่อวัตถุclass_variable
    print(my_bird.bird_name)

    #เรียก instance variable
    #print(Bird.color)#eror

    #ชื่อวัตถุ instance Variable
    print(my_bird.color)
