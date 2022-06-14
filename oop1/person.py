class Person:
    country = "Thailand" #class variable
    def __init__(self,name,gender,profession,study) -> None:
        #instance  variables
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study2 = study


    def work(self):
        print(f"{self.name} is working as a {self.profession}")

    def study(self):
        print(f"{self.name} studies for {self.study2} hour(s)")

    def show(self):
        print(f"Name: {self.name} Gender: {self.gender} Profession: {self.profession} Study: {self.study2}")

#create object
jessa_obj = Person ("Jess","Male","Software Engineer",10)
jessa_obj.show()
jessa_obj.work()
jessa_obj.study()

jon_obj = Person ("Jon","Male","Doctor",15)
jon_obj.show()
jon_obj.work()
jon_obj.study()

lalisa_obj = Person ("Lalisa","Female","Korean Singer",13)
lalisa_obj.work()


print(f"Class Variable: {Person.country}")
print(f"Instance Variables: {lalisa_obj.country}")

#assign value
lalisa_obj.country = "Korea"
print("-------")
print(f"Class Variable: {Person.country}")
print(f"Instance Variables: {lalisa_obj.country}")
print(f"Instance Variables: {jon_obj.country}")

# assign class variable
Person.country = "England"
print(f"Class Variable: {Person.country}")
print(f"Instance Variables: {lalisa_obj.country}")
print(f"Instance Variables: {jon_obj.country}")