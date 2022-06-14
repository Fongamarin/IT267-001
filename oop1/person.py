class Person :
    def __init__(self,name,gender,profession,study) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study2 = study
    

    def work(self):
        print(f"{self.name} is workig as a{self.profession}")

    def study(self):
        print(f"{self.name} studies for {self.study2}hour(s)")
        
    def show(self):
        print(f"Name:{self.name} Gender: {self.gender} perfession : {self.profession} study : {self.study2}")

    #create object
jessa_obj= Person ("Jessa","Male","Software Engineer",10)
jessa_obj.show()
jessa_obj.work()
jessa_obj.study()

jon_obj= Person ("Jon","Male","doctor",15)
jon_obj.show()
jon_obj.work()
jon_obj.study()

lalisa_obj= Person ("lalisa","Male","doctor",13)
lalisa_obj.work()



