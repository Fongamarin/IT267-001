class Animal:
    #class varaiber
    animal = "cat"

    def new_animal(self,name:str,breed:str,color:str,age:int):
        #instance variable
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
    

    def print_detail(self):
        print(f"**********")
        print(f"Name: {self.name}")
        print(f"Animal: {self.animal}")
        print(f"Breed: {self.breed}")
        print(f"Color {self.color}")
        print(f"Age: {self.age}")

    def __del__(self):
            print(f'object was destroyed')

        #create object
if __name__ == "__main__":
        Animal.animal = "FISH"
        ula = Animal()
        ula.animal = "DOG"
        ula.new_animal("ula","Scottish","white",1)
        ula.print_detail()

        drac = Animal()
        drac.new_animal("Drac","Scottish","White",1)
        drac.print_detail()
        drac.breed = "Catfish"
        drac.print_detail()

        #เรียกดูข้อมูลของ opject ผ่านทางชื่อclass
        Animal.print_detail(ula) #ula.print_detail()
        Animal.print_detail(drac) #drac.print_detail()

        #เรียกดู class variableทั้งหมด
        print(f'{Animal.__dict__}')
        
        #เรียกดู instand variable
        print(f'{ula.__dict__}')

        peter = Animal()
        peter.new_animal("peter","Parrot","green yellow red",2)
        # add new attribute to petor
        peter.legs = 2
        print(f'{peter.__dict__}')

        
