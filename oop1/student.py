class Student:
    #major:str + "it"
    #major = "it"
    #major:"It" error
    def __init__(self,id:str,name:str,major:str = "IT"):
        self.id = id
        self.name = name
        self.major = major

    def display_detail(self):
        print(f"Id : {self.id}")
        print(f"Name : {self.name}")
        print(f"Major : {self.major}")

    def __del__(self):
        print("Object Destroyed")

if __name__ == "_main_":
    jes = Student("111","Jesica","IT")
    john = Student("112","John","MKT")
    amy = Student("113","Amy")

    jes.display_detail()
    john.display_detail() 
    amy.display_detail()
